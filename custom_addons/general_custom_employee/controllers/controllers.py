# -*- coding: utf-8 -*-
# from odoo import http


# class GeneralCustomEmployee(http.Controller):
#     @http.route('/general_custom_employee/general_custom_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/general_custom_employee/general_custom_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('general_custom_employee.listing', {
#             'root': '/general_custom_employee/general_custom_employee',
#             'objects': http.request.env['general_custom_employee.general_custom_employee'].search([]),
#         })

#     @http.route('/general_custom_employee/general_custom_employee/objects/<model("general_custom_employee.general_custom_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('general_custom_employee.object', {
#             'object': obj
#         })
