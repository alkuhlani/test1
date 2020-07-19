from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Quality"),
			"items": [
				{
					"type": "doctype",
					"name": "Goals",
					"onboard": 1,
				},
				
			]
		}
		
	]
