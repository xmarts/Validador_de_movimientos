# -*- coding: utf-8 -*-
from odoo import http

# class BloqueoMercancia(http.Controller):
#     @http.route('/bloqueo_mercancia/bloqueo_mercancia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bloqueo_mercancia/bloqueo_mercancia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bloqueo_mercancia.listing', {
#             'root': '/bloqueo_mercancia/bloqueo_mercancia',
#             'objects': http.request.env['bloqueo_mercancia.bloqueo_mercancia'].search([]),
#         })

#     @http.route('/bloqueo_mercancia/bloqueo_mercancia/objects/<model("bloqueo_mercancia.bloqueo_mercancia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bloqueo_mercancia.object', {
#             'object': obj
#         })