from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Programs"),
			"items": [
				{
					"type": "doctype",
					"name": "Program1",
					"onboard": 1,
				},
				
			]
		}
		
	]
