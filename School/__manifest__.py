# -*- coding: utf-8 -*-
{
    'name': "Daffodil International University",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Israt",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    "installable": True,
    "application": True,
    "auto_install": False,
    # always loaded
    'data': [
        #security
        "security/ir.model.access.csv",
        #views
        "views/student.xml",
        "views/teacher.xml",
        "views/section.xml",
        "views/course.xml",
        "views/registration.xml",
        #menus
        "views/menu.xml",

    ],
    # only loaded in demonstration mode

}