from odoo import api, fields, models


class GlobalReport(models.Model):
    _name = 'tr.globalreport'
    _description = 'Global Report'

    name = fields.Char('Title', required=True)
    report_ids = fields.One2many('tr.report', string='Report')
    command_id = fields.Many2one('account.invoice')
