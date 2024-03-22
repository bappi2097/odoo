{
    'name': "Employee Digital Book",
    'version': '16.0.0',
    'summary': "Employee Digital Book",
    'sequence': 0,
    'author': "Bappi Saha",
    'description': """
    Employee Digital Book
    """,
    'category': 'Human Resource',
    'website': '',
    'depends': ['hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/digital_book_category.xml',
        'views/digital_book_type.xml',
        'views/digital_book.xml',
        'views/menu_views.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
