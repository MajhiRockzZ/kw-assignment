# -*- coding: utf-8 -*-

from odoo import api, fields, models


class KwSemester(models.Model):
    _name = 'kw_semester'
    _rec_name = 'semester_name'

    semester_name = fields.Char(string="Semester Name")
    semester_subject = fields.One2many(
        'kw_subject', 'subject_semester_id', string="Subject")
    semester_stream_id = fields.Many2one('kw_stream', string="Semester ID")
