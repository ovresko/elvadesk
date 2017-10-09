// Copyright (c) 2017, ovresko tech and contributors
// For license information, please see license.txt



frappe.ui.form.on("Lactation",{
		refresh: function(frm){
			if(!frm.doc.__islocal){
				frm.add_custom_button('Créer nouveau',function(){
					btn_save_and_new(frm);
				});
			}


		},
		onload: function(frm){
			frappe.call({
				method:"elvaapp.production.doctype.lactation.lactation.get_vache_en_lactation",
				callback: function(r){
					frm.set_value("vache_on_lactation",r.message);
					cur_frm.refresh();
				}
			});
		}
	}
);

frappe.ui.form.on('Lactation', {
	onload: function(frm) {
		console.log("onload");
	}
});


// cur_frm.add_fetch("vache_name", "date", cur_frm.doc.date);
// cur_frm.add_fetch("vache_name", "numero_session", cur_frm.doc.numero);
// cur_frm.add_fetch("vache_name", "qts", undefined);

frappe.ui.form.on("Lactation","ajouter_tout",function(frm){
	frappe.call({
		method:"frappe.client.get_list",
		args:{
			"doctype": "Vache",
			"filters":{
				"etat_lactation":"En lactation",
				"etat_actuel":"Active"	
		},
			"fields" :"*"
		},
		callback: function(r){
			console.log(r.message);
			fill_table(r.message);

		}

	});
});

frappe.ui.form.on("Lactation","ajouter",function(frm){
	var vache = cur_frm.doc.chercher_vache;
	console.log(vache);
	add_vache(vache);
});

frappe.ui.form.on("Lactation item","qts",function(frm){
	calculate_totals(frm);
});

frappe.ui.form.on("Lactation item","vache_name",function(frm){
	var line = frm.doc.lactations.length-1;
	if(line > -1){
		var row = frm.doc.lactations[line];
		row.date = frm.doc.date;
		row.numero_session = frm.doc.numero;
	}
	console.log(line);
	cur_frm.set_value("lactations","date", frappe.datetime.nowdate());
	cur_frm.refresh();
	calculate_totals(frm);

});

var fill_table = function(vaches){
	vaches.forEach( function(row){
			// var r = check_vache(row);
			// var result = r.message[1];
			// if(!result){
			// 	frappe.msgprint(r.message[0]);
			// 	frappe.throw('SSSS');
			// }

			var child = cur_frm.add_child("lactations");
			console.log(row);
			frappe.model.set_value(child.doctype, child.name, "vache_name", row.name);
			frappe.model.set_value(child.doctype, child.name, "date", cur_frm.doc.date);
			frappe.model.set_value(child.doctype, child.name, "numero_session", cur_frm.doc.numero);
			frappe.model.set_value(child.doctype, child.name, "qts", 0);
			frappe.model.set_value(child.doctype, child.name, "remarques", "");
		});


		cur_frm.refresh();
		calculate_totals(cur_frm);

};

function add_vache(vache){
	if(typeof vache == "undefined"){
		frappe.msgprint("Selectionner une vache d'abord");
	}else{
		console.log("add_vache : "+vache);

		check_vache(vache);

		var child = cur_frm.add_child("lactations");
		frappe.model.set_value(child.doctype, child.name, "vache_name", vache);
		frappe.model.set_value(child.doctype, child.name, "date", cur_frm.doc.date);
		frappe.model.set_value(child.doctype, child.name, "numero_session", cur_frm.doc.numero);
		frappe.model.set_value(child.doctype, child.name, "qts", undefined);
		frappe.model.set_value(child.doctype, child.name, "remarques", "");

		cur_frm.set_value("chercher_vache",undefined);
		cur_frm.refresh();
		calculate_totals(cur_frm);
	}
}



function calculate_totals(frm){
	console.log("Executing calcalte totals");
	var nombre_vache = 0;
	var qts_total = 0.0;
	var top_prod = 0.0;
	var vache_top_prod = undefined;
	$.each(frm.doc.lactations, function(i,lact){
		console.log("Valuse "+lact.qts);
		nombre_vache += 1;
		qts_total += flt(lact.qts);
		if(lact.qts > top_prod){
			console.log(top_prod + " is smaller "+lact.qts);
			top_prod = lact.qts;
			console.log("top prod = "+top_prod	);

			vache_top_prod = lact.vache_name;
		}
	});

	frm.set_value('qts_total',qts_total);
	frm.set_value('nombre_vache',nombre_vache);
	frm.set_value('top_productrice','vache : '+vache_top_prod + ' / produit : ' + top_prod+' Lrs');

}

var btn_save_and_new = function (frm) {
	if (!frm.doc.name) {
		frappe.throw("Enrsgitrer d'abord 'Ctr + S'");
	}
	frappe.route_options = {
		"numero": frm.doc.numero,
	};
	frappe.new_doc("Lactation");
};

function check_vache(vache){

	console.log("calling: check_vache "+ vache);

	frappe.call({
		method : "elvaapp.production.doctype.lactation.lactation.validate_lactation",
		args:{
			"vache":vache
		},
		callback: function(r){
			console.log("Returning from check_vache ");
			if(r.message[1]){
				frappe.msgprint(r.message[0]);
				// cur_frm.doc.lactations.splice(cur_frm.doc.lactations.indexOf(vache),1);
				// cur_frm.refresh_field('lactations');
			}
		}
	});




}
