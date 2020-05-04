# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class UserTemplate(models.TransientModel):
	_name = 'users.wizard'

	@api.multi
	def create_user(self):

		'''To check if selected primary client id is in logged user allowed company list'''
		user = self.env.user
		company_list = []
		for x in user.company_ids:
			company_list.append(x.id)
		if self.primary_client.id not in company_list:
			raise Warning(_("The selected Primary Client is not in the allowed companies list of the logged in user"))
		else:
			'''creates new user'''
			data={'name': self.name,
				'login':self.email,
				'company_id':self.primary_client.id,
				}

			'''adds access group to newly created user'''
			res = self.env['res.users'].create(data)
			group = self.env['res.groups'].search([('name','=',self.user_type.name)])
			get_user = self.env['res.users'].search([('login','=',self.email)])
			group_data = [(0,0,{'name':get_user.id,
				'login':get_user.login})]
			group.write({'users': [(4, get_user.id)]})
			
			'''Opens the newly created user on boolean check'''
			if self.user_setting == True:
				user = self.env['ir.actions.act_window'].for_xml_id('base', 
					'action_res_users')
				user['domain'] = [('login', '=', self.email)]
				return user
			return res

	
	

	name = fields.Char(string="First Name", required=True)
	last_name =  fields.Char(string="Last Name")
	email = fields.Char(string="Email", required=True)
	primary_client = fields.Many2one('res.company', string="Primary Client", required=True)
	user_type = fields.Many2one('res.groups', string="user Type",
		domain = "[('quick_user','=',True)]", required=True)
	user_setting = fields.Boolean(string="Open User Setting")


