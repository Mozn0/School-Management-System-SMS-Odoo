from odoo import models, fields

class SchoolParent(models.Model):
    _name = 'school.parent'
    _description = 'Parent'

    name = fields.Char(string="Full Name", required=True)
    relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian'),
    ], string="Relation to Student", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")
    student_ids = fields.One2many('school.student', 'parent_id', string="Children")
