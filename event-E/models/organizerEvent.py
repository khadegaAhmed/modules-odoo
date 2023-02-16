# -*- coding: utf-8 -*-
import re
from odoo.exceptions import UserError,ValidationError
from odoo import models, fields, api
class Organizer(models.Model):
    _name = 'organizer.event'

    @api.depends('first_name', 'last_name')
    def compute_name(self):
        self.name = (self.first_name or '') + ' ' + (self.last_name or '')
    @api.constrains('phone')
    def validate_phone(self):
        if self.phone:
            match = re.match('^[1-9]\d{8}$',self.phone)
            if not match:
                raise ValidationError('The entered number is wrong!')

    @api.onchange('mail')
    def validate_email(self):
        if self.mail:
            match = re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.mail)
            if not match:
                raise ValidationError('the Email enterd is wrong , try use the following pattern: aaa@aaa.aaa')

    @api.onchange('first_name')
    def onchange_first_name(self):
        if self.first_name:
            self.first_name=str((self.first_name).title())
        else:
            self.first_name=''

    @api.onchange('last_name')
    def onchange_last_name(self):
        if self.last_name:
            self.last_name= str((self.last_name).title())
        else:
            self.last_name = ''

    first_name = fields.Char(string="First Name",required=True)
    last_name = fields.Char(string="Last Name",required=True)
    name = fields.Char(compute='compute_name',store=True)
    my_select = fields.Selection([('mr','Mr'),('mrs','Mrs'),('miss','Miss'),('ms','Ms')],default='mr',string="Personal Title",help="please select Personal Type")
    phone = fields.Char(string="Phone",required=True)
    mail = fields.Char(string="Email")
    is_customer = fields.Boolean(string='Is a Custmoer', default=False,
                                help="Check if the organizer is a company, otherwise it is a vendor")


class ResPartner(models.Model):
    _inherit = 'res.partner'
    # _name='organizer.ev'
    is_organizer = fields.Boolean(string='Is a Organizer', default=False,
                                help="Check if the contact is a organizer")

#,default='mr'
#,('mrs','Mrs'),('miss','Miss') ,,('ms','Ms')
