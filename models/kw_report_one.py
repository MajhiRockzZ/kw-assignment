# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class KwReportOne(models.Model):
    _name = 'kw_report_one'
    _auto = False

    employee_name = fields.Char(string="Employee Name")
    employee_subject = fields.Char(string="Employee Subject")
    employee_marks = fields.Char(string="Employee Marks")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'kw_report_one')
        self._cr.execute("""
        CREATE VIEW kw_report_one AS (
        SELECT 
            SUBJECT.id AS id,
            SUBJECT.subject_name AS employee_subject,
            EMPLOYEE.name AS employee_name,
            SUBJECT.subject_mark AS employee_marks
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
        )
        """)
