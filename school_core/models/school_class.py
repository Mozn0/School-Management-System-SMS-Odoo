from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class'

    name = fields.Char(string="Class Name", required=True)
    academic_year_id = fields.Many2one('school.academic.year', string="Academic Year")
