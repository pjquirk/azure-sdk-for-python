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

from .azure_entity_resource import AzureEntityResource


class ListContainerItem(AzureEntityResource):
    """The blob container properties be listed out.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    :param public_access: Specifies whether data in the container may be
     accessed publicly and the level of access. Possible values include:
     'Container', 'Blob', 'None'
    :type public_access: str or
     ~azure.mgmt.storage.v2019_04_01.models.PublicAccess
    :ivar last_modified_time: Returns the date and time the container was last
     modified.
    :vartype last_modified_time: datetime
    :ivar lease_status: The lease status of the container. Possible values
     include: 'Locked', 'Unlocked'
    :vartype lease_status: str or
     ~azure.mgmt.storage.v2019_04_01.models.LeaseStatus
    :ivar lease_state: Lease state of the container. Possible values include:
     'Available', 'Leased', 'Expired', 'Breaking', 'Broken'
    :vartype lease_state: str or
     ~azure.mgmt.storage.v2019_04_01.models.LeaseState
    :ivar lease_duration: Specifies whether the lease on a container is of
     infinite or fixed duration, only when the container is leased. Possible
     values include: 'Infinite', 'Fixed'
    :vartype lease_duration: str or
     ~azure.mgmt.storage.v2019_04_01.models.LeaseDuration
    :param metadata: A name-value pair to associate with the container as
     metadata.
    :type metadata: dict[str, str]
    :ivar immutability_policy: The ImmutabilityPolicy property of the
     container.
    :vartype immutability_policy:
     ~azure.mgmt.storage.v2019_04_01.models.ImmutabilityPolicyProperties
    :ivar legal_hold: The LegalHold property of the container.
    :vartype legal_hold:
     ~azure.mgmt.storage.v2019_04_01.models.LegalHoldProperties
    :ivar has_legal_hold: The hasLegalHold public property is set to true by
     SRP if there are at least one existing tag. The hasLegalHold public
     property is set to false by SRP if all existing legal hold tags are
     cleared out. There can be a maximum of 1000 blob containers with
     hasLegalHold=true for a given account.
    :vartype has_legal_hold: bool
    :ivar has_immutability_policy: The hasImmutabilityPolicy public property
     is set to true by SRP if ImmutabilityPolicy has been created for this
     container. The hasImmutabilityPolicy public property is set to false by
     SRP if ImmutabilityPolicy has not been created for this container.
    :vartype has_immutability_policy: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'lease_status': {'readonly': True},
        'lease_state': {'readonly': True},
        'lease_duration': {'readonly': True},
        'immutability_policy': {'readonly': True},
        'legal_hold': {'readonly': True},
        'has_legal_hold': {'readonly': True},
        'has_immutability_policy': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'public_access': {'key': 'properties.publicAccess', 'type': 'PublicAccess'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'lease_status': {'key': 'properties.leaseStatus', 'type': 'str'},
        'lease_state': {'key': 'properties.leaseState', 'type': 'str'},
        'lease_duration': {'key': 'properties.leaseDuration', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': '{str}'},
        'immutability_policy': {'key': 'properties.immutabilityPolicy', 'type': 'ImmutabilityPolicyProperties'},
        'legal_hold': {'key': 'properties.legalHold', 'type': 'LegalHoldProperties'},
        'has_legal_hold': {'key': 'properties.hasLegalHold', 'type': 'bool'},
        'has_immutability_policy': {'key': 'properties.hasImmutabilityPolicy', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ListContainerItem, self).__init__(**kwargs)
        self.public_access = kwargs.get('public_access', None)
        self.last_modified_time = None
        self.lease_status = None
        self.lease_state = None
        self.lease_duration = None
        self.metadata = kwargs.get('metadata', None)
        self.immutability_policy = None
        self.legal_hold = None
        self.has_legal_hold = None
        self.has_immutability_policy = None
