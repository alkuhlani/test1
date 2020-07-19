from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Funding"),
			"items": [
				{
					"type": "doctype",
					"name": "Project Proposal",
					"onboard": 1,
				},
				
			]
		}
		
	]
