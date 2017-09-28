# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Vache(Document):
	pass

@frappe.whitelist()
def set_jours_lactation(_vache):
	vache = frappe.get_doc('Vache',_vache)
	dv = frappe.utils.data.date_diff(frappe.utils.data.today(),vache.debut_lactation)
	#frappe.set_value('Vache',vache.name,'jours_lactation',dv)
	return dv
