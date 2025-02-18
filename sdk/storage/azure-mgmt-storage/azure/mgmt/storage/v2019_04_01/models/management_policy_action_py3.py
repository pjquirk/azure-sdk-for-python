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


class ManagementPolicyAction(Model):
    """Actions are applied to the filtered blobs when the execution condition is
    met.

    :param base_blob: The management policy action for base blob
    :type base_blob:
     ~azure.mgmt.storage.v2019_04_01.models.ManagementPolicyBaseBlob
    :param snapshot: The management policy action for snapshot
    :type snapshot:
     ~azure.mgmt.storage.v2019_04_01.models.ManagementPolicySnapShot
    """

    _attribute_map = {
        'base_blob': {'key': 'baseBlob', 'type': 'ManagementPolicyBaseBlob'},
        'snapshot': {'key': 'snapshot', 'type': 'ManagementPolicySnapShot'},
    }

    def __init__(self, *, base_blob=None, snapshot=None, **kwargs) -> None:
        super(ManagementPolicyAction, self).__init__(**kwargs)
        self.base_blob = base_blob
        self.snapshot = snapshot
