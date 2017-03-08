# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
import azure.cli.core.azlogging as azlogging
from azure.cli.core._util import CLIError

logger = azlogging.get_az_logger(__name__)

def attach(address = None, username= None, password = None):
	"""Attach to compute context"""

	fo = open("context.cc", "w")
	fo.write( "targets:\n\tremote:\n\t\taddress: " + address + "\n\t\tusername: " + username + "\n\t\tpassword: " + password)
	fo.close()

	return "Executed vienna command attach"

def detach(name = None):
	"""Detach compute context"""

	if name:
		print("Detach")

	return "Executed vienna command detach"