# -*- coding: utf-8 -*-
# from odoo import http


# class Pointeuse(http.Controller):
#     @http.route('/pointeuse/pointeuse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pointeuse/pointeuse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pointeuse.listing', {
#             'root': '/pointeuse/pointeuse',
#             'objects': http.request.env['pointeuse.pointeuse'].search([]),
#         })

#     @http.route('/pointeuse/pointeuse/objects/<model("pointeuse.pointeuse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pointeuse.object', {
#             'object': obj
#         })
