# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from openapi_server import util
from openapi_server.models.unit import Unit
from openapi_server.models.base_model_ import Model


class VariablePresentation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, type=None, label=None, description=None, has_long_name=None, has_short_name=None, has_standard_variable=None, has_relevance_level=None, uses_unit=None):  # noqa: E501
        """VariablePresentation - a model defined in OpenAPI

        :param id: The id of this VariablePresentation.  # noqa: E501
        :type id: str
        :param type: The type of this VariablePresentation.  # noqa: E501
        :type type: List[str]
        :param label: The label of this VariablePresentation.  # noqa: E501
        :type label: str
        :param description: The description of this VariablePresentation.  # noqa: E501
        :type description: str
        :param has_long_name: The has_long_name of this VariablePresentation.  # noqa: E501
        :type has_long_name: str
        :param has_short_name: The has_short_name of this VariablePresentation.  # noqa: E501
        :type has_short_name: str
        :param has_standard_variable: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :type has_standard_variable: str
        :param has_relevance_level: The has_relevance_level of this VariablePresentation.  # noqa: E501
        :type has_relevance_level: int
        :param uses_unit: The uses_unit of this VariablePresentation.  # noqa: E501
        :type uses_unit: Unit
        """
        self.openapi_types = {
            'id': str,
            'type': List[str],
            'label': str,
            'description': str,
            'has_long_name': str,
            'has_short_name': str,
            'has_standard_variable': str,
            'has_relevance_level': int,
            'uses_unit': Unit
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'label': 'label',
            'description': 'description',
            'has_long_name': 'has_long_name',
            'has_short_name': 'has_short_name',
            'has_standard_variable': 'has_standard_variable',
            'has_relevance_level': 'has_relevance_level',
            'uses_unit': 'uses_unit'
        }

        self._id = id
        self._type = type
        self._label = label
        self._description = description
        self._has_long_name = has_long_name
        self._has_short_name = has_short_name
        self._has_standard_variable = has_standard_variable
        self._has_relevance_level = has_relevance_level
        self._uses_unit = uses_unit

    @classmethod
    def from_dict(cls, dikt) -> 'VariablePresentation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VariablePresentation of this VariablePresentation.  # noqa: E501
        :rtype: VariablePresentation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VariablePresentation.


        :return: The id of this VariablePresentation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariablePresentation.


        :param id: The id of this VariablePresentation.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this VariablePresentation.


        :return: The type of this VariablePresentation.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariablePresentation.


        :param type: The type of this VariablePresentation.
        :type type: List[str]
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this VariablePresentation.


        :return: The label of this VariablePresentation.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VariablePresentation.


        :param label: The label of this VariablePresentation.
        :type label: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this VariablePresentation.


        :return: The description of this VariablePresentation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariablePresentation.


        :param description: The description of this VariablePresentation.
        :type description: str
        """

        self._description = description

    @property
    def has_long_name(self):
        """Gets the has_long_name of this VariablePresentation.


        :return: The has_long_name of this VariablePresentation.
        :rtype: str
        """
        return self._has_long_name

    @has_long_name.setter
    def has_long_name(self, has_long_name):
        """Sets the has_long_name of this VariablePresentation.


        :param has_long_name: The has_long_name of this VariablePresentation.
        :type has_long_name: str
        """

        self._has_long_name = has_long_name

    @property
    def has_short_name(self):
        """Gets the has_short_name of this VariablePresentation.


        :return: The has_short_name of this VariablePresentation.
        :rtype: str
        """
        return self._has_short_name

    @has_short_name.setter
    def has_short_name(self, has_short_name):
        """Sets the has_short_name of this VariablePresentation.


        :param has_short_name: The has_short_name of this VariablePresentation.
        :type has_short_name: str
        """

        self._has_short_name = has_short_name

    @property
    def has_standard_variable(self):
        """Gets the has_standard_variable of this VariablePresentation.


        :return: The has_standard_variable of this VariablePresentation.
        :rtype: str
        """
        return self._has_standard_variable

    @has_standard_variable.setter
    def has_standard_variable(self, has_standard_variable):
        """Sets the has_standard_variable of this VariablePresentation.


        :param has_standard_variable: The has_standard_variable of this VariablePresentation.
        :type has_standard_variable: str
        """

        self._has_standard_variable = has_standard_variable

    @property
    def has_relevance_level(self):
        """Gets the has_relevance_level of this VariablePresentation.


        :return: The has_relevance_level of this VariablePresentation.
        :rtype: int
        """
        return self._has_relevance_level

    @has_relevance_level.setter
    def has_relevance_level(self, has_relevance_level):
        """Sets the has_relevance_level of this VariablePresentation.


        :param has_relevance_level: The has_relevance_level of this VariablePresentation.
        :type has_relevance_level: int
        """

        self._has_relevance_level = has_relevance_level

    @property
    def uses_unit(self):
        """Gets the uses_unit of this VariablePresentation.


        :return: The uses_unit of this VariablePresentation.
        :rtype: Unit
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this VariablePresentation.


        :param uses_unit: The uses_unit of this VariablePresentation.
        :type uses_unit: Unit
        """

        self._uses_unit = uses_unit
