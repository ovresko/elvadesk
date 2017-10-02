# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Diagnostique(Document):
	def before_insert(self):
		pass

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
