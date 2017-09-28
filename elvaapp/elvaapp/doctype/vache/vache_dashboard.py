from frappe import _

def get_data():
	return {
		'fieldname': 'vache',
		'non_standard_fieldnames': {
			'Insemination': 'vache'
		},
		'transactions': [
			{
				'label': _('Reproduction'),
				'items': ['Insemination','Velage','Diagnostique']
			},
			{
				'label': _('Production'),
				'items': ['Lactation item']
			},
			{
				'label': _('Sante'),
				'items': ['Dossier medical','Poids']
			}
		]
	}
