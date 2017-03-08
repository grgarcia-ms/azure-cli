# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import register_cli_argument

register_cli_argument('vienna computecontext attach', 'address', options_list=('--address','-a'), help='Specifies compute context address to attach.')
register_cli_argument('vienna computecontext attach', 'username', options_list=('--username','-u'), help='Specifies compute context username to attach.')
register_cli_argument('vienna computecontext attach', 'password', options_list=('--password','-p'), help='Specifies compute context password to attach.')

register_cli_argument('vienna computecontext detach', 'name', options_list=('--name','-n'), help='Specifies compute context name to detach.')

# register_cli_argument('vienna computecontext', 'attach', options_list=('--attach', '-a'), help='Specifies compute context to attach.')
# register_cli_argument('vienna computecontext', 'dettach', options_list=('--dettach', '-d'), help='Specifies compute context to dettach.')

# register_cli_argument('login', 'service_principal', action='store_true', help='The credential representing a service principal.')
# register_cli_argument('login', 'username', options_list=('--username', '-u'), help='Organization id or service principal')
# register_cli_argument('login', 'tenant', options_list=('--tenant', '-t'), help='The AAD tenant, must provide when using service principals.')