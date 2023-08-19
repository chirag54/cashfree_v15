# -*- encoding: utf-8 -*-
{
    'name': 'Payment Acquirer: cashfree',
    'version': '1.0',
    'category': 'Accounting/Payment Providers',
    'sequence': 350,
    'author': 'Chirag Chauhan',
    'support': 'chauhanchirag662@gmail.com',
    'summary': "Cash free payment",
    'depends': ['payment'],
    'data': [
        'views/payment_provider_views.xml',
        'views/payment_cashfree_template.xml',
        'data/payment_provider_data.xml',
    ],
    'images': ['static/description/banner.png'],
    'application': False,
    'assets': {
        'web.assets_frontend': [

        ],
    },
    'price': 55.00,
    'currency': 'EUR',
    'uninstall_hook': 'uninstall_hook',
    'license': 'OPL-1',
}
