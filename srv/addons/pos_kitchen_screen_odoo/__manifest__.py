# -*- coding: utf-8 -*-
#############################################################################
#
#   Odoo Kitchen Screen
#############################################################################
{
    'name': 'POS Kitchen Screen',
    'version': '17.0.1.0.4',
    'category': 'Point Of Sale',
    'summary': 'POS Kitchen Screen facilitates sending certain orders '
               'automatically to the kitchen.The POS Kitchen Screen allows for'
               'the customization of order views, so that staff can see the '
               'information that is most important to them.',
    'description': 'The POS Kitchen Screen in Odoo 17 is a feature that '
                   'allows restaurant staff to view and manage orders in '
                   'real-time from the kitchen. This screen provides a clear '
                   'and organized display of all active orders, enabling '
                   'kitchen staff to prioritize and manage their tasks '
                   'efficiently. The POS Kitchen Screen in Odoo 16 also '
                   'allows for the customization of order views, so that '
                   'staff can see the information that is most important to '
                   'them. Additionally, this feature facilitates '
                   'communication between front-end and back-end staff, '
                   'enabling them to work together seamlessly and provide a '
                   'better dining experience for customers.',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['pos_restaurant'],
    'data': [
        'security/pos_kitchen_screen_groups.xml',
        "security/ir.model.access.csv",
        'data/kitchen_screen_sequence_data.xml',
        "views/kitchen_screen_views.xml",
        "views/pos_kitchen_screen_odoo_menus.xml",
        "views/pos_order_views.xml",
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_kitchen_screen_odoo/static/src/js/fields_load.js',
            'pos_kitchen_screen_odoo/static/src/js/order_payment.js',
            'pos_kitchen_screen_odoo/static/src/js/order_button.js',
        ],
        'web.assets_backend': [
            'pos_kitchen_screen_odoo/static/src/css/kitchen_screen.css',
            'pos_kitchen_screen_odoo/static/src/js/kitchen_screen.js',
            'pos_kitchen_screen_odoo/static/src/xml/kitchen_screen_templates.xml',
            'https://code.jquery.com/jquery-1.10.2.min.js',
            'https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js',
            'https://fonts.googleapis.com',
            'https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js',
            'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js',
        ],
    },
    'images': [
        'static/description/banner.jpg',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
