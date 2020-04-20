# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class KwReportFour(models.Model):
    _name = 'kw_report_four'
    _auto = False

    subject_name = fields.Char(string="Subject Name")
    average_marks = fields.Integer(string="Average Marks")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'kw_report_four')
        self._cr.execute("""
        CREATE VIEW kw_report_four AS (
            SELECT 
                SUBJECT.id AS id,
                SUBJECT.subject_name AS subject_name,
                AVG(SUBJECT.subject_mark) AS average_marks
            FROM 
                kw_stream AS STREAM,
                kw_semester AS SEMESTER,
                kw_subject AS SUBJECT
            WHERE 
                STREAM.id = SEMESTER.semester_stream_id
                AND SEMESTER.id = SUBJECT.subject_semester_id
                GROUP BY(SUBJECT.id)
        )
        """)
