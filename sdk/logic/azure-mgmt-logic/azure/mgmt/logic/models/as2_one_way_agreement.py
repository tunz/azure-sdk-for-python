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


class AS2OneWayAgreement(Model):
    """The integration account AS2 one-way agreement.

    All required parameters must be populated in order to send to Azure.

    :param sender_business_identity: Required. The sender business identity
    :type sender_business_identity: ~azure.mgmt.logic.models.BusinessIdentity
    :param receiver_business_identity: Required. The receiver business
     identity
    :type receiver_business_identity:
     ~azure.mgmt.logic.models.BusinessIdentity
    :param protocol_settings: Required. The AS2 protocol settings.
    :type protocol_settings: ~azure.mgmt.logic.models.AS2ProtocolSettings
    """

    _validation = {
        'sender_business_identity': {'required': True},
        'receiver_business_identity': {'required': True},
        'protocol_settings': {'required': True},
    }

    _attribute_map = {
        'sender_business_identity': {'key': 'senderBusinessIdentity', 'type': 'BusinessIdentity'},
        'receiver_business_identity': {'key': 'receiverBusinessIdentity', 'type': 'BusinessIdentity'},
        'protocol_settings': {'key': 'protocolSettings', 'type': 'AS2ProtocolSettings'},
    }

    def __init__(self, **kwargs):
        super(AS2OneWayAgreement, self).__init__(**kwargs)
        self.sender_business_identity = kwargs.get('sender_business_identity', None)
        self.receiver_business_identity = kwargs.get('receiver_business_identity', None)
        self.protocol_settings = kwargs.get('protocol_settings', None)
