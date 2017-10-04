# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Lactation(Document):
	def validate(self):
		if(self.qts_total < 1):
			frappe.throw("Quantité non valide")

@frappe.whitelist()
def validate_lactation(vache):
	vacheobjecy = frappe.get_doc("Vache",vache)
	#frappe.msgprint(vacheobjecy+"")
	if(vacheobjecy.etat_lactation != "En lactation"):
		return "La vache {} est {}".format(vacheobjecy.tag, vacheobjecy.etat_lactation),True
	if(vacheobjecy.consommation == "Veaux" or vacheobjecy.consommation == "Abandonner"):
		return """Production doit étre hors consommation humaine
	Pour la vache <br>  خارج استهلاك """+vache+""", """,True

	return "",False

@frappe.whitelist()
def get_vache_en_lactation():
	vaches = frappe.get_list("Vache",filters = {"etat_lactation": "En lactation"},fields= "*")
	return len(vaches)
