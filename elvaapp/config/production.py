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
        }
	]
