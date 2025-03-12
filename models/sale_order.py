from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default='New')
    is_action_clear_hide = fields.Boolean(string="Is clear line button hidden", default=True, compute="_compute_hide_clear_line_button")
    
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
            vals['name'] = self.env['ir.sequence'].next_by_code('custom.sale.order') or 'New'
        return super(SaleOrder, self).create(vals)
    
    def action_clear_line(self):
        raw_query = """
            DELETE FROM sale_order_line
            WHERE order_id = %s
        """
        self.env.cr.execute(raw_query, (self.id,))
        
    @api.depends('order_line')
    def _compute_hide_clear_line_button(self):
        for record in self:
            if record.order_line:
                record.is_action_clear_hide = False
            if not record.order_line:
                record.is_action_clear_hide = True