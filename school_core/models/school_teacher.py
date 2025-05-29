# models/teacher.py
from odoo import models, fields, api

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(required=True)
    employee_id = fields.Char(string="Employee ID", required=True, default='New', copy=False, readonly=True)

    email = fields.Char()
    phone = fields.Char()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender")
    birth_date = fields.Date(string="Date of Birth")
    hire_date = fields.Date(string="Hire Date")
    subject_ids = fields.Many2many('school.subject', string="Subjects")
    
    @api.model
    def create(self, vals):
        if vals.get('employee_id', 'New') == 'New':
            vals['employee_id'] = self.env['ir.sequence'].next_by_code('school.teacher') or 'New'
        return super(SchoolTeacher, self).create(vals)