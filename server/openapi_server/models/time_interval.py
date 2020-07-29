# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TimeInterval(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, interval_unit=None, description=None, id=None, label=None, type=None, interval_value=None):  # noqa: E501
        """TimeInterval - a model defined in OpenAPI

        :param interval_unit: The interval_unit of this TimeInterval.  # noqa: E501
        :type interval_unit: List[Unit]
        :param description: The description of this TimeInterval.  # noqa: E501
        :type description: List[str]
        :param id: The id of this TimeInterval.  # noqa: E501
        :type id: str
        :param label: The label of this TimeInterval.  # noqa: E501
        :type label: List[str]
        :param type: The type of this TimeInterval.  # noqa: E501
        :type type: List[str]
        :param interval_value: The interval_value of this TimeInterval.  # noqa: E501
        :type interval_value: List[AnyOfintegerstring]
        """
        from openapi_server.models.any_ofintegerstring import AnyOfintegerstring
        from openapi_server.models.unit import Unit

          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'interval_unit': List[Unit],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str],
            'interval_value': List[AnyOfintegerstring]
        }

        self.attribute_map = {
            'interval_unit': 'intervalUnit',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'interval_value': 'intervalValue'
        }

        self._interval_unit = interval_unit
        self._description = description
        self._id = id
        self._label = label
        self._type = type
        self._interval_value = interval_value

    @classmethod
    def from_dict(cls, dikt) -> 'TimeInterval':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimeInterval of this TimeInterval.  # noqa: E501
        :rtype: TimeInterval
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interval_unit(self):
        """Gets the interval_unit of this TimeInterval.

        Unit used in an interval (e.g., month)  # noqa: E501

        :return: The interval_unit of this TimeInterval.
        :rtype: List[Unit]
        """
        return self._interval_unit

    @interval_unit.setter
    def interval_unit(self, interval_unit):
        """Sets the interval_unit of this TimeInterval.

        Unit used in an interval (e.g., month)  # noqa: E501

        :param interval_unit: The interval_unit of this TimeInterval.
        :type interval_unit: List[Unit]
        """

        self._interval_unit = interval_unit

    @property
    def description(self):
        """Gets the description of this TimeInterval.

        small description  # noqa: E501

        :return: The description of this TimeInterval.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TimeInterval.

        small description  # noqa: E501

        :param description: The description of this TimeInterval.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this TimeInterval.

        identifier  # noqa: E501

        :return: The id of this TimeInterval.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimeInterval.

        identifier  # noqa: E501

        :param id: The id of this TimeInterval.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this TimeInterval.

        short description of the resource  # noqa: E501

        :return: The label of this TimeInterval.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TimeInterval.

        short description of the resource  # noqa: E501

        :param label: The label of this TimeInterval.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this TimeInterval.

        type of the resource  # noqa: E501

        :return: The type of this TimeInterval.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimeInterval.

        type of the resource  # noqa: E501

        :param type: The type of this TimeInterval.
        :type type: List[str]
        """

        self._type = type

    @property
    def interval_value(self):
        """Gets the interval_value of this TimeInterval.

        Value used in the time interval of a model (e.g., 1 month, 5 days, 'harvest cycle')  # noqa: E501

        :return: The interval_value of this TimeInterval.
        :rtype: List[AnyOfintegerstring]
        """
        return self._interval_value

    @interval_value.setter
    def interval_value(self, interval_value):
        """Sets the interval_value of this TimeInterval.

        Value used in the time interval of a model (e.g., 1 month, 5 days, 'harvest cycle')  # noqa: E501

        :param interval_value: The interval_value of this TimeInterval.
        :type interval_value: List[AnyOfintegerstring]
        """

        self._interval_value = interval_value
