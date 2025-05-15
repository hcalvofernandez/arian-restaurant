# -*- coding: utf-8 -*-
{
    'name': 'Ciclistas',
    'version': '1.0.0',
    'summary': """ Ciclistas Summary """,
    'author': 'Hanoi Calvo Fernández',
    'company': 'Hanoi Calvo Fernández',
    'website': 'https://www.hanoicalvo.com',
    'category': 'Ciclismo',
    'depends': ['base', 'web' , 'mail'],
    "data": [
        "views/cycling_modality_views.xml",
        "views/cyclist_views.xml",
    ],
    'application': True,
    'installable': True,
}
