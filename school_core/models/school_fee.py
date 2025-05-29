# models/fee.py
from odoo import models, fields

class SchoolFee(models.Model):
    _name = 'school.fee'
    _description = 'School Fee'

    name = fields.Char(string="Fee Title", required=True)
    amount = fields.Float(string="Amount", required=True)
    due_date = fields.Date(string="Due Date", required=True)
    student_id = fields.Many2one('school.student', string="Student", required=True)
    academic_year_id = fields.Many2one('school.academic.year', string="Academic Year", required=True)
    is_paid = fields.Boolean(string="Paid", default=False)
