# -*- coding: utf-8 -*-
from odoo import fields, models, api
from playsound import playsound
import os
import time

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the full path to the MP3 file
mp3_file_path = os.path.join(current_directory, 'ring.mp3')



# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     @api.model_create_multi
#     def create(self, vals):
#         res = super(SaleOrder, self).create(vals)
#         if vals[0].get('website_id'):
#             channel = self.env['mail.channel'].search([('name', '=', 'sales')],limit=1)
#             if channel:
#                 channel.message_post(body="New sale order created: %s" % res.name, message_type="comment", subtype_xmlid="mail.mt_comment")
#                 uid = self.env.uid
#                 user_id = self.env['res.users'].sudo().search([('id','=',2)])
#                 message="New sale order created: %s" % res.name
#                 user_id.notify_success(message)
#                 # playsound(mp3_file_path)
#         return res

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'



    @api.model_create_multi
    def create(self, vals):
        res = super(PaymentTransaction, self).create(vals)
        channel = self.env['mail.channel'].search([('name', '=', 'sales')],limit=1)
        if channel:
            channel.message_post(body="New sale order created: %s" % res.reference, message_type="comment", subtype_xmlid="mail.mt_comment")
            # print(res.user_id)
            # uid = self.env.uid
            user_id = self.env['res.users'].sudo().search([('id','=',2)])
            message="New sale order created: %s" % res.reference
            print(">>>>>",user_id)
            user_id.notify_success(message)
            # playsound(mp3_file_path)
        return res