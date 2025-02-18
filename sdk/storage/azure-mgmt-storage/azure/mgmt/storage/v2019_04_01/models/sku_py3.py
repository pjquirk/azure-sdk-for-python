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


class Sku(Model):
    """The SKU of the storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Gets or sets the SKU name. Required for account
     creation; optional for update. Note that in older versions, SKU name was
     called accountType. Possible values include: 'Standard_LRS',
     'Standard_GRS', 'Standard_RAGRS', 'Standard_ZRS', 'Premium_LRS',
     'Premium_ZRS', 'Standard_GZRS', 'Standard_RAGZRS'
    :type name: str or ~azure.mgmt.storage.v2019_04_01.models.SkuName
    :ivar tier: Gets the SKU tier. This is based on the SKU name. Possible
     values include: 'Standard', 'Premium'
    :vartype tier: str or ~azure.mgmt.storage.v2019_04_01.models.SkuTier
    :ivar resource_type: The type of the resource, usually it is
     'storageAccounts'.
    :vartype resource_type: str
    :ivar kind: Indicates the type of storage account. Possible values
     include: 'Storage', 'StorageV2', 'BlobStorage', 'FileStorage',
     'BlockBlobStorage'
    :vartype kind: str or ~azure.mgmt.storage.v2019_04_01.models.Kind
    :ivar locations: The set of locations that the SKU is available. This will
     be supported and registered Azure Geo Regions (e.g. West US, East US,
     Southeast Asia, etc.).
    :vartype locations: list[str]
    :ivar capabilities: The capability information in the specified SKU,
     including file encryption, network ACLs, change notification, etc.
    :vartype capabilities:
     list[~azure.mgmt.storage.v2019_04_01.models.SKUCapability]
    :param restrictions: The restrictions because of which SKU cannot be used.
     This is empty if there are no restrictions.
    :type restrictions:
     list[~azure.mgmt.storage.v2019_04_01.models.Restriction]
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
        'resource_type': {'readonly': True},
        'kind': {'readonly': True},
        'locations': {'readonly': True},
        'capabilities': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'SkuTier'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'capabilities': {'key': 'capabilities', 'type': '[SKUCapability]'},
        'restrictions': {'key': 'restrictions', 'type': '[Restriction]'},
    }

    def __init__(self, *, name, restrictions=None, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = None
        self.resource_type = None
        self.kind = None
        self.locations = None
        self.capabilities = None
        self.restrictions = restrictions
