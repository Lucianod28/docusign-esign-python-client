# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class BulkSendEnvelopesInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'authoritative_copy': 'str',
        'completed': 'str',
        'correct': 'str',
        'created': 'str',
        'declined': 'str',
        'deleted': 'str',
        'delivered': 'str',
        'digital_signatures_pending': 'str',
        'sent': 'str',
        'signed': 'str',
        'timed_out': 'str',
        'transfer_completed': 'str',
        'voided': 'str'
    }

    attribute_map = {
        'authoritative_copy': 'authoritativeCopy',
        'completed': 'completed',
        'correct': 'correct',
        'created': 'created',
        'declined': 'declined',
        'deleted': 'deleted',
        'delivered': 'delivered',
        'digital_signatures_pending': 'digitalSignaturesPending',
        'sent': 'sent',
        'signed': 'signed',
        'timed_out': 'timedOut',
        'transfer_completed': 'transferCompleted',
        'voided': 'voided'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendEnvelopesInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authoritative_copy = None
        self._completed = None
        self._correct = None
        self._created = None
        self._declined = None
        self._deleted = None
        self._delivered = None
        self._digital_signatures_pending = None
        self._sent = None
        self._signed = None
        self._timed_out = None
        self._transfer_completed = None
        self._voided = None
        self.discriminator = None

        setattr(self, "_{}".format('authoritative_copy'), kwargs.get('authoritative_copy', None))
        setattr(self, "_{}".format('completed'), kwargs.get('completed', None))
        setattr(self, "_{}".format('correct'), kwargs.get('correct', None))
        setattr(self, "_{}".format('created'), kwargs.get('created', None))
        setattr(self, "_{}".format('declined'), kwargs.get('declined', None))
        setattr(self, "_{}".format('deleted'), kwargs.get('deleted', None))
        setattr(self, "_{}".format('delivered'), kwargs.get('delivered', None))
        setattr(self, "_{}".format('digital_signatures_pending'), kwargs.get('digital_signatures_pending', None))
        setattr(self, "_{}".format('sent'), kwargs.get('sent', None))
        setattr(self, "_{}".format('signed'), kwargs.get('signed', None))
        setattr(self, "_{}".format('timed_out'), kwargs.get('timed_out', None))
        setattr(self, "_{}".format('transfer_completed'), kwargs.get('transfer_completed', None))
        setattr(self, "_{}".format('voided'), kwargs.get('voided', None))

    @property
    def authoritative_copy(self):
        """Gets the authoritative_copy of this BulkSendEnvelopesInfo.  # noqa: E501

        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.  # noqa: E501

        :return: The authoritative_copy of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._authoritative_copy

    @authoritative_copy.setter
    def authoritative_copy(self, authoritative_copy):
        """Sets the authoritative_copy of this BulkSendEnvelopesInfo.

        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.  # noqa: E501

        :param authoritative_copy: The authoritative_copy of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._authoritative_copy = authoritative_copy

    @property
    def completed(self):
        """Gets the completed of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The completed of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param completed: The completed of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._completed = completed

    @property
    def correct(self):
        """Gets the correct of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The correct of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._correct

    @correct.setter
    def correct(self, correct):
        """Sets the correct of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param correct: The correct of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._correct = correct

    @property
    def created(self):
        """Gets the created of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The created of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param created: The created of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def declined(self):
        """Gets the declined of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The declined of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._declined

    @declined.setter
    def declined(self, declined):
        """Sets the declined of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param declined: The declined of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._declined = declined

    @property
    def deleted(self):
        """Gets the deleted of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The deleted of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param deleted: The deleted of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._deleted = deleted

    @property
    def delivered(self):
        """Gets the delivered of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The delivered of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param delivered: The delivered of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._delivered = delivered

    @property
    def digital_signatures_pending(self):
        """Gets the digital_signatures_pending of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The digital_signatures_pending of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._digital_signatures_pending

    @digital_signatures_pending.setter
    def digital_signatures_pending(self, digital_signatures_pending):
        """Sets the digital_signatures_pending of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param digital_signatures_pending: The digital_signatures_pending of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._digital_signatures_pending = digital_signatures_pending

    @property
    def sent(self):
        """Gets the sent of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The sent of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param sent: The sent of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._sent = sent

    @property
    def signed(self):
        """Gets the signed of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The signed of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        """Sets the signed of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param signed: The signed of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._signed = signed

    @property
    def timed_out(self):
        """Gets the timed_out of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The timed_out of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._timed_out

    @timed_out.setter
    def timed_out(self, timed_out):
        """Sets the timed_out of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param timed_out: The timed_out of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._timed_out = timed_out

    @property
    def transfer_completed(self):
        """Gets the transfer_completed of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The transfer_completed of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._transfer_completed

    @transfer_completed.setter
    def transfer_completed(self, transfer_completed):
        """Sets the transfer_completed of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param transfer_completed: The transfer_completed of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._transfer_completed = transfer_completed

    @property
    def voided(self):
        """Gets the voided of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The voided of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._voided

    @voided.setter
    def voided(self, voided):
        """Sets the voided of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param voided: The voided of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._voided = voided

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BulkSendEnvelopesInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkSendEnvelopesInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendEnvelopesInfo):
            return True

        return self.to_dict() != other.to_dict()