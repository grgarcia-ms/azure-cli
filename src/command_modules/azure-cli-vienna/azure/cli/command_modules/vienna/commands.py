# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from collections import OrderedDict

from azure.cli.core.commands import cli_command

cli_command(__name__, 'vienna computecontext attach', 'azure.cli.command_modules.vienna.custom#attach')
cli_command(__name__, 'vienna computecontext detach', 'azure.cli.command_modules.vienna.custom#detach')



def transform_account_list(result):
    transformed = []
    for r in result:
        res = OrderedDict([('Name', r['name']),
                           ('CloudName', r['cloudName']),
                           ('SubscriptionId', r['id']),
                           ('State', r['state']),
                           ('IsDefault', r['isDefault'])])
        transformed.append(res)
    return transformed
