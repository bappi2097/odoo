from datetime import datetime
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class HREmployeeJobRank(models.Model):
    _name = 'employee.job_rank'
    name = fields.Char(string='Job Rank', size=100, required=True)

class HREmployeeInherited(models.Model):
    _inherit = 'hr.employee'
    project_history_ids = fields.One2many(comodel_name="employee.project_history", inverse_name="employee_id",
                                        string="Project History")
    job_rank_id = fields.Many2one(comodel_name="employee.job_rank", inverse_name="employee_id", string="Job Rank")


class HREmployeeProjectHistory(models.Model):
    _name = "employee.project_history"
    name = fields.Char(string="Project Name", required=True)
    no_of_members = fields.Integer(string="Members", required=True, default=1)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=False)
    start_date = fields.Date(string="Start date", required=True )
    end_date = fields.Date(string="End date", required=True )
    duration = fields.Char(string="Project duration", compute='calculate_project_duration')
    status = fields.Selection(string="Status",
                                selection=[('completed', 'Completed'),
                                            ('in_progress', 'In Progress')
                                            ], default='completed', required=True, )
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id.id)

    @api.depends('start_date', 'end_date')
    def calculate_project_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = record.end_date - record.start_date
                record.duration = str(delta.days) + " days"
            else:
                record.duration = ""