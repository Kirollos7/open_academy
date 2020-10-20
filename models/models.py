# -*- coding: utf-8 -*-

# Simple Fieldes like:
	# Char, Date, Boolean

# Special Fields:
	#


from odoo import models, fields, api

class Course(models.Model):
	_name = 'openacademy.course'
	_description = 'Open Academy Courses'

	name = fields.Char('Title', required=True, index=True, help='Enter Title of a Course',)
	description = fields.Text(required=True)




# any table created on database have a Reserved Fields
# Reserved Fields:
	# id
	# create_date
	# create_uid --> user id
	# write date --> last modification date
	# write_uid --> last user doing modification

