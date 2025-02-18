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
from .operations.registries_operations import RegistriesOperations
from .operations.operations import Operations
from .operations.replications_operations import ReplicationsOperations
from .operations.webhooks_operations import WebhooksOperations
from .operations.scope_maps_operations import ScopeMapsOperations
from .operations.tokens_operations import TokensOperations
from . import models


class ContainerRegistryManagementClientConfiguration(AzureConfiguration):
    """Configuration for ContainerRegistryManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
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

        super(ContainerRegistryManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-containerregistry/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ContainerRegistryManagementClient(SDKClient):
    """ContainerRegistryManagementClient

    :ivar config: Configuration for client.
    :vartype config: ContainerRegistryManagementClientConfiguration

    :ivar registries: Registries operations
    :vartype registries: azure.mgmt.containerregistry.v2019_05_01_preview.operations.RegistriesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerregistry.v2019_05_01_preview.operations.Operations
    :ivar replications: Replications operations
    :vartype replications: azure.mgmt.containerregistry.v2019_05_01_preview.operations.ReplicationsOperations
    :ivar webhooks: Webhooks operations
    :vartype webhooks: azure.mgmt.containerregistry.v2019_05_01_preview.operations.WebhooksOperations
    :ivar scope_maps: ScopeMaps operations
    :vartype scope_maps: azure.mgmt.containerregistry.v2019_05_01_preview.operations.ScopeMapsOperations
    :ivar tokens: Tokens operations
    :vartype tokens: azure.mgmt.containerregistry.v2019_05_01_preview.operations.TokensOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ContainerRegistryManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ContainerRegistryManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.registries = RegistriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.replications = ReplicationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.webhooks = WebhooksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scope_maps = ScopeMapsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tokens = TokensOperations(
            self._client, self.config, self._serialize, self._deserialize)
