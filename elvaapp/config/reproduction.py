from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Reproduction"),
			"items": [
				{
					"type": "doctype",
					"name": "Insemination",
                    "label": "Inseminations",
					"description": _("Operations d'inseminatins"),
				},
				{
					"type": "doctype",
					"name": "Velage",
                    "label": _("Mise bas"),
					"description": _("Operations des Velages"),
				},
                {
					"type": "doctype",
					"name": "Diagnostique",
                    "label": _("Diagnostiques"),
					"description": _("Operations des Diagnostiques"),
				},
			]
		},
        {
            "label": _("Vaches par etat"),
            "items": [
            {
                "type": "report",
				"is_query_report": True,
				"name": "Vaches en service",
				"doctype": "Vache"
            },
            {
                "type": "report",
				"is_query_report": True,
				"name": "Proche de velage",
				"doctype": "Vache"
            }
            ]
        }
	]
