from odoo import models,fields, api

class ResPartner(models.Model):
    #Inherits from partner model
    _inherit =  'res.partner'
    x_commercial_name = fields.Char(string = 'Nombre Comercial')
    x_janaq_partner = fields.Many2one('janaq.partner', string = 'Contacto Janaq')   

class JanaqPartner(models.Model):
    # Partner especial para Janaq
    _name = 'janaq.partner'

    x_name = fields.Char(string = 'Name')
    x_code = fields.Char(string = 'Code')
    x_salary = fields.Float(string = 'Salary')