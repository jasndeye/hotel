from odoo import models,fields,api

class Reservation(models.Model):
     _name = 'hotel.reservation'
     
     date_deb=fields.Datetime(string="Date de Debut")
     date_fin=fields.Datetime(string="Date de Fin")
     etat=fields.Selection([('r','reservé'),('v','validé'),('a','annulé')], default="d", string="Etat de la réservation")
     chambre_ids=fields.Many2many('hotel.chambre', string='Chambres')