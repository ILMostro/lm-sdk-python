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


class DeviceDataSourceInstanceConfigAlert(object):
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
        'alert_id': 'str',
        'alert_level': 'int',
        'alert_summary': 'str',
        'id': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'alert_id': 'alertId',
        'alert_level': 'alertLevel',
        'alert_summary': 'alertSummary',
        'id': 'id',
        'timestamp': 'timestamp'
    }

    def __init__(self, alert_id=None, alert_level=None, alert_summary=None, id=None, timestamp=None):  # noqa: E501
        """DeviceDataSourceInstanceConfigAlert - a model defined in Swagger"""  # noqa: E501

        self._alert_id = None
        self._alert_level = None
        self._alert_summary = None
        self._id = None
        self._timestamp = None
        self.discriminator = None

        if alert_id is not None:
            self.alert_id = alert_id
        if alert_level is not None:
            self.alert_level = alert_level
        if alert_summary is not None:
            self.alert_summary = alert_summary
        if id is not None:
            self.id = id
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def alert_id(self):
        """Gets the alert_id of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501


        :return: The alert_id of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :rtype: str
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this DeviceDataSourceInstanceConfigAlert.


        :param alert_id: The alert_id of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :type: str
        """

        self._alert_id = alert_id

    @property
    def alert_level(self):
        """Gets the alert_level of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501


        :return: The alert_level of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :rtype: int
        """
        return self._alert_level

    @alert_level.setter
    def alert_level(self, alert_level):
        """Sets the alert_level of this DeviceDataSourceInstanceConfigAlert.


        :param alert_level: The alert_level of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :type: int
        """

        self._alert_level = alert_level

    @property
    def alert_summary(self):
        """Gets the alert_summary of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501


        :return: The alert_summary of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :rtype: str
        """
        return self._alert_summary

    @alert_summary.setter
    def alert_summary(self, alert_summary):
        """Sets the alert_summary of this DeviceDataSourceInstanceConfigAlert.


        :param alert_summary: The alert_summary of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :type: str
        """

        self._alert_summary = alert_summary

    @property
    def id(self):
        """Gets the id of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501


        :return: The id of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceDataSourceInstanceConfigAlert.


        :param id: The id of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501


        :return: The timestamp of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DeviceDataSourceInstanceConfigAlert.


        :param timestamp: The timestamp of this DeviceDataSourceInstanceConfigAlert.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if issubclass(DeviceDataSourceInstanceConfigAlert, dict):
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
        if not isinstance(other, DeviceDataSourceInstanceConfigAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other