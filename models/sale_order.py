from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_update_form(self):
        view_id = self.env.ref('test_custom.sale_form_wizard').id
        return {
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
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'invoice.product.wizard',
            'view_id': view_id,
            'target': 'new',
            'context': {

                },
        }