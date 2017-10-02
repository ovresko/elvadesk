// Copyright (c) 2017, ovresko tech and contributors
// For license information, please see license.txt


frappe.ui.form.on('Velage', {
	refresh: function(frm) {
			frm.clear_table('Veau');
	},
	setup: function(frm){
		frm.add_fetch('taureau','name',)
	},
	vache: function(frm){
			var child = cur_frm.add_child("veau");
			frappe.model.set_value(child.doctype, child.name, "mere", frm.doc.vache);
			frappe.model.set_value(child.doctype, child.name, "dob", frm.doc.date_velage);
			frappe.model.set_value(child.doctype, child.name, "race", frm.doc.vache.race);
			cur_frm.refresh_field("veau");

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
