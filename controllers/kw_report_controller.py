# -*- coding: utf-8 -*-
from odoo import http


class ReportController(http.Controller):
    @http.route('/report', type='http', auth='public', website=True)
    def render_report_page(self):
        return http.request.render('kw_assignment.report_page', {})

    @http.route('/report/one', type='http', auth='public', website=True)
    def render_report_one_page(self):

        # ==== [ SUBJECT WISE AVERAGE MARK ] ====
        subject_wise_avg = dict()
        subject_wise_avg['subject_list'] = []
        main_list = []

        subjects = http.request.env['kw_subject'].sudo().search([])

        for subject in subjects:
            if subject.subject_name not in main_list:
                main_list.append(subject.subject_name)

        for subject in main_list:
            unique_subjects = http.request.env['kw_subject'].sudo().search(
                [('subject_name', '=', subject)])
            subject_number = len(unique_subjects)
            total_marks = 0

            for data in unique_subjects:
                total_marks = total_marks + data.subject_mark

            subject_avg = total_marks / subject_number

            subject_wise_avg['subject_list'].append(
                {'subject': subject, 'average': subject_avg})

        return http.request.render('kw_assignment.report_one_page', subject_wise_avg)

    @http.route('/report/two', type='http', auth='public', website=True)
    def render_report_two_page(self):

        # ==== [ EMPLOYEE NAME AND SUBJECT WISE HIGHEST MARK ] ====
        subjects = http.request.env['kw_subject'].sudo().search([])
        employees = http.request.env['hr.employee'].sudo().search([])

        unique_subject_list = []

        subject_max_mark = {}
        subject_max_mark['subject_list'] = []

        for subject in subjects:
            if subject.subject_name not in unique_subject_list:
                unique_subject_list.append(subject.subject_name)

        for subject_name in unique_subject_list:
            subject_data = http.request.env['kw_subject'].sudo().search(
                [('subject_name', '=', subject_name)])

            max_mark = 0
            employee_college_id = None
            employee_name = None

            for data in subject_data:
                if data.subject_mark > max_mark:
                    max_mark = data.subject_mark
                    employee_college_id = data.subject_semester_id.semester_stream_id.stream_college_id.id

            for employee in employees:
                if employee_college_id == employee.emp_college_id.id:
                    employee_name = employee.name

            subject_max_mark['subject_list'].append({
                'employee_name': employee_name,
                'subject_name': subject_name,
                'max_mark': max_mark
            })

        return http.request.render('kw_assignment.report_two_page', subject_max_mark)
