# -*- coding: utf-8 -*-
{
    'name': "User Wizard",

    'summary': """
        Wizard to create user""",

    'description': """
        Wizard to create user with company and access groups details
    """,

    
    'developer': "Deepshikha Varma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/views.xml',
        'wizard/wizard_user.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}