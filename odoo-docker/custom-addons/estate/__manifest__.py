{
    'name': "Estate",
    'version': "1.0",
    'depends': ['base', 'web'],
    'author': "Bappi Saha",
    'category': "Real Estate/Brokerage",
    'sequence': 0,
    'description': """
        Lorem ipsum sit amet
    """,
    'data': [
        "security/ir.model.access.csv",
        "views/estate_property_offer_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        # "views/res_users_views.xml",
        "views/estate_menus.xml",
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'application': True
}