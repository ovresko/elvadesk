// Copyright (c) 2017, ovresko tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('aliments', {
	onload: function(frm) {
		cur_frm.set_query('aliment', function() {
			return {
				"filters": {
					"item_group": "Consommable"
				}
			};
		});
	}
});
