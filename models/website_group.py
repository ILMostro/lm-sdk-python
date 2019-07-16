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

from logicmonitor_sdk.models.name_and_value import NameAndValue  # noqa: F401,E501
from logicmonitor_sdk.models.website_location import WebsiteLocation  # noqa: F401,E501


class WebsiteGroup(object):
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
        'description': 'str',
        'disable_alerting': 'bool',
        'full_path': 'str',
        'has_websites_disabled': 'bool',
        'id': 'int',
        'name': 'str',
        'num_of_direct_sub_groups': 'int',
        'num_of_direct_websites': 'int',
        'num_of_websites': 'int',
        'parent_id': 'int',
        'properties': 'list[NameAndValue]',
        'stop_monitoring': 'bool',
        'test_location': 'WebsiteLocation',
        'user_permission': 'str'
    }

    attribute_map = {
        'description': 'description',
        'disable_alerting': 'disableAlerting',
        'full_path': 'fullPath',
        'has_websites_disabled': 'hasWebsitesDisabled',
        'id': 'id',
        'name': 'name',
        'num_of_direct_sub_groups': 'numOfDirectSubGroups',
        'num_of_direct_websites': 'numOfDirectWebsites',
        'num_of_websites': 'numOfWebsites',
        'parent_id': 'parentId',
        'properties': 'properties',
        'stop_monitoring': 'stopMonitoring',
        'test_location': 'testLocation',
        'user_permission': 'userPermission'
    }

    def __init__(self, description=None, disable_alerting=None, full_path=None, has_websites_disabled=None, id=None, name=None, num_of_direct_sub_groups=None, num_of_direct_websites=None, num_of_websites=None, parent_id=None, properties=None, stop_monitoring=None, test_location=None, user_permission=None):  # noqa: E501
        """WebsiteGroup - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._disable_alerting = None
        self._full_path = None
        self._has_websites_disabled = None
        self._id = None
        self._name = None
        self._num_of_direct_sub_groups = None
        self._num_of_direct_websites = None
        self._num_of_websites = None
        self._parent_id = None
        self._properties = None
        self._stop_monitoring = None
        self._test_location = None
        self._user_permission = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if disable_alerting is not None:
            self.disable_alerting = disable_alerting
        if full_path is not None:
            self.full_path = full_path
        if has_websites_disabled is not None:
            self.has_websites_disabled = has_websites_disabled
        if id is not None:
            self.id = id
        self.name = name
        if num_of_direct_sub_groups is not None:
            self.num_of_direct_sub_groups = num_of_direct_sub_groups
        if num_of_direct_websites is not None:
            self.num_of_direct_websites = num_of_direct_websites
        if num_of_websites is not None:
            self.num_of_websites = num_of_websites
        if parent_id is not None:
            self.parent_id = parent_id
        if properties is not None:
            self.properties = properties
        if stop_monitoring is not None:
            self.stop_monitoring = stop_monitoring
        if test_location is not None:
            self.test_location = test_location
        if user_permission is not None:
            self.user_permission = user_permission

    @property
    def description(self):
        """Gets the description of this WebsiteGroup.  # noqa: E501

        The description of the group  # noqa: E501

        :return: The description of this WebsiteGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebsiteGroup.

        The description of the group  # noqa: E501

        :param description: The description of this WebsiteGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disable_alerting(self):
        """Gets the disable_alerting of this WebsiteGroup.  # noqa: E501

        true: alerting is disabled for the websites in the group false: alerting is enabled for the websites in the group If stopMonitoring=true, then alerting will also by default be disabled for the websites in the group  # noqa: E501

        :return: The disable_alerting of this WebsiteGroup.  # noqa: E501
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """Sets the disable_alerting of this WebsiteGroup.

        true: alerting is disabled for the websites in the group false: alerting is enabled for the websites in the group If stopMonitoring=true, then alerting will also by default be disabled for the websites in the group  # noqa: E501

        :param disable_alerting: The disable_alerting of this WebsiteGroup.  # noqa: E501
        :type: bool
        """

        self._disable_alerting = disable_alerting

    @property
    def full_path(self):
        """Gets the full_path of this WebsiteGroup.  # noqa: E501

        The full path of the group  # noqa: E501

        :return: The full_path of this WebsiteGroup.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this WebsiteGroup.

        The full path of the group  # noqa: E501

        :param full_path: The full_path of this WebsiteGroup.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def has_websites_disabled(self):
        """Gets the has_websites_disabled of this WebsiteGroup.  # noqa: E501


        :return: The has_websites_disabled of this WebsiteGroup.  # noqa: E501
        :rtype: bool
        """
        return self._has_websites_disabled

    @has_websites_disabled.setter
    def has_websites_disabled(self, has_websites_disabled):
        """Sets the has_websites_disabled of this WebsiteGroup.


        :param has_websites_disabled: The has_websites_disabled of this WebsiteGroup.  # noqa: E501
        :type: bool
        """

        self._has_websites_disabled = has_websites_disabled

    @property
    def id(self):
        """Gets the id of this WebsiteGroup.  # noqa: E501

        The Id of the group  # noqa: E501

        :return: The id of this WebsiteGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebsiteGroup.

        The Id of the group  # noqa: E501

        :param id: The id of this WebsiteGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WebsiteGroup.  # noqa: E501

        The name of the group  # noqa: E501

        :return: The name of this WebsiteGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebsiteGroup.

        The name of the group  # noqa: E501

        :param name: The name of this WebsiteGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def num_of_direct_sub_groups(self):
        """Gets the num_of_direct_sub_groups of this WebsiteGroup.  # noqa: E501

        The number of direct website groups in this group (exlcuding those in subgroups)  # noqa: E501

        :return: The num_of_direct_sub_groups of this WebsiteGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_direct_sub_groups

    @num_of_direct_sub_groups.setter
    def num_of_direct_sub_groups(self, num_of_direct_sub_groups):
        """Sets the num_of_direct_sub_groups of this WebsiteGroup.

        The number of direct website groups in this group (exlcuding those in subgroups)  # noqa: E501

        :param num_of_direct_sub_groups: The num_of_direct_sub_groups of this WebsiteGroup.  # noqa: E501
        :type: int
        """

        self._num_of_direct_sub_groups = num_of_direct_sub_groups

    @property
    def num_of_direct_websites(self):
        """Gets the num_of_direct_websites of this WebsiteGroup.  # noqa: E501


        :return: The num_of_direct_websites of this WebsiteGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_direct_websites

    @num_of_direct_websites.setter
    def num_of_direct_websites(self, num_of_direct_websites):
        """Sets the num_of_direct_websites of this WebsiteGroup.


        :param num_of_direct_websites: The num_of_direct_websites of this WebsiteGroup.  # noqa: E501
        :type: int
        """

        self._num_of_direct_websites = num_of_direct_websites

    @property
    def num_of_websites(self):
        """Gets the num_of_websites of this WebsiteGroup.  # noqa: E501


        :return: The num_of_websites of this WebsiteGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_websites

    @num_of_websites.setter
    def num_of_websites(self, num_of_websites):
        """Sets the num_of_websites of this WebsiteGroup.


        :param num_of_websites: The num_of_websites of this WebsiteGroup.  # noqa: E501
        :type: int
        """

        self._num_of_websites = num_of_websites

    @property
    def parent_id(self):
        """Gets the parent_id of this WebsiteGroup.  # noqa: E501

        The Id of the parent group. If parentId=1 then the group exists under the root  group  # noqa: E501

        :return: The parent_id of this WebsiteGroup.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this WebsiteGroup.

        The Id of the parent group. If parentId=1 then the group exists under the root  group  # noqa: E501

        :param parent_id: The parent_id of this WebsiteGroup.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def properties(self):
        """Gets the properties of this WebsiteGroup.  # noqa: E501


        :return: The properties of this WebsiteGroup.  # noqa: E501
        :rtype: list[NameAndValue]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this WebsiteGroup.


        :param properties: The properties of this WebsiteGroup.  # noqa: E501
        :type: list[NameAndValue]
        """

        self._properties = properties

    @property
    def stop_monitoring(self):
        """Gets the stop_monitoring of this WebsiteGroup.  # noqa: E501

        true: monitoring is disabled for the websites in the group false: monitoring is enabled for the websites in the group If stopMonitoring=true, then alerting will also by default be disabled for the websites in the group  # noqa: E501

        :return: The stop_monitoring of this WebsiteGroup.  # noqa: E501
        :rtype: bool
        """
        return self._stop_monitoring

    @stop_monitoring.setter
    def stop_monitoring(self, stop_monitoring):
        """Sets the stop_monitoring of this WebsiteGroup.

        true: monitoring is disabled for the websites in the group false: monitoring is enabled for the websites in the group If stopMonitoring=true, then alerting will also by default be disabled for the websites in the group  # noqa: E501

        :param stop_monitoring: The stop_monitoring of this WebsiteGroup.  # noqa: E501
        :type: bool
        """

        self._stop_monitoring = stop_monitoring

    @property
    def test_location(self):
        """Gets the test_location of this WebsiteGroup.  # noqa: E501


        :return: The test_location of this WebsiteGroup.  # noqa: E501
        :rtype: WebsiteLocation
        """
        return self._test_location

    @test_location.setter
    def test_location(self, test_location):
        """Sets the test_location of this WebsiteGroup.


        :param test_location: The test_location of this WebsiteGroup.  # noqa: E501
        :type: WebsiteLocation
        """

        self._test_location = test_location

    @property
    def user_permission(self):
        """Gets the user_permission of this WebsiteGroup.  # noqa: E501

        The permission level of the user that made the API request. Acceptable values are: write, read, ack  # noqa: E501

        :return: The user_permission of this WebsiteGroup.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this WebsiteGroup.

        The permission level of the user that made the API request. Acceptable values are: write, read, ack  # noqa: E501

        :param user_permission: The user_permission of this WebsiteGroup.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

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
        if issubclass(WebsiteGroup, dict):
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
        if not isinstance(other, WebsiteGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other