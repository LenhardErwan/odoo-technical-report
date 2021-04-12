from odoo import api, fields, models


class Report(models.Model):
    _name = 'tr.report'
    _description = 'Report'

    name = fields.Char('Title', required=True)
    date_published = fields.Date('Published Date')
    block_ids = fields.One2many('tr.block', 'report_id', string='Content')
    globalreport_id = fields.Many2one(
        'tr.globalreport', string='Global Report ID')
