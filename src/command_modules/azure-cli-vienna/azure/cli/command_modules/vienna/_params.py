# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
import argparse
from azure.cli.core.commands import register_cli_argument, register_extra_cli_argument

""" Compute Context Arguments """

register_cli_argument('vienna computecontext attach', 'name', options_list=('--name','-n'), help='Specifies compute context name.')
register_cli_argument('vienna computecontext attach', 'address', options_list=('--address','-a'), help='Specifies compute context address to attach.')
register_cli_argument('vienna computecontext attach', 'username', options_list=('--username','-u'), help='Specifies compute context username to attach.')
register_cli_argument('vienna computecontext attach', 'password', options_list=('--password','-p'), help='Specifies compute context password to attach.')

register_cli_argument('vienna computecontext detach', 'name', options_list=('--name','-n'), help='Specifies compute context name to detach.')

# register_extra_cli_argument('vienna computecontext listc', 'arguments', options_list=('--arguments','-a'), nargs=argparse.REMAINDER, help="List of things that don't need parsing." )
# register_cli_argument('vienna computecontext listc', 'xtra', options_list=('--xtra','-x'), help="List of things that don't need parsing." )

