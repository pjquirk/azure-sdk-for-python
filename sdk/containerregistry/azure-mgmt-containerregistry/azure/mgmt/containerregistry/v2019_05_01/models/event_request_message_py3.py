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


class EventRequestMessage(Model):
    """The event request message sent to the service URI.

    :param content: The content of the event request message.
    :type content:
     ~azure.mgmt.containerregistry.v2019_05_01.models.EventContent
    :param headers: The headers of the event request message.
    :type headers: dict[str, str]
    :param method: The HTTP method used to send the event request message.
    :type method: str
    :param request_uri: The URI used to send the event request message.
    :type request_uri: str
    :param version: The HTTP message version.
    :type version: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'EventContent'},
        'headers': {'key': 'headers', 'type': '{str}'},
        'method': {'key': 'method', 'type': 'str'},
        'request_uri': {'key': 'requestUri', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, *, content=None, headers=None, method: str=None, request_uri: str=None, version: str=None, **kwargs) -> None:
        super(EventRequestMessage, self).__init__(**kwargs)
        self.content = content
        self.headers = headers
        self.method = method
        self.request_uri = request_uri
        self.version = version
