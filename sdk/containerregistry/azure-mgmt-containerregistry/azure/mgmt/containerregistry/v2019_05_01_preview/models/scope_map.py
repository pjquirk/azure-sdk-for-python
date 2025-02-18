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

from .proxy_resource import ProxyResource


class ScopeMap(ProxyResource):
    """An object that represents a scope map for a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param description: The user friendly description of the scope map.
    :type description: str
    :ivar scope_map_type: The type of the scope map. E.g. BuildIn scope map.
    :vartype scope_map_type: str
    :ivar creation_date: The creation date of scope map.
    :vartype creation_date: datetime
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Creating', 'Updating', 'Deleting', 'Succeeded', 'Failed',
     'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.ProvisioningState
    :param actions: Required. The list of scoped permissions for registry
     artifacts.
     E.g. repositories/repository-name/pull,
     repositories/repository-name/delete
    :type actions: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'scope_map_type': {'readonly': True},
        'creation_date': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'actions': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'scope_map_type': {'key': 'properties.type', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'actions': {'key': 'properties.actions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ScopeMap, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.scope_map_type = None
        self.creation_date = None
        self.provisioning_state = None
        self.actions = kwargs.get('actions', None)
