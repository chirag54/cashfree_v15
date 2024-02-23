from odoo import _, api, exceptions, fields, models

from odoo.addons.bus.models.bus import channel_with_db, json_dump

DEFAULT_MESSAGE = "Default message"

SUCCESS = "success"
DEFAULT = "default"


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.depends("create_date")
    def _compute_channel_names(self):
        for record in self:
            record.notify_success_channel_name = json_dump(
                channel_with_db(self.env.cr.dbname, record.partner_id)
            )

    notify_success_channel_name = fields.Char(compute="_compute_channel_names")
  

    def notify_success(
        self, message=None, title=None, sticky=False, target=None
    ):
        title = title or _("Success")
        self._notify_channel(SUCCESS, message, title, sticky, target)


    def _notify_channel(
        self,
        type_message=DEFAULT,
        message=DEFAULT_MESSAGE,
        title=None,
        sticky=False,
        target=None,
    ):
        if not (self.env.user._is_admin() or self.env.su) and any(
            user.id != self.env.uid for user in self
        ):
            raise exceptions.UserError(
                _("Sending a notification to another user is forbidden.")
            )
        if not target:
            target = self.partner_id
        bus_message = {
            "type": type_message,
            "message": message,
            "title": title,
            "sticky": sticky,
        }

        notifications = [[partner, "web.notify", [bus_message]] for partner in target]
        self.env["bus.bus"]._sendmany(notifications)
