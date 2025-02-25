from odoo import fields, models, api, _

class TestModel(models.Model):
    _name = 'test.model'
    
    name = fields.Char(string='Name')
    test_line_id = fields.One2many('test.model.line')
    
class TestModelLine(models.Model):
    _name = 'test.model.line'
    
    
    product_id = fields.Many2one('product.product', string="Product")