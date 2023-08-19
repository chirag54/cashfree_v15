from . import models, controllers

from odoo.addons.payment import reset_payment_acquirer


def uninstall_hook(cr, registry):
    reset_payment_provider(cr, registry, 'cashfree')