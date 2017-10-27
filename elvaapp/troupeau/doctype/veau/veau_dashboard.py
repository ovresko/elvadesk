from frappe import _

def get_data():
	return {
		'fieldname': 'veau',
		'non_standard_fieldnames': {
			'Insemination': 'veau'
		},
		'transactions': [
			{
				'label': _('Sante'),
				'items': ['Dossier medical','Poids']
			}
		]
	}
