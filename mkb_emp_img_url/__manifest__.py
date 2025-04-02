# Copyright 2020-23 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Employee Image From URL',
    'version': '16.0',
    'summary': 'This module allows you to import employee images using URL, Import Image, Import Contacts images',
    'description': 'This module allows you to import employee images using URL',
    'category': 'Others',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'LGPL-3',
    "data": [
        'views/hr_employee.xml',
    ],
    'images': ['static/description/banner.png'],
    'depends': ['hr'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
