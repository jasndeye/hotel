from odoo import models,fields,api

class Specification(models.Model):
     _name = 'hotel.specification'
     
     nom=fields.Char(string="Spécification")