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
