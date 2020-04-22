{
    'name': 'Assignment',
    'version': '12.0.1.0.0',
    'summary': 'Module for employee wise subject wise mark database app',
    'category': 'Extra Tools',
    'sequence': '0',
    'license': 'AGPL-3',
    'author': 'Sumesh Majhi',
    'website': 'https://www.majhirockzz.me',
    'depends': [
        'hr',
    ],
    'data': [
        'security/employee_group.xml',
        'security/ir.model.access.csv',
        'views/includes/kw_college.xml',
        'views/includes/kw_stream.xml',
        'views/includes/kw_semester.xml',
        'views/includes/kw_subject.xml',
        'views/includes/kw_employee.xml',
        'views/includes/kw_report_one.xml',
        'views/includes/kw_report_two.xml',
        'views/includes/kw_report_three.xml',
        'views/includes/kw_report_four.xml',
        'views/website/report_webpage.xml',
        'views/kw_action.xml',
        'views/kw_menuitem.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
