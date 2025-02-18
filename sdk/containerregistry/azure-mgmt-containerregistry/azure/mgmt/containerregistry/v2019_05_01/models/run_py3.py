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

from .proxy_resource_py3 import ProxyResource


class Run(ProxyResource):
    """Run resource properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param run_id: The unique identifier for the run.
    :type run_id: str
    :param status: The current status of the run. Possible values include:
     'Queued', 'Started', 'Running', 'Succeeded', 'Failed', 'Canceled',
     'Error', 'Timeout'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_05_01.models.RunStatus
    :param last_updated_time: The last updated time for the run.
    :type last_updated_time: datetime
    :param run_type: The type of run. Possible values include: 'QuickBuild',
     'QuickRun', 'AutoBuild', 'AutoRun'
    :type run_type: str or
     ~azure.mgmt.containerregistry.v2019_05_01.models.RunType
    :param create_time: The time the run was scheduled.
    :type create_time: datetime
    :param start_time: The time the run started.
    :type start_time: datetime
    :param finish_time: The time the run finished.
    :type finish_time: datetime
    :param output_images: The list of all images that were generated from the
     run. This is applicable if the run generates base image dependencies.
    :type output_images:
     list[~azure.mgmt.containerregistry.v2019_05_01.models.ImageDescriptor]
    :param task: The task against which run was scheduled.
    :type task: str
    :param image_update_trigger: The image update trigger that caused the run.
     This is applicable if the task has base image trigger configured.
    :type image_update_trigger:
     ~azure.mgmt.containerregistry.v2019_05_01.models.ImageUpdateTrigger
    :param source_trigger: The source trigger that caused the run.
    :type source_trigger:
     ~azure.mgmt.containerregistry.v2019_05_01.models.SourceTriggerDescriptor
    :param platform: The platform properties against which the run will
     happen.
    :type platform:
     ~azure.mgmt.containerregistry.v2019_05_01.models.PlatformProperties
    :param agent_configuration: The machine configuration of the run agent.
    :type agent_configuration:
     ~azure.mgmt.containerregistry.v2019_05_01.models.AgentProperties
    :param source_registry_auth: The scope of the credentials that were used
     to login to the source registry during this run.
    :type source_registry_auth: str
    :param custom_registries: The list of custom registries that were logged
     in during this run.
    :type custom_registries: list[str]
    :ivar run_error_message: The error message received from backend systems
     after the run is scheduled.
    :vartype run_error_message: str
    :param provisioning_state: The provisioning state of a run. Possible
     values include: 'Creating', 'Updating', 'Deleting', 'Succeeded', 'Failed',
     'Canceled'
    :type provisioning_state: str or
     ~azure.mgmt.containerregistry.v2019_05_01.models.ProvisioningState
    :param is_archive_enabled: The value that indicates whether archiving is
     enabled or not. Default value: False .
    :type is_archive_enabled: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'run_error_message': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'run_id': {'key': 'properties.runId', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'last_updated_time': {'key': 'properties.lastUpdatedTime', 'type': 'iso-8601'},
        'run_type': {'key': 'properties.runType', 'type': 'str'},
        'create_time': {'key': 'properties.createTime', 'type': 'iso-8601'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'finish_time': {'key': 'properties.finishTime', 'type': 'iso-8601'},
        'output_images': {'key': 'properties.outputImages', 'type': '[ImageDescriptor]'},
        'task': {'key': 'properties.task', 'type': 'str'},
        'image_update_trigger': {'key': 'properties.imageUpdateTrigger', 'type': 'ImageUpdateTrigger'},
        'source_trigger': {'key': 'properties.sourceTrigger', 'type': 'SourceTriggerDescriptor'},
        'platform': {'key': 'properties.platform', 'type': 'PlatformProperties'},
        'agent_configuration': {'key': 'properties.agentConfiguration', 'type': 'AgentProperties'},
        'source_registry_auth': {'key': 'properties.sourceRegistryAuth', 'type': 'str'},
        'custom_registries': {'key': 'properties.customRegistries', 'type': '[str]'},
        'run_error_message': {'key': 'properties.runErrorMessage', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'is_archive_enabled': {'key': 'properties.isArchiveEnabled', 'type': 'bool'},
    }

    def __init__(self, *, run_id: str=None, status=None, last_updated_time=None, run_type=None, create_time=None, start_time=None, finish_time=None, output_images=None, task: str=None, image_update_trigger=None, source_trigger=None, platform=None, agent_configuration=None, source_registry_auth: str=None, custom_registries=None, provisioning_state=None, is_archive_enabled: bool=False, **kwargs) -> None:
        super(Run, self).__init__(**kwargs)
        self.run_id = run_id
        self.status = status
        self.last_updated_time = last_updated_time
        self.run_type = run_type
        self.create_time = create_time
        self.start_time = start_time
        self.finish_time = finish_time
        self.output_images = output_images
        self.task = task
        self.image_update_trigger = image_update_trigger
        self.source_trigger = source_trigger
        self.platform = platform
        self.agent_configuration = agent_configuration
        self.source_registry_auth = source_registry_auth
        self.custom_registries = custom_registries
        self.run_error_message = None
        self.provisioning_state = provisioning_state
        self.is_archive_enabled = is_archive_enabled
