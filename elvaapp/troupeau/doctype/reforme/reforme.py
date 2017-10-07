# -*- coding: utf-8 -*-
# Copyright (c) 2017, ovresko tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Reforme(Document):
	def validate(self):
		if(self.vache is None and self.taureau is None and self.veau is None):
			frappe.throw("Il faut choisir le code d'animal à réformé")
