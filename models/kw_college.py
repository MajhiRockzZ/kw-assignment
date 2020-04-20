# -*- coding: utf-8 -*-

from odoo import api, fields, models


class KwCollege(models.Model):
    _name = 'kw_college'
    _rec_name = 'college_name'

    college_name = fields.Char(string="College Name")
    college_stream = fields.One2many(
        'kw_stream', 'stream_college_id', string="Stream")

    _sql_constraints = [
        ("college_name_unique", "unique(college_name)",
         "The college name should be unique.")
    ]
