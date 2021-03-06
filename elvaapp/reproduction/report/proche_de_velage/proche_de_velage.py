# Copyright (c) 2013, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _



def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = frappe.db.sql('''select name,age,etat_reproduction, race, date(velage_presume)
		from tabVache
			where etat_reproduction = "Gestante" and velage_presume <= %s and velage_presume > %s''',(frappe.utils.data.add_days(frappe.utils.data.today(),30),frappe.utils.data.add_days(frappe.utils.data.today(),-30) ))
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
			'fieldname': 'etat_reproduction',
			'label': _('Etat'),
			'fieldtype': 'Data',
			'width':140
		},
		{
			'fieldname': 'race',
			'fieldtype': 'Data',
			'width':120,
			'label': 'Race'
		},
		{
			'fieldname': 'velage_presume',
			'fieldtype': 'Date',
			'width':200,
			'label': 'Velage presume'
		}
	]
