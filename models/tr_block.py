from odoo import api, fields, models


class Block(models.Model):
    _name = 'tr.block'
    _description = 'Block Content'

    order = fields.Integer('Order')
    image = fields.Image('Image')
    text = fields.Text('Text')
