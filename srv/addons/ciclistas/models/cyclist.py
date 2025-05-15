# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Cyclist(models.Model):
    _name = 'cyclist'
    _description = 'Cyclist'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    cycling_modality_ids = fields.Many2many(
        'cycling.modality',
        'cyclist_cycling_modality_rel',
        'cyclist_id',
        'modality_id',
        string='Cycling Modalities'
    )
