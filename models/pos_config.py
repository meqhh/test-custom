from odoo import models, fields, api

class PosConfig(models.Model):
    _inherit = 'pos.config'
    
    is_numpad_visible = fields.Boolean(string="Show Backspace Button", help='Text to print at the top of the receipt')