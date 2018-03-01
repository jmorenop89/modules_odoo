# -*- coding: utf-8 -*-
{
    'name': "Academic Module",

    'summary': """
        Implements a new module for academic purposes.
    """,

    'description': """
    Adds classes Career and Student.
    """,

    'author': "CRR",
    'website': "http://www.crr.com",

    'category': 'Academic',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
     #   'security/ir.model.access.csv',
        'views/views.xml',
     #   'views/data_tipos.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
#        'demo/demo.xml',
    ],
}