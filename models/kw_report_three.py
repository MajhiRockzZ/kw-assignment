# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class KwReportThree(models.Model):
    _name = 'kw_report_three'
    _auto = False

    student_count_max = fields.Integer(string="Student Count Max")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'kw_report_three')
        self._cr.execute("""
        CREATE VIEW kw_report_three AS (
            SELECT
                COUNT(EMPLOYEE.name) AS id,
                COUNT(EMPLOYEE.name) AS student_count_max
            FROM 
                hr_employee AS EMPLOYEE,
                kw_college AS COLLEGE,
                kw_stream AS STREAM,
                kw_semester AS SEMESTER,
                kw_subject AS SUBJECT
            WHERE 
                EMPLOYEE.emp_college_id = COLLEGE.id
                AND COLLEGE.id = STREAM.stream_college_id
                AND STREAM.id = SEMESTER.semester_stream_id
                AND SEMESTER.id = SUBJECT.subject_semester_id
                AND SUBJECT.subject_mark >= 90
        )
        """)
