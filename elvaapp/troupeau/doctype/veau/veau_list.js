frappe.listview_settings['Veau'] = {
	onload: function(listview) {
		if (!frappe.route_options){ //remove this condition if not required
			frappe.route_options = {
				"etat_actuel": ["=", "Active"]
			};
		}
	}
};
