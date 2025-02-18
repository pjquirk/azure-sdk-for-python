# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IPRule(Model):
    """A rule governing the accessibility of a vault from a specific ip address or
    ip range.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. An IPv4 address range in CIDR notation, such as
     '124.56.78.91' (simple IP address) or '124.56.78.0/24' (all addresses that
     start with 124.56.78).
    :type value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IPRule, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
