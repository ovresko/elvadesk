# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import frappe.website.render

page_title = "Vaches"
no_cache = 1

def get_context(context):
    context.no_cache = 1
    context.data = ["566","662525","5555"]
