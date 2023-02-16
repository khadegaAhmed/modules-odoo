from odoo import models, fields, api
class Material(models.Model):
    _name='material.event'
    # _inherit = "event.event"
    @api.depends('price', 'number')
    def compute_cost(self):
        for r in self:
            if not r.price:
                r.total_cost=0.0
            else:
                r.total_cost=r.number*r.price

    name=fields.Char(string="Material Name")
    type = fields.Selection([('soundEquipment','SoundEquipment'),('ProjectionEquipment','ProjectionEquipment'),('printedMaterials','Printed Materials')],string="Type",default='soundEquipment')
    price = fields.Float(string="Price ($)", required=True)
    number=fields.Integer(string="Required Number",required=True)
    total_cost= fields.Float(string="Total Cost($)",compute='compute_cost',store=True,readonly=True)
# class NewTypePartner(models.Model):
#     _name='new.type.partener'


#string="Characteristics"