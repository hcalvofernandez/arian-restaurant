# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# List of contributors:
# Bernardo Yaser León Ávila <bernardo@idola.it>
# Yunior Rafael Hernández Cabrera <yunior@idola.it>
# Yusnel Rojas Garcia
# Julio Smith
# Segu
# Javier Escobar
# hcalvofernandez (scnetisla@gmail.com)

{
    "name": "Cuba - Localización Contable",
    "version": "17.0.1.0.0",
    "category": "Localization",
    "summary": "Plan contable y localización para Cuba",
    "depends": [
        "account",
        "base_iban",
        "om_account_accountant",  # Odoo Mate
        # otros módulos OM si los usas
    ],
    'data': [
        'data/account_chart_data.xml',        
        'data/account.account.template-common.csv',
        'data/account.account.template-tcp.csv',
        'data/account.account.template-private.csv',
        'data/account.account.template-public.csv',
        'data/account_chart_post_data.xml',
        'data/account_group_template_data.xml',
         # 'data/account_tax_template_data.xml',
        # 'data/account_fiscal_position_template_data.xml',
        # 'data/account_fiscal_position_tax_template_data.xml',
        # 'data/account_chart_template_data.xml',
        # 'data/res_cnae_data.xml',
        "views/account_views.xml",
        "views/res_company_views.xml",
        "views/expense_element_views.xml",
        "security/ir.model.access.csv"
    ],
    'license': 'LGPL-3',
}
