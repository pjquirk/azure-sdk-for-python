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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.skus_operations import SkusOperations
from .operations.storage_accounts_operations import StorageAccountsOperations
from .operations.usages_operations import UsagesOperations
from .operations.management_policies_operations import ManagementPoliciesOperations
from .operations.blob_services_operations import BlobServicesOperations
from .operations.blob_containers_operations import BlobContainersOperations
from . import models


class StorageManagementClientConfiguration(AzureConfiguration):
    """Configuration for StorageManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(StorageManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-storage/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class StorageManagementClient(SDKClient):
    """The Azure Storage Management API.

    :ivar config: Configuration for client.
    :vartype config: StorageManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2019_04_01.operations.Operations
    :ivar skus: Skus operations
    :vartype skus: azure.mgmt.storage.v2019_04_01.operations.SkusOperations
    :ivar storage_accounts: StorageAccounts operations
    :vartype storage_accounts: azure.mgmt.storage.v2019_04_01.operations.StorageAccountsOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.storage.v2019_04_01.operations.UsagesOperations
    :ivar management_policies: ManagementPolicies operations
    :vartype management_policies: azure.mgmt.storage.v2019_04_01.operations.ManagementPoliciesOperations
    :ivar blob_services: BlobServices operations
    :vartype blob_services: azure.mgmt.storage.v2019_04_01.operations.BlobServicesOperations
    :ivar blob_containers: BlobContainers operations
    :vartype blob_containers: azure.mgmt.storage.v2019_04_01.operations.BlobContainersOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = StorageManagementClientConfiguration(credentials, subscription_id, base_url)
        super(StorageManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.management_policies = ManagementPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.blob_services = BlobServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
