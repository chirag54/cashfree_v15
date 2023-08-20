from odoo import http
from odoo.http import request
import base64
from odoo.addons.website_sale.controllers.main import WebsiteSale as Base


class WebsiteSale(Base):
    @http.route('/upload_document', redirect=None, type='http', auth='public', website=True)
    def upload_document_form(self, **post):


        if post.get('attachment_1'):
            name = post.get('attachment_1').filename
            file = post.get('attachment_1')
            attachment = request.env['ir.attachment']
            attachment_id = attachment.sudo().create({
                'name': name,
                'type': 'binary',
                'datas': base64.b64encode(file.read())
                })

