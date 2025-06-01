from odoo import models, api
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)


class SchoolReport(models.Model):
    _name = 'school.report'
    _description = 'School Reports'

    @api.model
    def get_fee_collection_data(self, academic_year_id=False):
        domain = []
        if academic_year_id:
            domain.append(('academic_year_id', '=', int(academic_year_id)))

        fees = self.env['school.fee'].search(domain)
        paid_fees = fees.filtered(lambda f: f.is_paid)
        unpaid_fees = fees.filtered(lambda f: not f.is_paid)

        # Calculate amounts
        total_amount = sum(fee.amount for fee in fees)
        paid_amount = sum(paid_fees.mapped('amount')) if paid_fees else 0
        unpaid_amount = sum(fee.amount for fee in unpaid_fees)

        # Calculate collection rate
        collection_rate = round((paid_amount / total_amount * 100), 2) if total_amount > 0 else 0.0

        # Monthly collection data
        monthly_data = {}
        for month in range(1, 13):
            month_fees = paid_fees.filtered(
                lambda f: f.due_date and f.due_date.month == month
            )
            monthly_data[datetime(2000, month, 1).strftime('%B')] = sum(fee.amount for fee in month_fees)

        # Yearly collection data
        yearly_data = {}
        if not academic_year_id:
            academic_years = self.env['school.academic.year'].search([])
            for year in academic_years:
                year_fees = paid_fees.filtered(
                    lambda f: f.academic_year_id == year
                )
                yearly_data[year.name] = sum(fee.amount for fee in year_fees)

        return {
            'total_fees': len(fees),
            'paid_fees': len(paid_fees),
            'unpaid_fees': len(unpaid_fees),
            'total_amount': total_amount,
            'paid_amount': paid_amount,
            'unpaid_amount': unpaid_amount,
            'collection_rate': collection_rate,
            'monthly_data': monthly_data if academic_year_id else {},
            'yearly_data': yearly_data,
            'show_monthly': bool(academic_year_id),
            'show_yearly': not bool(academic_year_id),
            'selected_year': academic_year_id
        }

    @api.model
    def get_student_statistics(self, academic_year_id=False):

        domain = []
        year_name = "All Academic Years"

        if academic_year_id:
            year = self.env['school.academic.year'].browse(int(academic_year_id))
            domain.append(('academic_year_id', '=', year.id))
            year_name = year.name
        else:
            year_name = "All Academic Years"

        students = self.env['school.student'].search(domain)

        class_data = {}
        for student in students:
            class_name = student.class_id.name or 'Unassigned'
            class_data[class_name] = class_data.get(class_name, 0) + 1

        return {
            'total_students': len(students),
            'male_students': len(students.filtered(lambda s: s.gender == 'male')),
            'female_students': len(students.filtered(lambda s: s.gender == 'female')),
            'class_distribution': dict(sorted(class_data.items())),
            'academic_year': year_name,
            'selected_year': academic_year_id,
            'has_data': bool(students)
        }
