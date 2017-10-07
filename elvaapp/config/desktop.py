# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [

		{
			"module_name": "Troupeau",
			"color": "blue",
			"icon": "assets/frappe/images/cow-silhouette.svg",
			"type": "module",
			"label": _("Troupeau")
		},
		{
			"module_name": "Vaches",
			"color": "yellow",
			"icon": "assets/frappe/images/cow-silhouette.svg",
			"type": "link",
			"link": "list/Vache"
		},
		{
			"module_name": "Alimentation",
			"color": "green",
			"icon": "assets/frappe/images/wheat.svg",
			"type": "module",
			"label": _("Alimentation")
		},
		{
			"module_name": "Reproduction",
			"color": "orange",
			"icon": "assets/frappe/images/medical.svg",
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
			"icon": "assets/frappe/images/heartbeat.svg",
			"type": "module",
			"label": _("Sante")
		},
		{
			"module_name": "La ferme",
			"color": "gray",
			"icon": "assets/frappe/images/transport.svg",
			"type": "module",
			"label": _("La ferme")
		}
	]
