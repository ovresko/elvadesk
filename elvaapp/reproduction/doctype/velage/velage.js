// Copyright (c) 2017, ovresko tech and contributors
// For license information, please see license.txt


frappe.ui.form.on('Velage', {
	refresh: function(frm) {

	},
	setup: function(frm){
		frm.add_fetch('taureau','name',)
	},
	onload: function(frm){
		cur_frm.set_query('vache', function() {
			return {
				"filters": {
					"etat_reproduction": 'Gestante'
				}
			};
		});
	}
});
