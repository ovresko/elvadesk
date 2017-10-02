# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Insemination(Document):
	def validate(self):
		vache = frappe.get_doc("Vache",self.vache)
		result,message = VachePeutInseminer(vache)
		if(not result):
			frappe.throw(message)
			return

def VachePeutInseminer(vache):
	if(vache.status != 'Vache' and vache.status != 'Génisse'):
		return False,u'La vache est une '+ (vache.status) + ', vous pouvez pas inseminer'
	if(vache.etat_reproduction != 'En service' and vache.etat_reproduction != 'En attente'):
		return False,u"Vous pouvez pas inseminer cette vache "+ (vache.etat_reproduction)+", mettre a jour l'état reproduction <br>"
	return True,''
