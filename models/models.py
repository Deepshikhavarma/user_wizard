# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResGroups(models.Model):
    _inherit = 'res.groups'

    '''for groups domain filter'''
    quick_user = fields.Boolean(string="Quick User")