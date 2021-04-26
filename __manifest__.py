{
    'name': 'Technical Reporting',
    'description': 'Report manage intervention reports',
    'author': 'Castel Jeremy, Lenhard Erwan, Very-Griette Milan',
    'depends': ['base', 'account', 'account_move'],
    'data': [
			'security/groups.xml',
			'security/ir.model.access.csv',
			'views/tr_global_report.xml',
			'views/tr_report.xml',
			'views/tr_block.xml'
		],
    'application': True,
}
