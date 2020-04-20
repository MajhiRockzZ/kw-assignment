# -*- coding: utf-8 -*-

from odoo import api, fields, models


class KwEmployee(models.Model):
    _inherit = 'hr.employee'

    emp_college_id = fields.Many2one('kw_college', string="College")
    emp_status = fields.Char(string="Status")

    @api.multi
    def employee_approve(self):
        all_employee_data = self.env['hr.employee'].sudo().search([])
        all_employee_data.write({'emp_status': 'Approved'})

    @api.multi
    def employee_reject(self):
        all_employee_data = self.env['hr.employee'].sudo().search([])
        all_employee_data.write({'emp_status': 'Rejected'})

    @api.onchange('emp_college_id')
    def on_change_state(self):
        for record in self:
            pass
