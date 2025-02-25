from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default='New')
    
    def action_update_form(self):
        view_id = self.env.ref('test_custom.sale_form_wizard').id
        return {
            'name': 'Update SO',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.form.wizard',
            'view_id': view_id,
            'target': 'new',
            'context': {
                # 'payment_term_id': self.payment_term_id,
                # 'state': self.state,
            },
        }
        # print(self.id)
        
    def action_import_so(self):
        view_id = self.env.ref('test_custom.invoice_product_wizard_form').id
        return {
            'name': 'Import Product Data',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'invoice.product.wizard',
            'view_id': view_id,
            'target': 'new',
            'context': {
                    'default_sale_order_id': self.id
                },
        }
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            print(12121212121212121212)
            vals['name'] = self.env['ir.sequence'].next_by_code('custom.sale.order') or 'New'
        return super(SaleOrder, self).create(vals)