# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Diagnostique(Document):
	def before_insert(self):
		vache = frappe.get_doc('Vache',self.vache)
		insemination = frappe.get_doc('Insemination',self.insemination)
		if(self.resultat == 'Positive'):
			#insemination.cancel()
			insemination.resultat = 'Positive'
			insemination._save(ignore_permissions=True)
			#frappe.set_value('Insemination',self.insemination,'resultat','Positive')
			#insemination.submit()
			frappe.set_value('Vache',self.vache,'etat_reproduction','Gestante')
			frappe.set_value('Vache',self.vache,'debut_velage',insemination.date)
			jours_debut_tarissement = frappe.db.get_value("Parametres","Parametres","jours_debut_tarissement")
			jours_gestation = frappe.db.get_value("Parametres","Parametres","duree_gestation")
			date_tarissement = frappe.utils.data.add_days(insemination.date,int(jours_debut_tarissement))
			todo_debut_tarissement = frappe.utils.data.add_days(insemination.date,(int(jours_debut_tarissement)-10))
			velage_presume = frappe.utils.data.add_days(insemination.date,int(jours_gestation))
			frappe.set_value('Vache',self.vache,'debut_tarissement',date_tarissement)
			frappe.set_value('Vache',self.vache,'velage_presume',velage_presume)
			# Velage event
			doc = frappe.get_doc({
				"doctype": "Event",
				"details": """Vélage """+ (vache.tag),
				"status": "Open",
				"subject": "Vélage "+ (vache.tag),
				"starts_on": velage_presume,
				"all_day": "1",
				"event_type":"Public",
				"color":"red",
				"description":"""Vélage """+ (vache.tag)+"""<br>
				Numero insemination"""+ (insemination.name)+"""<br>
				Inseminer le """+str(insemination.date)+""" """ + (insemination.type)
			})
			doc.insert()

			# Tarissement event_type
			doc = frappe.get_doc({
				"doctype": "Event",
				"details": """Début Tarissement """+ (vache.tag),
				"status": "Open",
				"subject": "Tarissement "+ (vache.tag),
				"starts_on": date_tarissement,
				"all_day": "1",
				"event_type":"Public",
				"color":"red",
				"description":"""Tarissement """+ (vache.tag)
			})
			doc.insert()

			date_debut_todo = frappe.utils.data.add_days(velage_presume,-10)
			todo = frappe.get_doc({
				"doctype" : "ToDo",
				"status":"Open",
				"priority":"High",
				"color":"red",
				"date": date_debut_todo,
				"description" : """Vérifier la vache """+(vache.tag)+""" vélage dans moin de 10 jours""",
				"reference_type" : "Velage"
			})
			todo.insert()

			todo = frappe.get_doc({
				"doctype" : "ToDo",
				"status":"Open",
				"priority":"High",
				"color":"red",
				"date": todo_debut_tarissement,
				"description" : """Début tarissement vache"""+(vache.tag)+""", dans moin de 10 jours""",
				"reference_type" : "Tarissement"
			})
			todo.insert()
		if(self.resultat == 'Négative'):
			frappe.set_value('Vache',self.vache,'etat_reproduction','En service')
			frappe.set_value('Vache',self.vache,'debut_velage',None)
			frappe.set_value('Insemination',self.insemination,'resultat','Négative')
			todo = frappe.get_doc({
				"doctype" : "ToDo",
				"status":"Open",
				"priority":"High",
				"color":"red",
				"date": self.date,
				"description" : """Diagnostique négative sur la vache """+(vache.tag)+""" considérer une réinsemination""",
				"reference_type" : "Diagnostique"
			})
			todo.insert()
			

	def validate(self):
		if(not self.vache):
			frappe.throw("Vous devez selectionner la vache")
		if(not self.insemination):
			frappe.throw("Vous devez selectionner une insemination")


@frappe.whitelist()
def get_jours(insemination):
	ins = frappe.get_doc('Insemination',insemination)
	if(ins.date is not None):
		days = frappe.utils.data.date_diff(frappe.utils.data.today(),ins.date)
		return str(days)+" jours"
