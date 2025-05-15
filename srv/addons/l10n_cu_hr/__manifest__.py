# List of contributors:
# Segu

{
     'name': 'Cuba - RRHH',
     'version': '17.0',
     'category': 'Human Resources',
     'summary': """
        Empleados, tarjetas de asistencias.
     """,
     'author': 'Comunidad Cubana de Odoo',
     'depends': ["hr"],
     'auto_install': True,     
     'data': [
          "data/hr_data.xml",
          "data/resource_data.xml",
          "views/assistance_cards_template.xml",
          "reports/report_assistance_cards.xml",
          "wizards/assistance_cards_wizard.xml",
          "security/ir.model.access.csv"
     ],
     'license': 'LGPL-3',
}
