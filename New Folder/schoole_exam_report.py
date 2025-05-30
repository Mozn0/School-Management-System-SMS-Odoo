from odoo import models, fields, api

class SchoolExamReport(models.Model):
    _name = 'school.exam.report'
    _description = 'Exam Report'

    student_id = fields.Many2one('school.student', string="Student", required=True)
    exam_id = fields.Many2one('school.exam', string="Exam", required=True)
    result_ids = fields.One2many('school.exam.result', 'report_id', string="Results")
    average_score = fields.Float(string="Average Score", compute="_compute_average", store=True)

    @api.depends('result_ids.marks_obtained')
    def _compute_average(self):
        for rec in self:
            marks = rec.result_ids.mapped('marks_obtained')
            rec.average_score = sum(marks) / len(marks) if marks else 0.0

   
    def print_report(self):
        return self.env.ref('action_report_exam_report_pdf').report_action(self)
