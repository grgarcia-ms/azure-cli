# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from collections import OrderedDict

from azure.cli.core.commands import cli_command

"""Compute Context Commands"""

cli_command(__name__, 'vienna computecontext attach', 'azure.cli.command_modules.vienna.custom#attach')
cli_command(__name__, 'vienna computecontext detach', 'azure.cli.command_modules.vienna.custom#detach')
# cli_command(__name__, 'vienna computecontext listc', 'azure.cli.command_modules.vienna.custom#listc')

