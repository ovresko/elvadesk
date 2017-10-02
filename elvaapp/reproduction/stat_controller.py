# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def insemination_event(insemination,method):
    vache = frappe.get_doc("Vache",insemination.vache)
    frappe.msgprint("La vache {} est inseminée avec succée".format(insemination.vache   ))
    if(insemination.resultat == 'En attente'):
        frappe.set_value('Vache',vache.tag,'derniere_insemination',insemination.date)
        vache = frappe.set_value('Vache',vache.tag,'etat_reproduction','En attente')
        jours_diagnostique = frappe.db.get_value("Parametres","Parametres","jours_diagnostique")
        date_debut = frappe.utils.data.add_days(insemination.date,int(jours_diagnostique))
        date_debut_todo = frappe.utils.data.add_days(insemination.date,int(jours_diagnostique)- 10)
        #frappe.msgprint(date_debut)
        doc = frappe.get_doc({
            "doctype": "Event",
            "details": """Diagnostique """+ (vache.tag)+"""<br>
            Inseminer le """+(insemination.date)+""" """ + (insemination.type),
            "status": "Open",
            "subject": "Diagnostique "+ (vache.tag),
            "starts_on": date_debut,
            "all_day": "1",
            "event_type":"Public",
            "color":"red",
            "description":"""Diagnostique """+ (vache.tag)+"""<br>
            Numero insemination"""+ (insemination.name)+"""<br>
            Inseminer le """+(insemination.date)+""" """ + (insemination.type)
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

def diagnostique_event(diagnostique,method):
	vache = frappe.get_doc('Vache',diagnostique.vache)
	insemination = frappe.get_doc('Insemination',diagnostique.insemination)
	if(diagnostique.resultat == 'Positive'):
		#insemination.cancel()
		insemination.resultat = 'Positive'
		insemination._save(ignore_permissions=True)
		#frappe.set_value('Insemination',self.insemination,'resultat','Positive')
		#insemination.submit()
		frappe.set_value('Vache',diagnostique.vache,'etat_reproduction','Gestante')
		frappe.set_value('Vache',diagnostique.vache,'debut_velage',insemination.date)
		jours_debut_tarissement = frappe.db.get_value("Parametres","Parametres","jours_debut_tarissement")
		jours_gestation = frappe.db.get_value("Parametres","Parametres","duree_gestation")
		date_tarissement = frappe.utils.data.add_days(insemination.date,int(jours_debut_tarissement))
		todo_debut_tarissement = frappe.utils.data.add_days(insemination.date,(int(jours_debut_tarissement)-10))
		velage_presume = frappe.utils.data.add_days(insemination.date,int(jours_gestation))
		frappe.set_value('Vache',diagnostique.vache,'debut_tarissement',date_tarissement)
		frappe.set_value('Vache',diagnostique.vache,'velage_presume',velage_presume)
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
	if(diagnostique.resultat == 'Négative'):
		frappe.set_value('Vache',diagnostique.vache,'etat_reproduction','En service')
		frappe.set_value('Vache',diagnostique.vache,'debut_velage',None)
		frappe.set_value('Insemination',diagnostique.insemination,'resultat','Négative')
		todo = frappe.get_doc({
			"doctype" : "ToDo",
			"status":"Open",
			"priority":"High",
			"color":"red",
			"date": diagnostique.date,
			"description" : """Diagnostique négative sur la vache """+(vache.tag)+""" considérer une réinsemination""",
			"reference_type" : "Diagnostique"
		})
		todo.insert()

def velage_event(velage,method):
    _velage = frappe.get_doc('Velage',velage.name)
    vache = frappe.get_doc('Vache',_velage.vache)
    frappe.set_value('Vache',velage.vache,'etat_reproduction','Post velage')
    frappe.set_value('Vache',velage.vache,'date_velage',_velage.date_velage)
    jours_post_velge = frappe.db.get_value("Parametres","Parametres","jours_post_velge")
    date_debut_service = frappe.utils.data.add_days(velage.date_velage,int(jours_post_velge))
    frappe.set_value('Vache',velage.vache,'debut_service',date_debut_service)
    frappe.set_value('Vache',velage.vache,'derniere_insemination',None)
    frappe.set_value('Vache',velage.vache,'debut_tarissement',None)
    frappe.set_value('Vache',velage.vache,'debut_velage',None)
    frappe.set_value('Vache',velage.vache,'velage_presume',None)
    frappe.set_value('Vache',velage.vache,'prochain_velage',None)
    frappe.set_value('Vache',velage.vache,'velage_presume',None)
    nombre_velage = vache.nombre_velage
    nombre_velage += 1
    frappe.set_value('Vache',velage.vache,'nombre_velage',nombre_velage)
    debut_lactation = frappe.utils.data.add_days(_velage.date_velage,2)
    frappe.set_value('Vache',velage.vache,'debut_lactation',debut_lactation)
    doc = frappe.get_doc({
        "doctype": "Event",
        "details": """Entre en service """+ (vache.tag),
        "status": "Open",
        "subject": "Entre en service "+ (vache.tag),
        "starts_on": date_debut_service,
        "all_day": "1",
        "event_type":"Public",
        "color":"red",
        "description":"La vache {} entre en service".format(vache.tag)
    })
    doc.insert()
    frappe.msgprint("Velage éffectué {} avec succée".format(_velage))
