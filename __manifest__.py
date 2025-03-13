{
    'name': 'Test Custom',
    'version': '1.0',
    'summary': 'Test',
    'sequence': 1,
    'description': """
    Testing Module For Odoo 17
    """,
    'category': 'other',
    'website': 'https://www.sgeede.com',
    'depends': [
        'point_of_sale',
        'web',
        'base',
        'web_enterprise',
        'stock_barcode'
    ],
    'license': 'LGPL-3',
    'data': [
        # data
        "data/menu.xml",
        "data/ir_sequence_data.xml",
        
        # security
        "security/ir.model.access.csv",
        "security/test_group.xml",
        
        # views
        "views/pos_config_view.xml",
        "views/sale_order_view.xml",
        
        # wizard
        "wizard/sale_form_wizaard.xml",
        "wizard/invoice_product_wizard.xml",
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'test_custom/static/src/js/pos_test.js',
            'test_custom/static/src/xml/pos_test.xml',
            
            'test_custom/static/src/js/navbar.js',
            'test_custom/static/src/xml/navbar.xml',
            
            # 'test_custom/static/src/js/numpad_invisible.js',
            # 'test_custom/static/src/xml/pos_backspace.xml',
            
            # 'test_custom/static/src/app/components/Numpad.js',
            # 'test_custom/static/src/app/services/pos_service.js',
            # 'test_custom/static/src/app/store/pos_store.js',
            # 'test_custom/static/src/app/registry.js',
            
        ],
        'web.assets_backend': [
            # 'test_custom/static/src/js/sale_order.js',
            # 'test_custom/static/src/xml/sale_order.xml',
        ],
    },
    'qweb': [
        # 'test_custom/static/src/xml/pos_backspace.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
