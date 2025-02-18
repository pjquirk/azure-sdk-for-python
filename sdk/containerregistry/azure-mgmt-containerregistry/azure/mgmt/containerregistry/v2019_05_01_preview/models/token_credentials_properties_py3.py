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


class TokenCredentialsProperties(Model):
    """The properties of the credentials that can be used for authenticating the
    token.

    :param certificates:
    :type certificates:
     list[~azure.mgmt.containerregistry.v2019_05_01_preview.models.TokenCertificate]
    :param passwords:
    :type passwords:
     list[~azure.mgmt.containerregistry.v2019_05_01_preview.models.TokenPassword]
    """

    _attribute_map = {
        'certificates': {'key': 'certificates', 'type': '[TokenCertificate]'},
        'passwords': {'key': 'passwords', 'type': '[TokenPassword]'},
    }

    def __init__(self, *, certificates=None, passwords=None, **kwargs) -> None:
        super(TokenCredentialsProperties, self).__init__(**kwargs)
        self.certificates = certificates
        self.passwords = passwords
