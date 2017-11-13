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


class FactoryUpdateParameters(Model):
    """Parameters for updating a factory resource.

    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param identity: Managed service identity of the factory.
    :type identity: ~azure.mgmt.datafactory.models.FactoryIdentity
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'FactoryIdentity'},
    }

    def __init__(self, tags=None, identity=None):
        self.tags = tags
        self.identity = identity
