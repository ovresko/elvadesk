from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Production"),
			"items": [
				{
					"type": "doctype",
					"name": "Lactation",
                    "label": "Sessions lactation",
					"description": _("Sessions lactation"),
				},
				{
					"type": "doctype",
					"name": "Tarissement",
                    "label": "Tarissements",
					"description": _("Tarissements"),
				},
			]
		},
        {
            "label": _("Stock"),
            "items": [
            {
                "type": "doctype",
				"name": "Indices lait",
				"label": "Indices lait",
                "description": _("Indices lait"),
            },
            ]
        },
		{
            "label": _("Rapports"),
			"icon": "fa fa-list",
            "items" : [
				{
				"type": "report",
				"is_query_report": True,
				"name": "Rapport Qts lactation",
				"doctype": "Lactation",
				"label": "Rapport journalier Qts lactation"
				}
            ]
        }
	]
