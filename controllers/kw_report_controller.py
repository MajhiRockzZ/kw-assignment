# -*- coding: utf-8 -*-
from odoo import http


class ReportController(http.Controller):
    @http.route('/report', type='http', auth='public', website=True)
    def render_report_page(self):
        return http.request.render('kw_assignment.report_page', {})

    @http.route('/report/one', type='http', auth='public', website=True)
    def render_report_one_page(self):
        subjects = http.request.env['kw_subject'].sudo().search([])
        return http.request.render('kw_assignment.report_one_page', {
            'subjects': subjects
        })
