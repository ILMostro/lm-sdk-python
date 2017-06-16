# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NextUpgradeInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'upgrade_time': 'str',
        'stable': 'bool',
        'major_version': 'int',
        'minor_version': 'int',
        'mandatory': 'bool'
    }

    attribute_map = {
        'upgrade_time': 'upgradeTime',
        'stable': 'stable',
        'major_version': 'majorVersion',
        'minor_version': 'minorVersion',
        'mandatory': 'mandatory'
    }

    def __init__(self, upgrade_time=None, stable=None, major_version=None, minor_version=None, mandatory=None):
        """
        NextUpgradeInfo - a model defined in Swagger
        """

        self._upgrade_time = None
        self._stable = None
        self._major_version = None
        self._minor_version = None
        self._mandatory = None

        if upgrade_time is not None:
          self.upgrade_time = upgrade_time
        if stable is not None:
          self.stable = stable
        if major_version is not None:
          self.major_version = major_version
        if minor_version is not None:
          self.minor_version = minor_version
        if mandatory is not None:
          self.mandatory = mandatory

    @property
    def upgrade_time(self):
        """
        Gets the upgrade_time of this NextUpgradeInfo.

        :return: The upgrade_time of this NextUpgradeInfo.
        :rtype: str
        """
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, upgrade_time):
        """
        Sets the upgrade_time of this NextUpgradeInfo.

        :param upgrade_time: The upgrade_time of this NextUpgradeInfo.
        :type: str
        """

        self._upgrade_time = upgrade_time

    @property
    def stable(self):
        """
        Gets the stable of this NextUpgradeInfo.

        :return: The stable of this NextUpgradeInfo.
        :rtype: bool
        """
        return self._stable

    @stable.setter
    def stable(self, stable):
        """
        Sets the stable of this NextUpgradeInfo.

        :param stable: The stable of this NextUpgradeInfo.
        :type: bool
        """

        self._stable = stable

    @property
    def major_version(self):
        """
        Gets the major_version of this NextUpgradeInfo.

        :return: The major_version of this NextUpgradeInfo.
        :rtype: int
        """
        return self._major_version

    @major_version.setter
    def major_version(self, major_version):
        """
        Sets the major_version of this NextUpgradeInfo.

        :param major_version: The major_version of this NextUpgradeInfo.
        :type: int
        """

        self._major_version = major_version

    @property
    def minor_version(self):
        """
        Gets the minor_version of this NextUpgradeInfo.

        :return: The minor_version of this NextUpgradeInfo.
        :rtype: int
        """
        return self._minor_version

    @minor_version.setter
    def minor_version(self, minor_version):
        """
        Sets the minor_version of this NextUpgradeInfo.

        :param minor_version: The minor_version of this NextUpgradeInfo.
        :type: int
        """

        self._minor_version = minor_version

    @property
    def mandatory(self):
        """
        Gets the mandatory of this NextUpgradeInfo.

        :return: The mandatory of this NextUpgradeInfo.
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """
        Sets the mandatory of this NextUpgradeInfo.

        :param mandatory: The mandatory of this NextUpgradeInfo.
        :type: bool
        """

        self._mandatory = mandatory

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NextUpgradeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other