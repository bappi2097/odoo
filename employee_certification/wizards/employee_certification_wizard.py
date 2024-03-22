import xlwt, base64, io
from odoo import fields, models, _


# temporary model
class ExcelReportOut(models.TransientModel):
    _name = 'excel.report.out'
    _description = 'Excel report'

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=150)


class EmployeeCertificationWizard(models.TransientModel):
    _name = 'employee.certification.wizard'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=False)
    preview = fields.Html('Report Preview')

    def action_preview(self):
        table, thead, th, tr, td = self.get_table_structure()
        body = ''
        column_header = [_('Employee'), _('Certification'), _('Institute'), _('Start date'),
                         _('End Date'), _('Status')]
        head = thead.format(th="".join(map(th.format, column_header)))
        data_set = self.generate_data_all()
        if data_set:
            for data in data_set:
                body += tr.format("".join(map(td.format, data.values())))
                view_result = table.format(thead=head, tbody=body)
                self.write({'preview': view_result})
            return True
        else:
            self.write({'preview': '<h3 style="text-align:center;">No data found !!!</h3>'})

    def action_export(self):
        """ Generate sales info report in Excel format """
        row = 0
        # Generate File name format
        filename = 'employee_certification_report' + '.xls'
        workbook = xlwt.Workbook(encoding="UTF-8")
        worksheet = workbook.add_sheet('Employee Certification')
        first_col = worksheet.col(0)
        first_col.width = 256 * 20
        snd_col = worksheet.col(1)
        snd_col.width = 256 * 50
        trd_col = worksheet.col(2)
        trd_col.width = 256 * 20
        frd_col = worksheet.col(3)
        frd_col.width = 256 * 20
        fifth_col = worksheet.col(4)
        fifth_col.width = 256 * 20
        sixth_col = worksheet.col(5)
        sixth_col.width = 256 * 20
        data_set = self.generate_data_all()
        self._write_sheet(worksheet, data_set)
        fp = io.BytesIO()
        workbook.save(fp)
        export_id = self.env['excel.report.out'].create(
            {'excel_file': base64.b64encode(fp.getvalue()), 'file_name': filename})
        fp.close()

        return {
            'name': '',
            'view_mode': 'form',
            'res_id': export_id.id,
            'res_model': 'excel.report.out',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def _write_sheet(self, worksheet, data_set):
        # Column Style
        header_style = xlwt.easyxf('pattern: pattern solid, fore_colour dark_purple;'
                                   'font: color white, bold True;'
                                   'alignment: horizontal center, vertical center;')
        row = 0
        mer_row = row + 1
        col = 0
        worksheet.write_merge(row, mer_row, col, col, 'Employee', header_style)
        col = 1
        worksheet.write_merge(row, mer_row, col, col, 'Certification', header_style)
        col = 2
        worksheet.write_merge(row, mer_row, col, col, 'Institute', header_style)
        col = 3
        worksheet.write_merge(row, mer_row, col, col, 'Start date', header_style)
        col = 4
        worksheet.write_merge(row, mer_row, col, col, 'End Date', header_style)
        col = 5
        worksheet.write_merge(row, mer_row, col, col, 'Status', header_style)
        row = 2
        for data in data_set:
            col = 0
            worksheet.write(row, col, data['employee'])
            col = 1
            worksheet.write(row, col, data['certification'])
            col = 2
            worksheet.write(row, col, data['institute'])
            col = 3
            worksheet.write(row, col, data['start_date'].strftime('%d %b %Y'))
            col = 4
            worksheet.write(row, col, data['end_date'].strftime('%d %b %Y'))
            col = 5
            worksheet.write(row, col, data['certificate_status'])
            row += 1
        return

    def generate_data_all(self):
        list_of_all_records = []
        where_con = []
        condition_str = ""
        if self.employee_id:
            # Where condition for ORM search
            where_con.append(('employee_id', '=', self.employee_id.id))
            # Where condition for SQL
            condition_str = "WHERE ec.employee_id = {}".format(self.employee_id.id)
        # with ORM
        # certification_objs = self.env['employee.certification'].search(where_con)
        # for certification_obj in certification_objs:
        #     row_val = {
        #         'employee': certification_obj.employee_id.name,
        #         'certification': certification_obj.certification_id.name,
        #         'institute': certification_obj.institute.name,
        #         'start_date': certification_obj.start_date,
        #         'end_date': certification_obj.end_date,
        #         'certificate_status': certification_obj.certificate_status,
        #     }
        #     list_of_all_records.append(row_val)
        # with SQL
        sql = """
            SELECT he.name as employee, cer.name as certification, ins.name as institute,
            start_date, end_date, certificate_status
            FROM employee_certification as ec
            LEFT JOIN hr_employee as he on ec.employee_id = he.id
            LEFT JOIN employee_certificate as cer on ec.certification_id = cer.id
            LEFT JOIN certificate_issued_by as ins on ec.institute = ins.id
            %s
        """ % (str(condition_str))
        self.env.cr.execute(sql)
        list_of_all_records = self.env.cr.dictfetchall()
        return list_of_all_records

    def get_table_structure(self):
        table = """
                    <table border="1" class="o_list_view table-bordered o_list_view_ungrouped">
                      <thead>
                    {thead}
                      </thead>
                      <tbody>
                    {tbody}
                      </tbody>
                    </table>
                """
        thead = """
                    <tr style="text-align: center;font-weight:bold ">
                    {th}
                    </tr>
                """
        th = """<th style='border: 1px solid #C0C0C0;position: sticky;top: 0;background: #ddd;padding: 3px;'>{}</th>\n"""
        td = """<td style='padding: 5px;'>{}</td>\n"""
        tr = """<tr>{}</tr>\n"""
        return table, thead, th, tr, td