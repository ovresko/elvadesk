# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "ElvaApp",
			"color": "green",
			"icon": "assets/frappe/images/cow-silhouette.svg",
			"type": "module",
			"label": _("ElvaApp")
		},
		{
			"module_name": "Troupeau",
			"color": "blue",
			"icon": "assets/frappe/images/cow-silhouette.svg",
			"type": "module",
			"label": _("Troupeau")
		},
		{
			"module_name": "Reproduction",
			"color": "orange",
			"icon": "assets/frappe/images/cow-silhouette.svg",
			"type": "module",
			"label": _("Reproduction")
		},
		{
			"module_name": "Production",
			"color": "gray",
			"icon": "assets/frappe/images/milk.svg",
			"type": "module",
			"label": _("Production")
		},
		{
			"module_name": "Sante",
			"color": "purple",
			"icon": "assets/frappe/images/milk.svg",
			"type": "module",
			"label": _("Sante")
		}
	]
