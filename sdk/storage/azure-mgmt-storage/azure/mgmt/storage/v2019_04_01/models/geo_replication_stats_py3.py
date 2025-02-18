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


class GeoReplicationStats(Model):
    """Statistics related to replication for storage account's Blob, Table, Queue
    and File services. It is only available when geo-redundant replication is
    enabled for the storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar status: The status of the secondary location. Possible values are: -
     Live: Indicates that the secondary location is active and operational. -
     Bootstrap: Indicates initial synchronization from the primary location to
     the secondary location is in progress.This typically occurs when
     replication is first enabled. - Unavailable: Indicates that the secondary
     location is temporarily unavailable. Possible values include: 'Live',
     'Bootstrap', 'Unavailable'
    :vartype status: str or
     ~azure.mgmt.storage.v2019_04_01.models.GeoReplicationStatus
    :ivar last_sync_time: All primary writes preceding this UTC date/time
     value are guaranteed to be available for read operations. Primary writes
     following this point in time may or may not be available for reads.
     Element may be default value if value of LastSyncTime is not available,
     this can happen if secondary is offline or we are in bootstrap.
    :vartype last_sync_time: datetime
    :ivar can_failover: A boolean flag which indicates whether or not account
     failover is supported for the account.
    :vartype can_failover: bool
    """

    _validation = {
        'status': {'readonly': True},
        'last_sync_time': {'readonly': True},
        'can_failover': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'last_sync_time': {'key': 'lastSyncTime', 'type': 'iso-8601'},
        'can_failover': {'key': 'canFailover', 'type': 'bool'},
    }

    def __init__(self, **kwargs) -> None:
        super(GeoReplicationStats, self).__init__(**kwargs)
        self.status = None
        self.last_sync_time = None
        self.can_failover = None
