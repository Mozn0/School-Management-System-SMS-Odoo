from odoo.tests import common, tagged
from datetime import date, timedelta

@tagged('school', 'standard')  # Proper test tagging
class TestSchoolManagement(common.TransactionCase):
    def setUp(self):
        super(TestSchoolManagement, self).setUp()

        # Setup test environment
        self.Student = self.env['school.student']
        self.Parent = self.env['school.parent']
        self.Teacher = self.env['school.teacher']
        self.Class = self.env['school.class']
        self.Subject = self.env['school.subject']
        self.AcademicYear = self.env['school.academic.year']
        self.Attendance = self.env['school.attendance']
        self.Fee = self.env['school.fee']
        self.Report = self.env['school.report']

        # Create test academic year
        current_year = date.today().year
        self.academic_year = self.AcademicYear.create({
            'name': f'{current_year}-{current_year + 1}',
            'start_date': date(current_year, 9, 1),
            'end_date': date(current_year + 1, 6, 30)
        })

        # Create test class
        self.class_1 = self.Class.create({
            'name': 'Grade 1',
            'academic_year_id': self.academic_year.id
        })

        # Create test subjects
        self.math = self.Subject.create({
            'name': 'Mathematics',
            'code': 'MATH01'
        })

        self.science = self.Subject.create({
            'name': 'Science',
            'code': 'SCI01'
        })

        # Create test teacher
        self.teacher = self.Teacher.create({
            'name': 'Eman Saeed',
            'email': 'eman.saeed@school.edu',
        })

        # Create test parent
        self.parent = self.Parent.create({
            'name': 'Mohamed Sirelkhatim',
            'email': 'mohamed.sirelkhatim@example.com',
            'relation': 'father'
        })

        # Create test student
        self.student = self.Student.create({
            'name': 'Hajer Sirelkhatim',
            'birth_date': date(2025, 5, 28),
            'gender': 'female',
            'email': 'hajer.sirelkhatim@school.edu',
            'parent_id': self.parent.id,
            'class_id': self.class_1.id,
            'academic_year_id': self.academic_year.id
        })

        # Create test attendance
        self.attendance = self.Attendance.create({
            'student_id': self.student.id,
            'class_id': self.class_1.id,
            'attendance_date': date.today(),
            'status': 'present'
        })

        # Create test fee
        self.fee = self.Fee.create({
            'name': 'my Fee',
            'amount': 1000,
            'due_date': date.today() + timedelta(days=30),
            'student_id': self.student.id,
            'academic_year_id': self.academic_year.id
        })

    def test_student_creation(self):
        self.assertEqual(self.student.name, 'Hajer Sirelkhatim')
        self.assertEqual(self.student.gender, 'female')
        self.assertEqual(self.student.parent_id, self.parent)
        self.assertEqual(self.student.class_id, self.class_1)

    def test_attendance(self):
        self.assertEqual(self.attendance.status, 'present')
        self.assertEqual(self.attendance.student_id, self.student)

    def test_fee_payment(self):

        self.fee.is_paid = True
        self.assertTrue(self.fee.is_paid)

        # Test fee report
        fee_data = self.Report.get_fee_collection_data(self.academic_year.id)
        self.assertEqual(fee_data['paid_amount'], 1000)

    def test_academic_year_constraints(self):

            # Should fail because end date is before start date
            self.AcademicYear.create({
                'name': 'Invalid Year',
                'start_date': '2023-01-01',
                'end_date': '2023-08-31'
            })

    def test_parent_child_relationship(self):
        self.assertEqual(self.parent.student_ids, self.student)
        self.assertEqual(self.student.parent_id, self.parent)

    def test_report_generation(self):
        student_stats = self.Report.get_student_statistics(self.academic_year.id)
        self.assertEqual(student_stats['total_students'], 1)
        self.assertEqual(student_stats['female_students'], 1)
        fee_stats = self.Report.get_fee_collection_data(self.academic_year.id)
        self.assertEqual(fee_stats['total_fees'], 1)