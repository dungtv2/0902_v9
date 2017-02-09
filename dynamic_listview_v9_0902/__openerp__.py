{
    'name': 'Dynamic ListView V9',
    'summary': 'Change The Odoo List view On the fly without any technical knowledge',
    'version': '1.0',
    'category': 'Web',
    'description': """

    """,
    'author': "Odoo Optima",
    'website': '',
    'depends': ['web'],
    'data': ['templates.xml',
             'security/show_fields_security.xml',
             'security/ir.model.access.csv'],
    'price': 299.99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': ['static/src/xml/listview_button_view.xml'],
    'images': [
        'images/4.jpg',
    ],
}
