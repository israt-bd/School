from odoo import models , fields, api , _

class Student(models.Model):
    _name = 'school.student'
    _description = 'student'

    image = fields.Image(string="Profile Picture")
    _logo = fields.Image(string="Logo")
    name = fields.Char('Stuent Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    birth_date = fields.Date('Date of Birth')
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], 'Gender')