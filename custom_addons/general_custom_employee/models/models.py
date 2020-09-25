# -*- coding: utf-8 -*-

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    

    ages = fields.Integer(string='Ages')
    tall = fields.Integer(string='Tall')
    whatsapp = fields.Char(string='Whatsapp')
    twitter = fields.Char(string='Twitter')
    telegram = fields.Char(string='Telegram')
    facebook = fields.Char(string='Facebook')
    instagram = fields.Char(string='Instagram')
    linked = fields.Char(string='Linked')
    medium = fields.Char(string='Medium')
    about = fields.Text(string='About')
    disease = fields.Text(string='Disease')
    allergy = fields.Text(string='Allergy')
    bpjs_kesehatan = fields.Char(string='BPJS Kesehatan')
    bpjs_kk = fields.Char(string='BPJS Ketenagakerjaan')
    
    blood = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'o-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-')
        ], string='Blood', default='a+')
    
    religion = fields.Selection([
        ('islam', 'Islam'),
        ('hindu', 'Hindu'),
        ('budha', 'Budha'),
        ('kristen', 'Kristen'),
        ('khong hu chu', 'Khong Hu Chu')
        ], string='Religion', default='islam')
    
    hobby_ids = fields.Many2many('type.hobby', 'type_hobby_pivot', 'emp_id', 'hobby_id', string='Hobby')

class HrEmployeeHobby(models.Model):
    _name = 'type.hobby'
    _description = 'Jenis Jenis Hobby'
    
    
    name = fields.Char(string='Name of Hobby')
        