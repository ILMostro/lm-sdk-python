# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.ops_note_scope import OpsNoteScope  # noqa: F401,E501
from logicmonitor_sdk.models.ops_note_tag_base import OpsNoteTagBase  # noqa: F401,E501


class OpsNote(object):
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
        'created_by': 'str',
        'happen_on_in_sec': 'int',
        'id': 'str',
        'note': 'str',
        'scopes': 'list[OpsNoteScope]',
        'tags': 'list[OpsNoteTagBase]'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'happen_on_in_sec': 'happenOnInSec',
        'id': 'id',
        'note': 'note',
        'scopes': 'scopes',
        'tags': 'tags'
    }

    def __init__(self, created_by=None, happen_on_in_sec=None, id=None, note=None, scopes=None, tags=None):  # noqa: E501
        """OpsNote - a model defined in Swagger"""  # noqa: E501

        self._created_by = None
        self._happen_on_in_sec = None
        self._id = None
        self._note = None
        self._scopes = None
        self._tags = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if happen_on_in_sec is not None:
            self.happen_on_in_sec = happen_on_in_sec
        if id is not None:
            self.id = id
        self.note = note
        if scopes is not None:
            self.scopes = scopes
        if tags is not None:
            self.tags = tags

    @property
    def created_by(self):
        """Gets the created_by of this OpsNote.  # noqa: E501

        The user that created the Ops Note  # noqa: E501

        :return: The created_by of this OpsNote.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OpsNote.

        The user that created the Ops Note  # noqa: E501

        :param created_by: The created_by of this OpsNote.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def happen_on_in_sec(self):
        """Gets the happen_on_in_sec of this OpsNote.  # noqa: E501

        The date and time associated with the note, in epoch seconds format  # noqa: E501

        :return: The happen_on_in_sec of this OpsNote.  # noqa: E501
        :rtype: int
        """
        return self._happen_on_in_sec

    @happen_on_in_sec.setter
    def happen_on_in_sec(self, happen_on_in_sec):
        """Sets the happen_on_in_sec of this OpsNote.

        The date and time associated with the note, in epoch seconds format  # noqa: E501

        :param happen_on_in_sec: The happen_on_in_sec of this OpsNote.  # noqa: E501
        :type: int
        """

        self._happen_on_in_sec = happen_on_in_sec

    @property
    def id(self):
        """Gets the id of this OpsNote.  # noqa: E501

        The id associated with the Ops Note  # noqa: E501

        :return: The id of this OpsNote.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OpsNote.

        The id associated with the Ops Note  # noqa: E501

        :param id: The id of this OpsNote.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def note(self):
        """Gets the note of this OpsNote.  # noqa: E501

        The note message  # noqa: E501

        :return: The note of this OpsNote.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this OpsNote.

        The note message  # noqa: E501

        :param note: The note of this OpsNote.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def scopes(self):
        """Gets the scopes of this OpsNote.  # noqa: E501

        The scopes associated with the note. Each scope has a type of device, service, deviceGroup or serviceGroup. A note with no scope will show up for everything in the account  # noqa: E501

        :return: The scopes of this OpsNote.  # noqa: E501
        :rtype: list[OpsNoteScope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this OpsNote.

        The scopes associated with the note. Each scope has a type of device, service, deviceGroup or serviceGroup. A note with no scope will show up for everything in the account  # noqa: E501

        :param scopes: The scopes of this OpsNote.  # noqa: E501
        :type: list[OpsNoteScope]
        """

        self._scopes = scopes

    @property
    def tags(self):
        """Gets the tags of this OpsNote.  # noqa: E501

        The tags that should be associated with the note. Each tag has a unique id and a name - you can either include the name of a new or existing tag, or the id of an existing tag  # noqa: E501

        :return: The tags of this OpsNote.  # noqa: E501
        :rtype: list[OpsNoteTagBase]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this OpsNote.

        The tags that should be associated with the note. Each tag has a unique id and a name - you can either include the name of a new or existing tag, or the id of an existing tag  # noqa: E501

        :param tags: The tags of this OpsNote.  # noqa: E501
        :type: list[OpsNoteTagBase]
        """

        self._tags = tags

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
        if issubclass(OpsNote, dict):
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
        if not isinstance(other, OpsNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other