from odoo import api, fields, models


class Report(models.Model):
    _name = 'tr.report'
    _description = 'Report'

    name = fields.Char('Title', required=True)
    date_published = fields.Date('Published Date')
    globalreport_id = fields.One2many('tr.globalreport', 'report_ids')
    block_ids = fields.One2many('tr.block', string='Content')
