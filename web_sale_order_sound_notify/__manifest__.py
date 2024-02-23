{
    "name": "Web Sale Order Sound Notify",
    "category":"Website",
    "summary": """
        Send Sale Order notification messages to Admin with Sound""",
    "version": "16",
    "license": "AGPL-3",
    "Versions":"15,16",
    "author": "Chirag Chauhan",
    "development_status": "",
    "website": "",
    "depends": ["sale","web","bus", "base", "mail","payment"],
    "images": ["static/description/notify.png"],
    "installable": True,
    "maintainers": ["chirag"],
    "assets": {
        "web.assets_backend": [
            "/web_sale_order_sound_notify/static/src/js/services/notification_services.esm.js",
        ]
    },
    'price': 40.00,
    'currency': 'EUR',
}
