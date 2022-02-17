from email.mime import image
from email.policy import default
from odoo import models,fields,api

class Chambre(models.Model):
     _name = 'hotel.chambre'

     nom=fields.Char(string="Chambre")
     image= fields.Binary(string="Photo")
     description= fields.Text(string="description")
     tarif_horaire= fields.Float(string="Tarif horaire")
     etat=fields.Selection([('d','disponible'),('o','occupe')], default="d", string="Etat Chambre")
     specification=fields.Many2many('hotel.specification')
     type=fields.Selection([('s','suite'),('sg','single'),('d','double'),('t','triple')], string="Type de Chambre")
     nbre_lit=fields.Integer(string="Nombre de lit")
     nbre_personne=fields.Integer(string="Nombre de personne")
     
     # reservation_ids=fields.Many2many('hotel.reservation',string='Reservation')