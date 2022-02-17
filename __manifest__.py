# -*- coding: utf-8 -*-
{
    'name': "Hotel",

    'sequence': 1,

    'description': """
        gestion et le suivi des hotels de taf_tech informatique
    """,

    'author': "Melax_dev",
    'website': "https://gitlab.melaximport.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
            'views/chambre.xml',
            'views/client.xml',
            'views/personnel.xml',
            # 'views/paiement.xml',
            'views/reservation.xml',
            'views/specification.xml',
            'menu/menu.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'auto_install': False,
    'application':True,
}