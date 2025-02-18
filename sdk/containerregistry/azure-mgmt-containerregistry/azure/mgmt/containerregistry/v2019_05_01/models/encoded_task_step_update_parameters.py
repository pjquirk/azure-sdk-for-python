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

from .task_step_update_parameters import TaskStepUpdateParameters


class EncodedTaskStepUpdateParameters(TaskStepUpdateParameters):
    """The properties for updating encoded task step.

    All required parameters must be populated in order to send to Azure.

    :param context_path: The URL(absolute or relative) of the source context
     for the task step.
    :type context_path: str
    :param context_access_token: The token (git PAT or SAS token of storage
     account blob) associated with the context for a step.
    :type context_access_token: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param encoded_task_content: Base64 encoded value of the
     template/definition file content.
    :type encoded_task_content: str
    :param encoded_values_content: Base64 encoded value of the
     parameters/values file content.
    :type encoded_values_content: str
    :param values: The collection of overridable values that can be passed
     when running a task.
    :type values:
     list[~azure.mgmt.containerregistry.v2019_05_01.models.SetValue]
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'context_path': {'key': 'contextPath', 'type': 'str'},
        'context_access_token': {'key': 'contextAccessToken', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'encoded_task_content': {'key': 'encodedTaskContent', 'type': 'str'},
        'encoded_values_content': {'key': 'encodedValuesContent', 'type': 'str'},
        'values': {'key': 'values', 'type': '[SetValue]'},
    }

    def __init__(self, **kwargs):
        super(EncodedTaskStepUpdateParameters, self).__init__(**kwargs)
        self.encoded_task_content = kwargs.get('encoded_task_content', None)
        self.encoded_values_content = kwargs.get('encoded_values_content', None)
        self.values = kwargs.get('values', None)
        self.type = 'EncodedTask'
