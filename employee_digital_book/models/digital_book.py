from odoo import api, fields, models
from odoo.exceptions import ValidationError


class DigitalBook(models.Model):
    _name = 'digital.book'
    _description = 'Digital Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_id'

    name = fields.Char(string="Title", required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    category_id = fields.Many2one('digital.book.category', string='Category', required=True, tracking=True)
    type_id = fields.Many2one('digital.book.type', string='Type', required=True, tracking=True)
    attachment_data = fields.Binary(string='File Data', required=True)
    attachment_name = fields.Char(string='File Name', required=True)

    @api.onchange('attachment_data')
    def _onchange_attachment_data(self):
        if self.type_id and self.attachment_data:
            allowed_extensions = [ext.lower() for ext in self.type_id.extension.split(",")]
            file_extension = self.attachment_name.split('.')[-1].lower()
            if file_extension not in allowed_extensions:
                self.attachment_data = False
                raise ValidationError(
                    f"Invalid file type for '{self.attachment_name}'. Allowed types: {', '.join(allowed_extensions)}")

    def create_attachment(self, vals):
        attachment_vals = {
            'name': vals.get('attachment_name', 'Untitled'),
            'datas': vals.get('attachment_data'),
            'res_model': 'digital.book',
            'res_id': self.id,
        }
        attachment = self.env['ir.attachment'].create(attachment_vals)
        return attachment


class HREmployeeInherited(models.Model):
    _inherit = 'hr.employee'

    digital_book_ids = fields.One2many(comodel_name="digital.book", inverse_name="employee_id",
                                        string="Documents")