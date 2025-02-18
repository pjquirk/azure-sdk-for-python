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


class Usage(Model):
    """Describes Storage Resource Usage.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar unit: Gets the unit of measurement. Possible values include:
     'Count', 'Bytes', 'Seconds', 'Percent', 'CountsPerSecond',
     'BytesPerSecond'
    :vartype unit: str or ~azure.mgmt.storage.v2019_04_01.models.UsageUnit
    :ivar current_value: Gets the current count of the allocated resources in
     the subscription.
    :vartype current_value: int
    :ivar limit: Gets the maximum count of the resources that can be allocated
     in the subscription.
    :vartype limit: int
    :ivar name: Gets the name of the type of usage.
    :vartype name: ~azure.mgmt.storage.v2019_04_01.models.UsageName
    """

    _validation = {
        'unit': {'readonly': True},
        'current_value': {'readonly': True},
        'limit': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'UsageUnit'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(self, **kwargs) -> None:
        super(Usage, self).__init__(**kwargs)
        self.unit = None
        self.current_value = None
        self.limit = None
        self.name = None
