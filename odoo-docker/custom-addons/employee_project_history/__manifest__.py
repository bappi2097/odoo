# -*- coding: utf-8 -*-
{
    'name': 'Employee Project History',
    'summary': "This module use for employee module.",
    'category': 'Human Resource',
    'author': 'Bappi Saha',
    'version': '1.0.0',
    'website': 'https://bjitgroup.com',
    'license': 'LGPL-3',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/employee_project_history_views.xml',
    ],
    'sequence': 0,
    'application': True
}
