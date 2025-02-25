from odoo import fields, models, api, _

class InvoiceProductWizard(models.TransientModel):
    _name = 'invoice.product.wizard'
    
    category = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service'),
        ('product', 'Storeable Product'),
        ('combo', 'Combo')
    ], string='Product Category', default="consu")
    invoice_ids = fields.One2many('invoice.product.wizard.line', 'invoice_id', String="Invoice")
    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    
    def action_import(self):
        for rec in self:
            for line in rec.invoice_ids:
                self.env['sale.order.line'].create({
                    'order_id': rec.sale_order_id.id,
                    'product_id': line.product_id.product_variant_id.id,
                    'product_template_id': line.product_id.id,
                    'name': line.product_id.name,
                    'product_uom_qty': 1.0,
                    'product_uom': line.product_id.uom_id.id,
                    'price_unit': line.product_id.list_price,
                })


class InvoiceProductWizardLine(models.TransientModel):
    _name = 'invoice.product.wizard.line'
    
    sale_id = fields.Many2one('sale.order.line', string='Sale Order')
    invoice_id = fields.Many2one('invoice.product.wizard', string='Invoice')
    product_id = fields.Many2one('product.template', string='Product')