from odoo import models, fields

class AcademicYear(models.Model):
    _name = 'school.academic.year'
    _description = 'Academic Year'

    name = fields.Char(string="Academic Year", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
