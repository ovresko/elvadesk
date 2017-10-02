# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Velage(Document):
	def validate(self):
		if( self.resultat == 'Succée' and len(self.veau) < 1):
			frappe.throw("Il faut insérer le/les veau(x) née(s)")
		vache = frappe.get_doc('Vache',self.vache)
		if(vache.etat_reproduction != 'Gestante'):
			frappe.throw("La vache n'est pas gestante")
		jg = frappe.utils.data.date_diff(frappe.utils.data.today(),vache.debut_velage)
		if(jg < 240):
			 frappe.throw("La vache {} est gestante depuis {} jours seulement, vérifier la date début vélage vache".format(vache,jg))
