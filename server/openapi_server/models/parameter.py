# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Parameter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_default_value=None, has_maximum_accepted_value=None, has_data_type=None, description=None, has_fixed_value=None, has_presentation=None, label=None, type=None, has_minimum_accepted_value=None, has_accepted_values=None, adjusts_variable=None, position=None, id=None, uses_unit=None, has_step_size=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI

        :param has_default_value: The has_default_value of this Parameter.  # noqa: E501
        :type has_default_value: List[object]
        :param has_maximum_accepted_value: The has_maximum_accepted_value of this Parameter.  # noqa: E501
        :type has_maximum_accepted_value: List[object]
        :param has_data_type: The has_data_type of this Parameter.  # noqa: E501
        :type has_data_type: List[str]
        :param description: The description of this Parameter.  # noqa: E501
        :type description: List[str]
        :param has_fixed_value: The has_fixed_value of this Parameter.  # noqa: E501
        :type has_fixed_value: List[object]
        :param has_presentation: The has_presentation of this Parameter.  # noqa: E501
        :type has_presentation: List[VariablePresentation]
        :param label: The label of this Parameter.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Parameter.  # noqa: E501
        :type type: List[str]
        :param has_minimum_accepted_value: The has_minimum_accepted_value of this Parameter.  # noqa: E501
        :type has_minimum_accepted_value: List[object]
        :param has_accepted_values: The has_accepted_values of this Parameter.  # noqa: E501
        :type has_accepted_values: List[str]
        :param adjusts_variable: The adjusts_variable of this Parameter.  # noqa: E501
        :type adjusts_variable: List[object]
        :param position: The position of this Parameter.  # noqa: E501
        :type position: List[int]
        :param id: The id of this Parameter.  # noqa: E501
        :type id: str
        :param uses_unit: The uses_unit of this Parameter.  # noqa: E501
        :type uses_unit: List[object]
        :param has_step_size: The has_step_size of this Parameter.  # noqa: E501
        :type has_step_size: List[float]
        """
        from openapi_server.models.variable_presentation import VariablePresentation

          # noqa: E501

        self.openapi_types = {
            'has_default_value': List[object],
            'has_maximum_accepted_value': List[object],
            'has_data_type': List[str],
            'description': List[str],
            'has_fixed_value': List[object],
            'has_presentation': List[VariablePresentation],
            'label': List[str],
            'type': List[str],
            'has_minimum_accepted_value': List[object],
            'has_accepted_values': List[str],
            'adjusts_variable': List[object],
            'position': List[int],
            'id': str,
            'uses_unit': List[object],
            'has_step_size': List[float]
        }

        self.attribute_map = {
            'has_default_value': 'hasDefaultValue',
            'has_maximum_accepted_value': 'hasMaximumAcceptedValue',
            'has_data_type': 'hasDataType',
            'description': 'description',
            'has_fixed_value': 'hasFixedValue',
            'has_presentation': 'hasPresentation',
            'label': 'label',
            'type': 'type',
            'has_minimum_accepted_value': 'hasMinimumAcceptedValue',
            'has_accepted_values': 'hasAcceptedValues',
            'adjusts_variable': 'adjustsVariable',
            'position': 'position',
            'id': 'id',
            'uses_unit': 'usesUnit',
            'has_step_size': 'hasStepSize'
        }

        self._has_default_value = has_default_value
        self._has_maximum_accepted_value = has_maximum_accepted_value
        self._has_data_type = has_data_type
        self._description = description
        self._has_fixed_value = has_fixed_value
        self._has_presentation = has_presentation
        self._label = label
        self._type = type
        self._has_minimum_accepted_value = has_minimum_accepted_value
        self._has_accepted_values = has_accepted_values
        self._adjusts_variable = adjusts_variable
        self._position = position
        self._id = id
        self._uses_unit = uses_unit
        self._has_step_size = has_step_size

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_default_value(self):
        """Gets the has_default_value of this Parameter.


        :return: The has_default_value of this Parameter.
        :rtype: List[object]
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this Parameter.


        :param has_default_value: The has_default_value of this Parameter.
        :type has_default_value: List[object]
        """

        self._has_default_value = has_default_value

    @property
    def has_maximum_accepted_value(self):
        """Gets the has_maximum_accepted_value of this Parameter.


        :return: The has_maximum_accepted_value of this Parameter.
        :rtype: List[object]
        """
        return self._has_maximum_accepted_value

    @has_maximum_accepted_value.setter
    def has_maximum_accepted_value(self, has_maximum_accepted_value):
        """Sets the has_maximum_accepted_value of this Parameter.


        :param has_maximum_accepted_value: The has_maximum_accepted_value of this Parameter.
        :type has_maximum_accepted_value: List[object]
        """

        self._has_maximum_accepted_value = has_maximum_accepted_value

    @property
    def has_data_type(self):
        """Gets the has_data_type of this Parameter.


        :return: The has_data_type of this Parameter.
        :rtype: List[str]
        """
        return self._has_data_type

    @has_data_type.setter
    def has_data_type(self, has_data_type):
        """Sets the has_data_type of this Parameter.


        :param has_data_type: The has_data_type of this Parameter.
        :type has_data_type: List[str]
        """

        self._has_data_type = has_data_type

    @property
    def description(self):
        """Gets the description of this Parameter.


        :return: The description of this Parameter.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parameter.


        :param description: The description of this Parameter.
        :type description: List[str]
        """

        self._description = description

    @property
    def has_fixed_value(self):
        """Gets the has_fixed_value of this Parameter.


        :return: The has_fixed_value of this Parameter.
        :rtype: List[object]
        """
        return self._has_fixed_value

    @has_fixed_value.setter
    def has_fixed_value(self, has_fixed_value):
        """Sets the has_fixed_value of this Parameter.


        :param has_fixed_value: The has_fixed_value of this Parameter.
        :type has_fixed_value: List[object]
        """

        self._has_fixed_value = has_fixed_value

    @property
    def has_presentation(self):
        """Gets the has_presentation of this Parameter.


        :return: The has_presentation of this Parameter.
        :rtype: List[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this Parameter.


        :param has_presentation: The has_presentation of this Parameter.
        :type has_presentation: List[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def label(self):
        """Gets the label of this Parameter.


        :return: The label of this Parameter.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Parameter.


        :param label: The label of this Parameter.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Parameter.


        :return: The type of this Parameter.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Parameter.


        :param type: The type of this Parameter.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_minimum_accepted_value(self):
        """Gets the has_minimum_accepted_value of this Parameter.


        :return: The has_minimum_accepted_value of this Parameter.
        :rtype: List[object]
        """
        return self._has_minimum_accepted_value

    @has_minimum_accepted_value.setter
    def has_minimum_accepted_value(self, has_minimum_accepted_value):
        """Sets the has_minimum_accepted_value of this Parameter.


        :param has_minimum_accepted_value: The has_minimum_accepted_value of this Parameter.
        :type has_minimum_accepted_value: List[object]
        """

        self._has_minimum_accepted_value = has_minimum_accepted_value

    @property
    def has_accepted_values(self):
        """Gets the has_accepted_values of this Parameter.


        :return: The has_accepted_values of this Parameter.
        :rtype: List[str]
        """
        return self._has_accepted_values

    @has_accepted_values.setter
    def has_accepted_values(self, has_accepted_values):
        """Sets the has_accepted_values of this Parameter.


        :param has_accepted_values: The has_accepted_values of this Parameter.
        :type has_accepted_values: List[str]
        """

        self._has_accepted_values = has_accepted_values

    @property
    def adjusts_variable(self):
        """Gets the adjusts_variable of this Parameter.


        :return: The adjusts_variable of this Parameter.
        :rtype: List[object]
        """
        return self._adjusts_variable

    @adjusts_variable.setter
    def adjusts_variable(self, adjusts_variable):
        """Sets the adjusts_variable of this Parameter.


        :param adjusts_variable: The adjusts_variable of this Parameter.
        :type adjusts_variable: List[object]
        """

        self._adjusts_variable = adjusts_variable

    @property
    def position(self):
        """Gets the position of this Parameter.


        :return: The position of this Parameter.
        :rtype: List[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Parameter.


        :param position: The position of this Parameter.
        :type position: List[int]
        """

        self._position = position

    @property
    def id(self):
        """Gets the id of this Parameter.


        :return: The id of this Parameter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Parameter.


        :param id: The id of this Parameter.
        :type id: str
        """

        self._id = id

    @property
    def uses_unit(self):
        """Gets the uses_unit of this Parameter.


        :return: The uses_unit of this Parameter.
        :rtype: List[object]
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this Parameter.


        :param uses_unit: The uses_unit of this Parameter.
        :type uses_unit: List[object]
        """

        self._uses_unit = uses_unit

    @property
    def has_step_size(self):
        """Gets the has_step_size of this Parameter.


        :return: The has_step_size of this Parameter.
        :rtype: List[float]
        """
        return self._has_step_size

    @has_step_size.setter
    def has_step_size(self, has_step_size):
        """Sets the has_step_size of this Parameter.


        :param has_step_size: The has_step_size of this Parameter.
        :type has_step_size: List[float]
        """

        self._has_step_size = has_step_size
