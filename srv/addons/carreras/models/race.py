from odoo import models, fields

class Race(models.Model):
    _name = 'race'
    _description = 'Race'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    participants_ids = fields.Many2many('res.partner', string='Participants')
    results = fields.One2many('race.result', 'race_id', string='Results')

class RaceResult(models.Model):
    _name = 'race.result'
    _description = 'Race Result'

    race_id = fields.Many2one('race', string='Race', required=True)
    partner_id = fields.Many2one('res.partner', string='Participant', required=True)
    position = fields.Integer(string='Position')