# models/stock_move_line.py
from odoo import models, api, _

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.onchange('quantity')  # Use 'quantity' instead of 'qty_done'
    def _onchange_quantity_check_demand(self):
        for line in self:
            move = line.move_id
            if move.sale_line_id and move.sale_line_id.order_id.state == 'sale':
                other_lines_done = sum(move.move_line_ids.filtered(lambda l: l != line).mapped('quantity'))
                remaining = move.product_uom_qty - other_lines_done
                if line.quantity > remaining:
                    line.quantity = remaining
                    return {
                        'warning': {
                            'title': _('Quantity Adjusted'),
                            'message': _('Cannot exceed remaining demand of %(remaining)s %(uom)s.') % {
                                'remaining': remaining,
                                'uom': move.product_uom.name
                            }
                        }
                    }