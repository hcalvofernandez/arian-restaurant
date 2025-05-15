# -*- coding: utf-8 -*-
{
    'name': "l10n_cu_website_sale",
    'summary': "Improve eCommerce in Cuba, adding support for addresses and municipalities.",
    'description': """
        The `l10n_cu_website_sale` module is designed to enhance eCommerce in Cuba, facilitating the management of 
        addresses and the integration of municipalities in the purchasing process.
        It provides a structure adapted to local needs, allowing companies to offer a more precise and personalized 
        shopping experience.
        This module is essential to optimize online sales, ensuring that addresses are handled appropriately 
        according to the Cuban context.
    """,
    "author": "Idola Odoo Team, Comunidad cubana de Odoo",
    'category': 'Website/Website',
    'version': '17.0.0.1',
    'depends': ['base', 'website_sale', 'l10n_cu_address'],
    'data': [
        'data/res_country_data.xml',
        'data/ir_model_fields.xml',
        'views/res_country_views.xml',
        'views/delivery_carrier_views.xml',
        'views/templates.xml',
    ],
    "assets": {
        'web.assets_frontend': [
            'l10n_cu_website_sale/static/src/**/*',
        ],
    },
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",

}
