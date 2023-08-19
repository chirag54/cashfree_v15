
{
    "name": "File Upload Snippet",
    "category": "Website",
    "summary": "eCommerce image Upload Category Snipped",
    'version': '1.0',
    "author": "Chirag Chauhan",
    'price': 10.00,
    'currency': 'EUR',
    "license": "OPL-1",
    "website": "",
    "depends": ["website"],
    "data": ["views/snippets.xml",
             "views/template.xml"
            ],
    "images": ["static/description/Home-My-Website.png"],
    "installable": True,
    "qweb": ["static/src/xml/*.xml"],
    "maintainers": ["chirag"],
    'assets': {
        'web.assets_frontend': [
            "/website_file_upload/static/src/css/file_uoload.css",
            "/website_file_upload/static/src/js/file_upload.js",
        ],
    },
}
