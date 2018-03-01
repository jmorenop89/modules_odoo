from odoo import models, fields, api

class AcademicCareer(models.Model):
    _name = 'academic.career'

    x_name = fields.Char(string = 'Name')
    x_code = fields.Char(string  = 'Code')

class AcademicStudent(models.Model):
    _name = 'academic.student'

    x_registry_number = fields.Char(string = 'Registry Number')
    x_name = fields.Char(string = 'Name')
    x_birthdate = fields.Date(string  = 'Birthdate')
    x_address = fields.Char(string = 'Address')
    x_tutor = fields.Many2one('res.partner', string = 'Tutor')
    x_career = fields.Many2one('academic.career', string = 'Career')