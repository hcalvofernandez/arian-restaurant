# -*- coding: utf-8 -*-
# Part of Creyox Technologies
{
    'name': 'POS Network Printer | POS Order Receipt Printer | ESC/POS Printer',
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    'category': 'Point of Sale',
    'summary': """
        This module allow users to direct print the PoS order receipt within the same network,
        POS Network Printer,
        POS Network Printer in Odoo,
        IP Network Printer Drivers,
        IP Network Printer Drivers in Odoo,
        ESC/POS Printer in Odoo,
        ESC/POS Printer,
        Direct Printer PoS Order Receipt,
        Direct Printer PoS Order Receipt in Odoo,
        Direct Printer PoS Invoice Receipt,
        Direct Printer PoS Invoice Receipt in Odoo,
        Direct Printer PoS Restaurant Receipt in Odoo,
        Direct Printer PoS Restaurant Receipt,
        Best Network Printer in Odoo,
    """,
    "license": "OPL-1",
    'version': '17.0',
    'description': """
        IP network ESC/POS printer drivers for point-of-sale
        enables the use of your IP-based ESC/POS printer in conjunction with Odoo Point of Sale
        You won't need an IoT Box after installing this app to print POS tickets and receipts.
        Installing this app only requires connecting your POS printer to the same network as your Odoo POS.
        Set the printer's IP address and port using the Point of Sale configuration menu.
    """,
    'depends': ['point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/pos_config_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'external_dependencies': {
        'python': ['python-escpos'],
    },
    'assets': {
        'point_of_sale._assets_pos': [
            'cr_pos_network_printer/static/src/**/*',
        ],
    },
    "images": ["static/description/banner.gif"],
    "price": 99,
    "currency": "USD"
}
