# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class KwReportTwo(models.Model):
    _name = 'kw_report_two'
    _auto = False

    college_name = fields.Char(string="College Name")
    student_count = fields.Integer(string="Student Count")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'kw_report_two')
        self._cr.execute("""
        CREATE VIEW kw_report_two AS (
            SELECT 
                COLLEGE.id AS id,
                COLLEGE.college_name AS college_name,
                COUNT(EMPLOYEE.name) AS student_count
            FROM 
                hr_employee AS EMPLOYEE,
                kw_college AS COLLEGE
            WHERE EMPLOYEE.emp_college_id = COLLEGE.id
            GROUP BY(COLLEGE.id)
        )
        """)
