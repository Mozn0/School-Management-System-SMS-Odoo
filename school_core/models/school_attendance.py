# models/attendance.py
from odoo import models, fields

class SchoolAttendance(models.Model):
    _name = 'school.attendance'
    _description = 'School Attendance'

    attendance_date = fields.Date(string="Date", required=True)
    student_id = fields.Many2one('school.student', string="Student", required=True)
    class_id = fields.Many2one('school.class', string="Class")
    section_id = fields.Many2one('school.section', string="Section")
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ], string="Status", required=True)
