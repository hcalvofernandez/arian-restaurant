from odoo import http

class WebsiteRanking(http.Controller):
    @http.route('/ranking', type='http', auth='public', website=True)
    def ranking(self):
        partners = http.request.env['res.partner'].search([])
        return http.request.render('carreras.ranking_template', {'partners': partners})