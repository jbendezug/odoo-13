# -*- coding: utf-8 -*-

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    
    github = fields.Char(string='Github')
    website = fields.Char(string='Website')
    member_id = fields.Char(string='No. Member')
    batch = fields.Char(string='Batch')
    
    status = fields.Selection([
        ('employee', 'Employee'),
        ('student', 'Student'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('mentor', 'Mentor')
        ], string='Status', default='student')
