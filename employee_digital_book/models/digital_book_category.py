from odoo import api, fields, models


class Category(models.Model):
    _name = 'digital.book.category'
    _description = 'File Category'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Category Name", tracking=True, required=True)