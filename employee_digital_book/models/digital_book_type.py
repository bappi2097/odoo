from odoo import api, fields, models


class FileType(models.Model):
    _name = 'digital.book.type'
    _description = 'File Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Type", tracking=True, required=True)
    extension = fields.Char(string="Extension", tracking=True, required=True)
