# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'AI Book Similarity',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Example module using Odoo 19 Vector fields',
    'depends': ['ai'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
