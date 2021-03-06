# -*- coding: utf-8 -*-
{
    'name': "Development Tools",

    'summary': """
    Development Helper, upgrade custom modules easily.
    Works in Community and Enterprise""",

    'description': """
    Development Helper, upgrade custom modules easily.
    Works in Community and Enterprise
    """,

    'author': "Ubay Abdelgadir",
    'website': "http://www.github.com/obayit/dev_tools",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '2.2',
    'license': 'LGPL-3',
    'support': 'obayit@gmail.com',

    # any module necessary for this one to work correctly
    'depends': ['base', 'bus'],

    # always loaded
    'data': [
        'views/assets.xml',
        'views/views_ir_model.xml',
    ],

    'qweb': [
        "static/src/xml/*.xml",
    ],
    'images': [
        'static/description/screenshot_1.png',
        'static/description/screenshot_2.png',
        'static/description/screenshot_3.png'
    ]
}
