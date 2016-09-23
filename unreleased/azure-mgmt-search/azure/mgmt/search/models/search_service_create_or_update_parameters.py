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


class SearchServiceCreateOrUpdateParameters(Model):
    """Properties that describe an Azure Search service.

    :param location: The geographic location of the Search service.
    :type location: str
    :param tags: Tags to help categorize the Search service in the Azure
     Portal.
    :type tags: dict
    :param properties: Properties of the Search service.
    :type properties: :class:`SearchServiceProperties
     <azure.mgmt.search.models.SearchServiceProperties>`
    """ 

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'SearchServiceProperties'},
    }

    def __init__(self, location=None, tags=None, properties=None):
        self.location = location
        self.tags = tags
        self.properties = properties