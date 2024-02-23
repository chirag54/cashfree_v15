{
    "name": "Web Sale Order Sound Notify",
    "category":"Website",
    "summary": """
        Send Sale Order notification messages to Admin with Sound""",
    "version": "16",
    "license": "AGPL-3",
    "author": "Chirag Chauhan",
    "development_status": "",
    "website": "",
    "depends": ["web","sale", "bus", "base", "mail","payment"],
    "images": ["static/description/notify.png"],
    "installable": True,
    "maintainers": ["chirag"],
    "assets": {
        "web.assets_backend": [
            "/web_sale_order_sound_notify/static/src/js/services/notification_services.esm.js",
        ]
    },
    'price': 28.00,
    'currency': 'EUR',
}
