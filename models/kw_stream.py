# -*- coding: utf-8 -*-

from odoo import api, fields, models


class KwStream(models.Model):
    _name = 'kw_stream'
    _rec_name = 'stream_name'

    stream_name = fields.Char(string="Stream Name")
    stream_semester = fields.One2many(
        'kw_semester', 'semester_stream_id', string="Semester")
    stream_college_id = fields.Many2one('kw_college', string="Stream ID")

    _sql_constraints = [
        ("stream_name_unique", "unique(stream_name)",
         "The stream name should be unique.")
    ]
