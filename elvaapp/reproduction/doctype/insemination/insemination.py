# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Insemination(Document):
	def on_submit(self):
		vache = frappe.get_doc("Vache",self.vache)
		if(self.resultat == 'En attente'):
			result,message = VachePeutInseminer(vache)
			if(not result):
				frappe.throw(message)
				return
			frappe.set_value('Vache',vache.tag,'derniere_insemination',self.date)
			vache = frappe.set_value('Vache',vache.tag,'etat_reproduction','En attente')
			jours_diagnostique = frappe.db.get_value("Parametres","Parametres","jours_diagnostique")
			date_debut = frappe.utils.data.add_days(self.date,int(jours_diagnostique))
			date_debut_todo = frappe.utils.data.add_days(self.date,int(jours_diagnostique)- 10)
			#frappe.msgprint(date_debut)
			doc = frappe.get_doc({
				"doctype": "Event",
				"details": """Diagnostique """+ (vache.tag)+"""<br>
				Inseminer le """+(self.date)+""" """ + (self.type),
				"status": "Open",
				"subject": "Diagnostique "+ (vache.tag),
				"starts_on": date_debut,
				"all_day": "1",
				"event_type":"Public",
				"color":"red",
				"description":"""Diagnostique """+ (vache.tag)+"""<br>
				Numero insemination"""+ (self.name)+"""<br>
				Inseminer le """+(self.date)+""" """ + (self.type)
			})
			doc.insert()

			todo = frappe.get_doc({
				"doctype" : "ToDo",
				"status":"Open",
				"priority":"High",
				"color":"red",
				"date": date_debut_todo,
				"description" : """Diagnostiquer la vache """+(vache.tag)+""" dans moin de 10 jours""",
				"reference_type" : "Insemination"
			})
			todo.insert()
			#frappe.msgprint(date_debut_todo)

	def validate(self):
		vache = frappe.get_doc("Vache",self.vache)
		result,message = VachePeutInseminer(vache,self)
		if(not result):
			frappe.throw(message)
			return

def VachePeutInseminer(vache,ins):
	if(ins.name is None):		
		if(vache.status != 'Vache' and vache.status != 'Génisse'):
			return False,u'La vache est une '+ (vache.status) + ', vous pouvez pas inseminer'
		if(vache.etat_reproduction != 'En service' and vache.etat_reproduction != 'En attente'):
			return False,u"Vous pouvez pas inseminer cette vache "+ (vache.etat_reproduction)+", mettre a jour l'état reproduction <br>"
		return True,''
