from odoo import models, fields, api, _

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'teacher'

    image = fields.Image(string="Photo")
    faculty = fields.Image(string='logo', max_width=100, max_height=100)
    name = fields.Char('Teacher Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    id_t = fields.Char('ID')
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], 'Gender')