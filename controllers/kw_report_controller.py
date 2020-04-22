# -*- coding: utf-8 -*-
from odoo import http


class ReportController(http.Controller):
    @http.route('/report', type='http', auth='public', website=True)
    def render_report_page(self):
        return http.request.render('kw_assignment.report_page', {})
