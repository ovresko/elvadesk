# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def reforme_vache(reforme,method):
    frappe.msgprint("In reforme vache")
    if(reforme.vache is not None):
        vache = frappe.get_doc('Vache',reforme.vache)
        frappe.set_value('Vache',reforme.vache,'etat_actuel',reforme.type_reforme)
        return None
    if(reforme.tureau is not None):
        taureau = frappe.get_doc('Taureau',reforme.taureau)
        frappe.set_value('Taureau',reforme.taureau,'etat_actuel',reforme.type_reforme)
        return None
    if(reforme.veau is not None):
        frappe.set_value('Veau',reforme.veau,'etat_actuel',reforme.type_reforme)
        return None
