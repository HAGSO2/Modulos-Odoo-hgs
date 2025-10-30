# -*- coding: utf-8 -*-
# from odoo import http


# class Skeleton(http.Controller):
#     @http.route('/skeleton/skeleton', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/skeleton/skeleton/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('skeleton.listing', {
#             'root': '/skeleton/skeleton',
#             'objects': http.request.env['skeleton.skeleton'].search([]),
#         })

#     @http.route('/skeleton/skeleton/objects/<model("skeleton.skeleton"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('skeleton.object', {
#             'object': obj
#         })

