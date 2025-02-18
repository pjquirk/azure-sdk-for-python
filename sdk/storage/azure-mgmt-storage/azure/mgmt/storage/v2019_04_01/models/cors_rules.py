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


class CorsRules(Model):
    """Sets the CORS rules. You can include up to five CorsRule elements in the
    request. .

    :param cors_rules: The List of CORS rules. You can include up to five
     CorsRule elements in the request.
    :type cors_rules: list[~azure.mgmt.storage.v2019_04_01.models.CorsRule]
    """

    _attribute_map = {
        'cors_rules': {'key': 'corsRules', 'type': '[CorsRule]'},
    }

    def __init__(self, **kwargs):
        super(CorsRules, self).__init__(**kwargs)
        self.cors_rules = kwargs.get('cors_rules', None)
