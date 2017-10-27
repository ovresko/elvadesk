# Copyright (c) 2013, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _



def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = frappe.db.sql('''select date,numero,vache_on_lactation, qts_total, nombre_vache, top_productrice
		from tabLactation where date(date) = %s''',(filters.get("date")))
	return columns, data

def get_columns():
	return [
		{
			'fieldname': 'date',
			'label': 'Date',
			'fieldtype': 'Date'
		},
		{
			'fieldname': 'numero',
			'label': 'Numero Lactation',
			'fieldtype': 'Data',
			'width':140
		},
		{
			'fieldname': 'vache_on_lactation',
			'label': _('Nombre de vache'),
			'fieldtype': 'Data',
			'width':140
		},
		{
			'fieldname': 'qts_total',
			'fieldtype': 'Float',
			'width':120,
			'label': 'Qts lait'
		},
		{
			'fieldname': 'nombre_vache',
			'fieldtype': 'Data',
			'width':200,
			'label': 'Nombre de vache'
		},
		{
		'fieldname': 'top_productrice',
		'fieldtype': 'Data',
		'width': 150,
		'label': 'Top productrice'
		}
	]
