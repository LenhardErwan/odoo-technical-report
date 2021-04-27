from odoo import api, fields, models


class Block(models.Model):
    _name = 'tr.block'
    _description = 'Block Content'

    image_exist = fields.Boolean(compute='compute_image')

    order = fields.Integer('Order')
    image = fields.Image('Image')
    text = fields.Text('Text')
    report_id = fields.Many2one('tr.report', string='Report ID')

    def compute_image(self):
        for block in self:
            if block.image:
                block.image_exist = True
            else:
                block.image_exist = True
