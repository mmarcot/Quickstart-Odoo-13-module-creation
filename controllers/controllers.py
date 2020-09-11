# -*- coding: utf-8 -*-
# from odoo import http


# class SimpleEvent(http.Controller):
#     @http.route('/simple_event/simple_event/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simple_event/simple_event/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simple_event.listing', {
#             'root': '/simple_event/simple_event',
#             'objects': http.request.env['simple_event.simple_event'].search([]),
#         })

#     @http.route('/simple_event/simple_event/objects/<model("simple_event.simple_event"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simple_event.object', {
#             'object': obj
#         })
