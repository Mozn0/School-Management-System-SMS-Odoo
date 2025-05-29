from odoo import http
from odoo.http import request


class DashboardController(http.Controller):

    @http.route('/admin/fee-dashboard', type='http', auth='user', website=True)
    def fee_dashboard(self, **kwargs):
        if not request.env.user.has_group('dashboard.group_dashboard_admin'):
            return request.redirect('/web/login')

        academic_year_id = kwargs.get('academic_year_id')
        fee_stats = request.env['school.report'].get_fee_collection_data(academic_year_id)
        years = request.env['school.academic.year'].sudo().search([])

        fee_stats['show_monthly'] = bool(academic_year_id)  # False when "All Academic Years"

        selected_year = None
        if academic_year_id:
            selected_year = request.env['school.academic.year'].sudo().browse(int(academic_year_id))

        return request.render('dashboard.fee_dashboard_page', {
            'fee_stats': fee_stats,
            'academic_years': years,
            'selected_year_id': academic_year_id,
            'selected_year_name': selected_year.name if selected_year else "All Academic Years"
        })

    @http.route('/admin/student-dashboard', type='http', auth='user', website=True)
    def student_dashboard(self, **kwargs):
        if not request.env.user.has_group('dashboard.group_dashboard_admin'):
            return request.redirect('/web/login')

        academic_year_id = kwargs.get('academic_year_id', '')
        student_stats = request.env['school.report'].get_student_statistics(
            academic_year_id if academic_year_id else False
        )
        years = request.env['school.academic.year'].sudo().search([])

        return request.render('dashboard.student_dashboard_page', {
            'student_stats': student_stats,
            'academic_years': years,
            'selected_year_id': academic_year_id,
            'selected_year_name': student_stats['academic_year']
        })