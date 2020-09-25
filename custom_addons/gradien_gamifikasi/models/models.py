# -*- coding: utf-8 -*-

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    rank = fields.Char(string='Rank')
    xp = fields.Integer(string='XP')

