from odoo import models, fields

class CyclingModality(models.Model):
    _name = 'cycling.modality'
    _description = 'Cycling Modality'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')