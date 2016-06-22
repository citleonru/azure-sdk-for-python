# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeepCreatedOrigin(Model):
    """Deep created origins within a CDN endpoint.

    :param name: Origin name
    :type name: str
    :param host_name: The address of the origin. Domain names, IPv4
     addresses, and IPv6 addresses are supported.
    :type host_name: str
    :param http_port: The value of the HTTP port. Must be between 1 and 65535
    :type http_port: int
    :param https_port: The value of the HTTPS port. Must be between 1 and
     65535
    :type https_port: int
    """ 

    _validation = {
        'name': {'required': True},
        'host_name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'http_port': {'key': 'properties.httpPort', 'type': 'int'},
        'https_port': {'key': 'properties.httpsPort', 'type': 'int'},
    }

    def __init__(self, name, host_name, http_port=None, https_port=None):
        self.name = name
        self.host_name = host_name
        self.http_port = http_port
        self.https_port = https_port