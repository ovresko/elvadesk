// Copyright (c) 2017, ovresko tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Diagnostique', {
	onload: function(frm) {
		cur_frm.set_query('insemination', function() {
			return {
				"filters": {
					"vache": frm.doc.vache,
					"resultat": "En attente"
				}
			};
		});
	}
});

cur_frm.add_fetch('insemination','taureau','taureau');
cur_frm.add_fetch('insemination','reference_sperme','reference_ia');

frappe.ui.form.on('Diagnostique','insemination',function(frm){

	var ins = frm.doc.insemination;
	if(ins != undefined){
		frappe.call({
			method:"elvaapp.reproduction.doctype.diagnostique.diagnostique.get_jours",
			args:{
				"insemination": frm.doc.insemination
			},
			callback: function(r){
				frm.set_value('jours',r.message);
			}
		});
		console.log("Update jours "+ins.date);
	}

});
