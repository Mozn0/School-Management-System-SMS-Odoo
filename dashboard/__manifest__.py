# -*- coding: utf-8 -*-
{
    'name': 'School Management Reports',
    'version': '1.0',
    'category': 'Education',
    'sequence': 2,
    'depends': ['school_core', 'website',],
    'data': [
        'security/dashboard_security.xml',
        'views/dashboard_views.xml',
    ],
    'installable': True,
    'application': True,
}
