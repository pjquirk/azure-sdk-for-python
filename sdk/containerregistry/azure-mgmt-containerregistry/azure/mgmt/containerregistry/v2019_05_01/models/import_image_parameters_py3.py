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


class ImportImageParameters(Model):
    """ImportImageParameters.

    All required parameters must be populated in order to send to Azure.

    :param source: Required. The source of the image.
    :type source:
     ~azure.mgmt.containerregistry.v2019_05_01.models.ImportSource
    :param target_tags: List of strings of the form repo[:tag]. When tag is
     omitted the source will be used (or 'latest' if source tag is also
     omitted).
    :type target_tags: list[str]
    :param untagged_target_repositories: List of strings of repository names
     to do a manifest only copy. No tag will be created.
    :type untagged_target_repositories: list[str]
    :param mode: When Force, any existing target tags will be overwritten.
     When NoForce, any existing target tags will fail the operation before any
     copying begins. Possible values include: 'NoForce', 'Force'. Default
     value: "NoForce" .
    :type mode: str or
     ~azure.mgmt.containerregistry.v2019_05_01.models.ImportMode
    """

    _validation = {
        'source': {'required': True},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'ImportSource'},
        'target_tags': {'key': 'targetTags', 'type': '[str]'},
        'untagged_target_repositories': {'key': 'untaggedTargetRepositories', 'type': '[str]'},
        'mode': {'key': 'mode', 'type': 'str'},
    }

    def __init__(self, *, source, target_tags=None, untagged_target_repositories=None, mode="NoForce", **kwargs) -> None:
        super(ImportImageParameters, self).__init__(**kwargs)
        self.source = source
        self.target_tags = target_tags
        self.untagged_target_repositories = untagged_target_repositories
        self.mode = mode
