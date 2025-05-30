# models/exam_result.py
from odoo import models, fields, api

class SchoolExamResult(models.Model):
    _name = 'school.exam.result'
    _description = 'Exam Result'

    exam_id = fields.Many2one('school.exam', string="Exam", required=True)
    student_id = fields.Many2one('school.student', string="Student", required=True)
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    marks_obtained = fields.Float(string="Marks Obtained")
    grade = fields.Char(string="Grade", compute="_compute_grade", store=True)
    report_id = fields.Many2one('school.exam.report', string="Exam Report")


    @api.depends('marks_obtained')
    def _compute_grade(self):
        for rec in self:
            if rec.marks_obtained >= 90:
                rec.grade = 'A'
            elif rec.marks_obtained >= 80:
                rec.grade = 'B'
            elif rec.marks_obtained >= 70:
                rec.grade = 'C'
            elif rec.marks_obtained >= 60:
                rec.grade = 'D'
            else:
                rec.grade = 'F'
