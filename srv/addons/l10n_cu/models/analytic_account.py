# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ExpenseElement(models.Model):
    _name = "expense.element"
    _description = 'Expense element'
    _parent_store = True

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    parent_id = fields.Many2one('expense.element', index=True, ondelete='set null', readonly=False, store=True)
    parent_path = fields.Char(index=True, unaccent=False)
    child_ids = fields.One2many('expense.element', 'parent_id')
    company_id = fields.Many2one('res.company', required=True, readonly=True, default=lambda self: self.env.company)

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        res._create_aa_childs()
        return res

    def _create_aa_childs(self):
        """Crea las cuentas analíticas correspondientes a la combinación cuenta analítica - elemento de gastos.
        No se crean los existentes. Si cambia la jerarquía de elementos, se desactivan las cuentas no válidas porque los elementos dejaron de ser hojas."""
        expense_elements = self.search([('child_ids', '=', False)])
        current_accounts = self.env['account.analytic.account'].search([('element_id', 'in', expense_elements.ids)])
        pending_elements = expense_elements - current_accounts.element_id
        elements_to_delete = self.env['account.analytic.account'].search([('element_id', 'not in', expense_elements.ids)])
        elements_tocreate = []
        for record in self.env['account.analytic.account'].search([]).filtered('element_detailed'):
            for element in pending_elements:
                elements_tocreate.append({
                    'name': f'{record.name}-{element.name}',
                    'code': f'{record.code}.{element.code}',
                    'element_id': element.id,
                    'parent_id': record.id,
                    'plan_id': record.plan_id.id
                })
        if elements_tocreate:
            self.env['account.analytic.account'].create(elements_tocreate)
        for element in elements_to_delete:
            element.toggle_active()
        return elements_tocreate


class AnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    element_detailed = fields.Boolean(string='Element detailed', default=False)
    element_id = fields.Many2one('expense.element', index=True, ondelete='set null', readonly=False, store=True)
    parent_id = fields.Many2one('account.analytic.account', index=True, ondelete='set null', readonly=False, store=True)

    @api.constrains('parent_id', 'element_id')
    def _constraint_element_code(self):
        # Puedes agregar aquí validaciones adicionales si lo necesitas
        pass

    def _validate_element_detailed(self):
        for record in self:
            if record.element_id and record.element_detailed:
                raise ValidationError('Invalid operation. This analytic account has a related expense element')

    def write(self, vals):
        """Crea automáticamente nuevas cuentas con la combinación cuenta-elemento"""
        write_res = super().write(vals)
        self.env['expense.element']._create_aa_childs()
        return write_res

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        self.env['expense.element']._create_aa_childs()
        return records