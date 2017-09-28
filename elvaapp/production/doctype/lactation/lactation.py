# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Lactation(Document):
	pass

@frappe.whitelist()
def validate_lactation(vache):
	vacheobjecy = frappe.get_doc("Vache",vache)
	#frappe.msgprint(vacheobjecy+"")
	if(vacheobjecy.consommation == "Veaux" or vacheobjecy.consommation == "Abandonner"):
		return """Production doit étre hors consommation humaine
	Pour la vache """+vache+""", """,True
	return "",False