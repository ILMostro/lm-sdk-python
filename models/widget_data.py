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


class WidgetData(object):
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
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'gauge': 'GaugeWidgetData',
        'noc': 'NOCWidgetData',
        'dynamictable': 'DynamicTableWidgetData',
        'groupnetflow': 'NetflowGroupWidgetData',
        'graph': 'GraphPlot',
        'websitesla': 'WebsiteSLAWidgetData',
        'table': 'TableWidgetData',
        'devicesla': 'DeviceSLAWidgetData',
        'gmap': 'GoogleMapWidgetData',
        'netflow': 'NetflowWidgetData',
        'piechart': 'PieChartWidgetData',
        'batchjob': 'BatchJobWidgetData',
        'alert': 'AlertWidgetData',
        'bignumber': 'BigNumberWidgetData'
    }

    def __init__(self, title=None, type=None):  # noqa: E501
        """WidgetData - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._type = None
        self.discriminator = 'type'

        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def title(self):
        """Gets the title of this WidgetData.  # noqa: E501


        :return: The title of this WidgetData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WidgetData.


        :param title: The title of this WidgetData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this WidgetData.  # noqa: E501


        :return: The type of this WidgetData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WidgetData.


        :param type: The type of this WidgetData.  # noqa: E501
        :type: str
        """

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(WidgetData, dict):
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
        if not isinstance(other, WidgetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other