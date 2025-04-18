# models/stock_picking.py
from odoo import models, api, _
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        for move in self.move_ids:
            if move.sale_line_id and move.sale_line_id.order_id.state == 'sale':
                # Sum the 'quantity' (done) from move lines
                done_qty = sum(move.move_line_ids.mapped('quantity'))
                if done_qty > move.product_uom_qty:
                    raise ValidationError(_(
                        "Quantity done (%(done)s) for product %(product)s exceeds sales order demand (%(demand)s)."
                    ) % {
                        'done': done_qty,
                        'product': move.product_id.display_name,
                        'demand': move.product_uom_qty
                    })
        return super().button_validate()