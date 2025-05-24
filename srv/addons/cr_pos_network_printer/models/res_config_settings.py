from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cr_network_printer_ip = fields.Char(
        related='pos_config_id.cr_network_printer_ip', store=True, readonly=False)
    cr_network_printer_port = fields.Char(
        related='pos_config_id.cr_network_printer_port', store=True, readonly=False)
