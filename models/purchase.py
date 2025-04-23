from odoo import models, fields, api
import pprint
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def purchase_inspect(self):
        purchase = self.env['purchase.order'].browse(self.id)
        pprint.pprint(self.read())