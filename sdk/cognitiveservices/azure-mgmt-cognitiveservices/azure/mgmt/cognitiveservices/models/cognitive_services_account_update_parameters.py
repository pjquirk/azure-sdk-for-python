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


class CognitiveServicesAccountUpdateParameters(Model):
    """The parameters to provide for the account.

    :param sku: Gets or sets the SKU of the resource.
    :type sku: ~azure.mgmt.cognitiveservices.models.Sku
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    :param properties: Additional properties for Account. Only provided fields
     will be updated.
    :type properties: object
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(CognitiveServicesAccountUpdateParameters, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)
