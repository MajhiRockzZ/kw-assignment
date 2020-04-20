# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class KwSubject(models.Model):
    _name = 'kw_subject'
    _rec_name = 'subject_name'

    subject_name = fields.Char(string="Subject Name")
    subject_mark = fields.Integer(string="Marks Obtained")
    subject_semester_id = fields.Many2one('kw_semester', string="Subject ID")

    _sql_constraints = [
        ("subject_name_unique", "unique(subject_name)",
         "The subject name should be unique.")
    ]

    @api.constrains('subject_mark')
    def validate_subject_mark(self):
        for record in self:
            if record.subject_mark > 100:
                raise ValidationError("Marks should be between 0 to 100")
