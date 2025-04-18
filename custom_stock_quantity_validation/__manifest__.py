{
    'name': 'Stock Picking Quantity Validation',
    'version': '18.0.1.0.0',
    'summary': """
        Prevents setting 'Done' quantity greater than 'Demand'
        on stock picking lines (Operations tab).
    """,
    'description': """
        This module adds an onchange validation to the 'Done' quantity field
        (qty_done) on stock move lines within a picking. If a user attempts
        to enter a quantity greater than the initial demand (product_uom_qty
        from the related stock move), a UserError is raised immediately,
        preventing the invalid input.
    """,
    'author': 'Your Name / Company Name',
    'website': 'Your Website',
    'category': 'Inventory/Inventory',
    'depends': [
        'sale',
        'stock',
        'sale_stock',# Depends on the stock module for stock.move.line
    ],
    'data': [
        # No XML views are needed for this Python-only logic
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3', # Or your preferred license
}