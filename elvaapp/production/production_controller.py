# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def check_article_milk(method):
    found = frappe.db.exists("Item","lait")
    frappe.msgprint("Lait found : {}".format(found))
    if(found == None):
        doc = frappe.get_doc({
        "doctype": "Item",
        "item_code": "lait",
        "item_group":"Produits",
        "is_stock_item": True,
        "stock_uom": "litre"
        })
        doc.insert()

def insert_session(lactation, method):
    check_article_milk(method)
    stock_value = frappe.db.get_value("Indices lait","Indices lait","qts_lait_total")
    today = lactation.qts_total
    value_  = int(stock_value) + (today)
    frappe.msgprint("Session enregistrée avec succée, qts total = {} litres.".format(value_))
    frappe.db.set_value("Indices lait","Indices lait","qts_lait_total",value_)
    '''
    Make stock entry'''
    from erpnext.stock.doctype.stock_entry.stock_entry_utils import make_stock_entry

    # default warehouse, or Stores
    ''':item_code: Item to be moved
	:qty: Qty to be moved
	:from_warehouse: Optional
	:to_warehouse: Optional
	:rate: Optional
	:serial_no: Optional
	:batch_no: Optional
	:posting_date: Optional
	:posting_time: Optional
	:do_not_save: Optional flag
	:do_not_submit: Optional flag
	'''
    stock_entry = make_stock_entry(item_code="lait", to_warehouse="Reservoir lait", qty=today, purpose = "Manufacture" )

    stock_entry.add_comment("Comment", ("Opening Stock"))

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
