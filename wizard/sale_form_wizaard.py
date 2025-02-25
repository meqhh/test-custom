from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleFormWizard(models.TransientModel):
    _name = 'sale.form.wizard'
    
    payment_term_id = fields.Many2one('account.payment.term', string="Payment Term")
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('cancel', 'Cancel')
    ], string="State Update", default=False)
    
    @api.model
    def default_get(self, fields_list):
        res = super(SaleFormWizard, self).default_get(fields_list)
        active_id =  self.env.context.get('active_ids')
        if active_id:
            sale_order = self.env['sale.order'].browse(active_id)
            res.update({
                'payment_term_id': sale_order.payment_term_id.id,
                'state': sale_order.state
            })
        return res
    
    @api.constrains('payment_term_id', 'state')
    def check_user_group(self):
        if self.payment_term_id or self.state  or self.payment_term_id and self.state:
            if not self.env.user.has_group('test_custom.edit_so_wizard'):
                raise  UserError("You don't have access to use this wizard")
            
    def action_update_sale(self):
        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))
        self.check_user_group()
        if sale_order:
            for record in sale_order:
                value = {}
                if self.payment_term_id:
                    value['payment_term_id'] = self.payment_term_id.id
                if self.state:
                    value['state'] = self.state
                if value:
                    print(value)
                    record.ensure_one()
                    record.write(value)