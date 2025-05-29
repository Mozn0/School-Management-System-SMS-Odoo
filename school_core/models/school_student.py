from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    student_id = fields.Char(string="Student ID",  default='New', copy=False, readonly=True)

    birth_date = fields.Date(string="Birth Date")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    parent_id = fields.Many2one('school.parent', string="Parent")
    class_id = fields.Many2one('school.class', string="Class")
    academic_year_id = fields.Many2one('school.academic.year', string="Academic Year")
    section_id = fields.Many2one('school.section', string="Section")
    state   = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('recorded','Recorded'),
    ], default='draft')
    

   
    @api.model
    def create(self, vals):
        if vals.get('student_id', 'New') == 'New':
            vals['student_id'] = self.env['ir.sequence'].next_by_code('school.student') or 'New'
        return super(SchoolStudent, self).create(vals) 
    