# -*- coding: utf-8 -*-
# from odoo import http


# class GradienGamifikasi(http.Controller):
#     @http.route('/gradien_gamifikasi/gradien_gamifikasi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gradien_gamifikasi/gradien_gamifikasi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gradien_gamifikasi.listing', {
#             'root': '/gradien_gamifikasi/gradien_gamifikasi',
#             'objects': http.request.env['gradien_gamifikasi.gradien_gamifikasi'].search([]),
#         })

#     @http.route('/gradien_gamifikasi/gradien_gamifikasi/objects/<model("gradien_gamifikasi.gradien_gamifikasi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gradien_gamifikasi.object', {
#             'object': obj
#         })
