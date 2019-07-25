# -*- coding: utf-8 -*-
{
    'name': "validador_de_movimientos",

    'summary': """
        No se recibara más mercancía de la solicitada para que en inventario no tenga más
        mercancía de lo demandado que se envíe una alerta cuando la mercancía sea mayor a lo demandado """,

    'description': """
        No recibir mercancia mayor a lo demandado
    """,

    'author': "XMARTS",
    'email': 'desarrollo@xmarts.com',
    'website': "https://xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,
}