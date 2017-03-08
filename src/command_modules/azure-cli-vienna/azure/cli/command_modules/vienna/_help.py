# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.help_files import helps  # pylint: disable=unused-import

helps['vienna'] = """
    type: command
    short-summary: Access Vienna commands (needs Vienna installed).
"""
helps['vienna computecontext'] = """
    type: command
    short-summary: Access compute context related commands within Vienna.
"""

helps['vienna computecontext attach'] = """
    type: command
    short-summary: Attach a compute context.
"""

helps['vienna computecontext detach'] = """
    type: command
    short-summary: Detacha compute context.
"""