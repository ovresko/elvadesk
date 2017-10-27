// Copyright (c) 2017, ovresko tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Veau', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		// frappe.msgprint(__("Please create new account from Chart of Accounts."));
		//frm.add_custom_button(__('Chart of Accounts'),
		//function () { frappe.set_route("Tree", "Account"); });

		if(!frm.doc.__islocal){
			var _dob = calculate_age(frm);
			get_etat_sante(frm);
			cur_frm.set_value("age",_dob);
			cur_frm.refresh();
			}



	}
});



frappe.ui.form.on("Veau","dob",function(frm){
	var _dob = calculate_age(frm);
	cur_frm.set_value("age",_dob);

});


function get_etat_sante(frm){

 frappe.call({
		method: "frappe.client.get_list",
		args:
		{
			"doctype" : "Dossier medical",
			"filters" : {"veau":frm.doc.name},
			"fields" : "*"
		},
		callback: function(r){
			var status='Aucun dossier medical';
			var medics ='Aucun médicament';
			console.log(r.message)
			if(typeof r.message != "undefined"){
				if(r.message.length > 0){
					status = (r.message[0]).name;
					if(r.message[0].medicament != "undefined"){
						medics = (r.message[0]).medicament;
					}
					console.log(r.message.name);
					console.log(r.message.medicament);
				}
			}else{
				console.log("r.exc");
			}
			console.log("Putting sante as :" + status);
			cur_frm.set_value("sante",status);
			cur_frm.set_value("medicaments",medics);
		}
	});

}

var calculate_age = function(frm){

	var dob = new Date(frm.doc.dob);
	var today = new Date();
	var age = Math.floor((today-dob) / (24 * 60 * 60 * 1000));
	// $('#age').html(age+' years old');
	var mois = age / 30;
	var astring = ''
	if(mois > 12){
		var years = cint(mois / 12);
		var months = cint(mois - (years * 12));
		astring =  years + " ans et "+ (months)+" mois";
	}
	else if(mois < 3){
		// get days
		astring = cint(age)+" jours";
	}
	else if(mois <= 12){
		astring = cint(mois) + " mois";
	}
	return astring;
}