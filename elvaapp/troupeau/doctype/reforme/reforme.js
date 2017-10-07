// Copyright (c) 2017, ovresko tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Reforme', {
	onload: function(frm) {
		cur_frm.set_query('vache', function() {
			return {
				"filters": {
					"etat_actuel": "Active",
				}
			};
		});
		cur_frm.set_query('taureau', function() {
			return {
				"filters": {
					"etat_actuel": "Active",
				}
			};
		});
		cur_frm.set_query('veau', function() {
			return {
				"filters": {
					"etat_actuel": "Active",
				}
			};
		});
	}
});
