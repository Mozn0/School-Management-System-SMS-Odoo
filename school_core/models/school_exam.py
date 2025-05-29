# models/exam.py
from odoo import models, fields

class SchoolExam(models.Model):
    _name = 'school.exam'
    _description = 'School Exam'

    name = fields.Char(string="Exam Name", required=True)
    exam_date = fields.Date(string="Exam Date", required=True)
    academic_year_id = fields.Many2one('school.academic.year', string="Academic Year", required=True)
    class_id = fields.Many2one('school.class', string="Class", required=True)
    section_id = fields.Many2one('school.section', string="Section")
