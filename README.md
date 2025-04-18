This module adds an onchange validation to the 'Done' quantity field
        (qty_done) on stock move lines within a picking. If a user attempts
        to enter a quantity greater than the initial demand (product_uom_qty
        from the related stock move), a UserError is raised immediately,
        preventing the invalid input for version 18 odoo
