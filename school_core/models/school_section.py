# school_core/models/section.py
from odoo import models, fields

class SchoolSection(models.Model):
    _name = 'school.section'
    _description = 'Class Section'

    name = fields.Char(string="Section Name", required=True)
    class_id = fields.Many2one('school.class', string="Class", required=True)
    student_ids = fields.One2many('school.student', 'section_id', string="Students")
