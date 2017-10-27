// Copyright (c) 2016, ovresko tech and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Vaches en gestation"] = {
	"filters": [
		{
			"fieldname":"name",
			"label": __("Etat"),
			"fieldtype": "Select",
			"options": "Post velage\nGestante",
		}
	]
}
