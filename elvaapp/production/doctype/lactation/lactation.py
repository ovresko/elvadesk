# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Lactation(Document):
	def before_insert(self):
		stock_value = frappe.db.get_value("Parametres","Parametres","stock")
		today = self.qts_total
		frappe.msgprint(stock_value)
		value_  = int(stock_value) + int(today)
		frappe.db.set_value("Parametres","Parametres","stock",value_)
	def validate(self):
		if(self.qts_total < 1):
			frappe.throw("Quantité non valide")

@frappe.whitelist()
def validate_lactation(vache):
	vacheobjecy = frappe.get_doc("Vache",vache)
	#frappe.msgprint(vacheobjecy+"")
	if(vacheobjecy.consommation == "Veaux" or vacheobjecy.consommation == "Abandonner"):
		return """Production doit étre hors consommation humaine
	Pour la vache """+vache+""", """,True
	return "",False
