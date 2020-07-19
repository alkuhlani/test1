# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		# Modules
		{

			"module_name": "Funding Management",
			"color": "grey",
			"icon": "icon grant-blue",
			"type": "module",
			"label": _("Funding Management")
		},
                {

			"module_name": "Program Management",
			"color": "grey",
			"icon": "icon pm-blue",
			"type": "module",
			"label": _("Program Management")
		},
                {

			"module_name": "MEAL",
			"color": "grey",
			"icon": "icon me-blue",
			"type": "module",
			"label": _("MEAL")
		}


	]
