from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Troupeau"),
			"items": [
				{
					"type": "doctype",
					"name": "Vache",
                    "label": "Vaches",
					"description": _("Vaches laiteiere"),
				},
				{
					"type": "doctype",
					"name": "Veau",
                    "label": _("Veaux et velles"),
					"description": _("Veaux et velles"),
				},
                {
					"type": "doctype",
					"name": "Taureau",
                    "label": _("Taureaux"),
					"description": _("Taureaux"),
				},
			]
		},

        {
            "label": _("Variantes"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Race",
                    "label": _("Les races"),
                    "description": _("Races presentes dans le Troupeau"),
                },
                {
                    "type": "doctype",
                    "name": "Robe",
                    "label": _("Les robes"),
                    "description": _("Robes presentes dans le Troupeau"),
                },
                {
                    "type": "doctype",
                    "name": "Lots alimentation",
                    "label": _("Lots alimentation"),
                    "description": _("Lots alimentation"),
                },
                {
                    "type": "doctype",
                    "name": "Lots troupeau",
                    "label": _("Lots troupeau"),
                    "description": _("Lots troupeau"),
                },

            ]
        },

        {
            "label": _("Reformes"),
            "items" : [
                {
                "type": "doctype",
                "name": "Reforme",
                "label": _("Reformes"),
                },
                {
                "type":"doctype",
                "name": "Archive vaches",
                "label": _("Archive des vaches"),
                }
            ]
        },

        {
            "label": _("Rapports"),
            "items" : [

            ]
        },
	]
