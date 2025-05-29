# models/class_subject.py
from odoo import models, fields

class SchoolClassSubject(models.Model):
    _name = 'school.class.subject'
    _description = 'Class Subject Assignment'
    _rec_name = 'display_name'

    class_id = fields.Many2one('school.class', string="Class", required=True)
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    teacher_id = fields.Many2one('school.teacher', string="Teacher", required=True)

    display_name = fields.Char(compute='_compute_display_name', store=True)

"""     @fields.depends('class_id', 'subject_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.class_id.name or ''} - {rec.subject_id.name or ''}" """
