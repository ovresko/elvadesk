# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def insert_session(lactation, method):
    stock_value = frappe.db.get_value("Indices lait","Indices lait","qts_lait_total")
    today = lactation.qts_total
    value_  = int(stock_value) + (today)
    frappe.msgprint("Session enregistrée avec succée, qts total = {} litres.".format(value_))
    frappe.db.set_value("Indices lait","Indices lait","qts_lait_total",value_)

def taris_vache(tarissement,method):
    vache = frappe.get_doc("Vache",tarissement.vache)
    frappe.msgprint("Tarissement terminé")
    today = frappe.utils.today()
    if(today > tarissement.date_debut and today < tarissement.date_fin):
        frappe.set_value("Vache",tarissement.vache,"etat_lactation","En tarissement")
    doc = frappe.get_doc({
        "doctype": "Event",
        "details": """Tarissement """+ (vache.tag),
        "status": "Open",
        "subject": "Tarissement "+ (vache.tag),
        "starts_on": tarissement.date_debut,
        "all_day": "1",
        "event_type":"Public",
        "color":"red",
        "description":"""Tarissement """+ (vache.tag)+"""<br>
        Numero tarissement"""+ (tarissement.name)+"""<br>
        Periode : """+(tarissement.date_debut)+""" => """ + (tarissement.date_fin)
    })
    doc.insert()

    doc = frappe.get_doc({
        "doctype": "Event",
        "details": """Fin Tarissement """+ (vache.tag),
        "status": "Open",
        "subject": "Fin Tarissement "+ (vache.tag),
        "starts_on": tarissement.date_fin,
        "all_day": "1",
        "event_type":"Public",
        "color":"red",
        "description":"""Fin Tarissement """+ (vache.tag)+"""<br>
        Numero tarissement"""+ (tarissement.name)+"""<br>
        Periode : """+(tarissement.date_debut)+""" => """ + (tarissement.date_fin)
    })
    doc.insert()
