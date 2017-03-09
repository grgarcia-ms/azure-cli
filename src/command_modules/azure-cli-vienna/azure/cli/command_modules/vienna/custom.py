# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
import azure.cli.core.azlogging as azlogging
from azure.cli.core._util import CLIError

logger = azlogging.get_az_logger(__name__)

def attach(name= None, address = None, username= None, password = None):
	"""Attach to compute context"""

	fo = open(name +".cc", "w")
	fo.write( name+ ":\n\taddress: " + address + "\n\tusername: " + username + "\n\tpassword: " + password)
	fo.close()

	return "Compute context attached."

def detach(name = None):
	"""Detach compute context"""

	if name:
		print("Detach")

	return "Compute context detached."

def listc(arguments = None, xtra=None ):
	"""List of compute context"""

	if arguments:
		print(*arguments)