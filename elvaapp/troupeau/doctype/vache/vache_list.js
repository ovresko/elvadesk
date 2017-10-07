frappe.listview_settings['Vache'] = {
	onload: function(listview) {
		if (!frappe.route_options){ //remove this condition if not required
			frappe.route_options = {
				"etat_actuel": ["=", "Active"]
			};
		}
	}
};
