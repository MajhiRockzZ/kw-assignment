# -*- coding: utf-8 -*-

from odoo import api, fields, models
from lxml import etree


class KwEmployee(models.Model):
    _inherit = 'hr.employee'

    emp_college_id = fields.Many2one(
        'kw_college', string="College", required=True)
    emp_stream_id = fields.Many2one(
        'kw_stream', string='Stream', required=True)
    emp_semester_id = fields.Many2one(
        'kw_semester', string='Semester', required=True)
    emp_subject_id = fields.Many2one(
        'kw_subject', string='Subject', required=True)

    emp_status = fields.Char(string="Status")

    @api.multi
    def employee_approve(self):
        all_employee_data = self.env['hr.employee'].sudo().search([])
        all_employee_data.write({'emp_status': 'Approved'})

    @api.multi
    def employee_reject(self):
        all_employee_data = self.env['hr.employee'].sudo().search([])
        all_employee_data.write({'emp_status': 'Rejected'})

    # TODO: add field_view_get method

    # TODO: add name_get method

    # TODO: add onchange method for employee college details
    @api.onchange('emp_college_id')
    def _onchange_emp_college_id(self):
        self.emp_stream_id = False
        if self.emp_college_id:
            return {'domain': {'emp_stream_id': [('stream_college_id', '=', self.emp_college_id.id)], }}

    @api.onchange('emp_stream_id')
    def _onchange_emp_stream_id(self):
        self.emp_semester_id = False
        if self.emp_stream_id:
            return {'domain': {'emp_semester_id': [('semester_stream_id', '=', self.emp_stream_id.id)], }}
