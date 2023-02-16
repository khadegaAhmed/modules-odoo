# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Eventt(models.Model):
    _name = 'event.event'
    _inherit = 'event.event'
    # _inherit =['event.event','organizer.event']
    theme_event = fields.Char(string="Theme Event")
    last_name_id = fields.Many2one('organizer.event',string="Organizer",required=True)
    materials_ids = fields.Many2many('material.event',string="Material")
    partner_id = fields.Many2one('res.partner', domain=[('is_organizer','=',True)],string="Organizer(new type of partner)")


