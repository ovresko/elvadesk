frappe.pages['performance-producti'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Performance production',
		single_column: true
	});
}