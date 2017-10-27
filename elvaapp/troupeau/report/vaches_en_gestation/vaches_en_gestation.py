# Copyright (c) 2013, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = frappe.db.sql('''select name,age,prochain_velage, numero_lactation, date(dob),race , date(debut_velage)
		from tabVache
			where etat_reproduction = "Gestante"''')
	return columns, data

def get_columns():
	return [
		{
			'fieldname': 'name',
			'label': 'Vache',
			'fieldtype': 'Data'
		},
		{
			'fieldname': 'age',
			'label': 'Age',
			'fieldtype': 'Data',
			'width':140
		},
		{
			'fieldname': 'prochain_velage',
			'label': _('Velage presume'),
			'fieldtype': 'Date',
			'width':140
		},
		{
			'fieldname': 'numero_lactation',
			'label': 'N Lactation',
			'fieldtype': 'Int'
		},
		{
			'fieldname': 'dob',
			'fieldtype': 'Date',
			'label': 'Naissance'
		},
		{
			'fieldname': 'race',
			'fieldtype': 'Data',
			'width':120,
			'label': 'Race'
		},
		{
			'fieldname': 'debut_velage',
			'fieldtype': 'Date',
			'width':200,
			'label': 'Debut velage'
		}
	]

# def get_vaches(filters):
# 	return frappe.db.sql("""select name from tabVache where etat_reproduction = 'Gestante' or etat_reproduction = 'Post velage'""", as_list=1)
