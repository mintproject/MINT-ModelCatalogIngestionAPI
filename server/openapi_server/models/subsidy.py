# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Subsidy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, id=None, label=None, type=None):  # noqa: E501
        """Subsidy - a model defined in OpenAPI

        :param description: The description of this Subsidy.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Subsidy.  # noqa: E501
        :type id: str
        :param label: The label of this Subsidy.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Subsidy.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Subsidy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Subsidy of this Subsidy.  # noqa: E501
        :rtype: Subsidy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Subsidy.


        :return: The description of this Subsidy.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subsidy.


        :param description: The description of this Subsidy.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Subsidy.


        :return: The id of this Subsidy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subsidy.


        :param id: The id of this Subsidy.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Subsidy.


        :return: The label of this Subsidy.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Subsidy.


        :param label: The label of this Subsidy.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Subsidy.


        :return: The type of this Subsidy.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subsidy.


        :param type: The type of this Subsidy.
        :type type: List[str]
        """

        self._type = type