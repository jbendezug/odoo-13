# -*- coding: utf-8 -*-
# from odoo import http


# class GradienEmployee(http.Controller):
#     @http.route('/gradien_employee/gradien_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gradien_employee/gradien_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gradien_employee.listing', {
#             'root': '/gradien_employee/gradien_employee',
#             'objects': http.request.env['gradien_employee.gradien_employee'].search([]),
#         })

#     @http.route('/gradien_employee/gradien_employee/objects/<model("gradien_employee.gradien_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gradien_employee.object', {
#             'object': obj
#         })
