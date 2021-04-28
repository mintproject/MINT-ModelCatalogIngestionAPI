# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class VariablePresentation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_default_value=None, has_short_name=None, has_minimum_accepted_value=None, has_standard_variable=None, has_maximum_accepted_value=None, description=None, part_of_dataset=None, id=None, label=None, uses_unit=None, type=None, has_long_name=None):  # noqa: E501
        """VariablePresentation - a model defined in OpenAPI

        :param has_default_value: The has_default_value of this VariablePresentation.  # noqa: E501
        :type has_default_value: List[object]
        :param has_short_name: The has_short_name of this VariablePresentation.  # noqa: E501
        :type has_short_name: List[str]
        :param has_minimum_accepted_value: The has_minimum_accepted_value of this VariablePresentation.  # noqa: E501
        :type has_minimum_accepted_value: List[object]
        :param has_standard_variable: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :type has_standard_variable: List[StandardVariable]
        :param has_maximum_accepted_value: The has_maximum_accepted_value of this VariablePresentation.  # noqa: E501
        :type has_maximum_accepted_value: List[object]
        :param description: The description of this VariablePresentation.  # noqa: E501
        :type description: List[str]
        :param part_of_dataset: The part_of_dataset of this VariablePresentation.  # noqa: E501
        :type part_of_dataset: List[DatasetSpecification]
        :param id: The id of this VariablePresentation.  # noqa: E501
        :type id: str
        :param label: The label of this VariablePresentation.  # noqa: E501
        :type label: List[str]
        :param uses_unit: The uses_unit of this VariablePresentation.  # noqa: E501
        :type uses_unit: List[Unit]
        :param type: The type of this VariablePresentation.  # noqa: E501
        :type type: List[str]
        :param has_long_name: The has_long_name of this VariablePresentation.  # noqa: E501
        :type has_long_name: List[str]
        """
        from openapi_server.models.dataset_specification import DatasetSpecification
        from openapi_server.models.standard_variable import StandardVariable
        from openapi_server.models.unit import Unit

          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'has_default_value': List[object],
            'has_short_name': List[str],
            'has_minimum_accepted_value': List[object],
            'has_standard_variable': List[StandardVariable],
            'has_maximum_accepted_value': List[object],
            'description': List[str],
            'part_of_dataset': List[DatasetSpecification],
            'id': str,
            'label': List[str],
            'uses_unit': List[Unit],
            'type': List[str],
            'has_long_name': List[str]
        }

        self.attribute_map = {
            'has_default_value': 'hasDefaultValue',
            'has_short_name': 'hasShortName',
            'has_minimum_accepted_value': 'hasMinimumAcceptedValue',
            'has_standard_variable': 'hasStandardVariable',
            'has_maximum_accepted_value': 'hasMaximumAcceptedValue',
            'description': 'description',
            'part_of_dataset': 'partOfDataset',
            'id': 'id',
            'label': 'label',
            'uses_unit': 'usesUnit',
            'type': 'type',
            'has_long_name': 'hasLongName'
        }

        self._has_default_value = has_default_value
        self._has_short_name = has_short_name
        self._has_minimum_accepted_value = has_minimum_accepted_value
        self._has_standard_variable = has_standard_variable
        self._has_maximum_accepted_value = has_maximum_accepted_value
        self._description = description
        self._part_of_dataset = part_of_dataset
        self._id = id
        self._label = label
        self._uses_unit = uses_unit
        self._type = type
        self._has_long_name = has_long_name

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
    def has_default_value(self):
        """Gets the has_default_value of this VariablePresentation.

        Default accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_default_value of this VariablePresentation.
        :rtype: List[object]
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this VariablePresentation.

        Default accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_default_value: The has_default_value of this VariablePresentation.
        :type has_default_value: List[object]
        """

        self._has_default_value = has_default_value

    @property
    def has_short_name(self):
        """Gets the has_short_name of this VariablePresentation.

        A short name (e.g., temperature) capturing the high-level concept of the variable  # noqa: E501

        :return: The has_short_name of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_short_name

    @has_short_name.setter
    def has_short_name(self, has_short_name):
        """Sets the has_short_name of this VariablePresentation.

        A short name (e.g., temperature) capturing the high-level concept of the variable  # noqa: E501

        :param has_short_name: The has_short_name of this VariablePresentation.
        :type has_short_name: List[str]
        """

        self._has_short_name = has_short_name

    @property
    def has_minimum_accepted_value(self):
        """Gets the has_minimum_accepted_value of this VariablePresentation.

        Minimum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_minimum_accepted_value of this VariablePresentation.
        :rtype: List[object]
        """
        return self._has_minimum_accepted_value

    @has_minimum_accepted_value.setter
    def has_minimum_accepted_value(self, has_minimum_accepted_value):
        """Sets the has_minimum_accepted_value of this VariablePresentation.

        Minimum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_minimum_accepted_value: The has_minimum_accepted_value of this VariablePresentation.
        :type has_minimum_accepted_value: List[object]
        """

        self._has_minimum_accepted_value = has_minimum_accepted_value

    @property
    def has_standard_variable(self):
        """Gets the has_standard_variable of this VariablePresentation.

        the standard name of a variable  # noqa: E501

        :return: The has_standard_variable of this VariablePresentation.
        :rtype: List[StandardVariable]
        """
        return self._has_standard_variable

    @has_standard_variable.setter
    def has_standard_variable(self, has_standard_variable):
        """Sets the has_standard_variable of this VariablePresentation.

        the standard name of a variable  # noqa: E501

        :param has_standard_variable: The has_standard_variable of this VariablePresentation.
        :type has_standard_variable: List[StandardVariable]
        """

        self._has_standard_variable = has_standard_variable

    @property
    def has_maximum_accepted_value(self):
        """Gets the has_maximum_accepted_value of this VariablePresentation.

        Maximum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_maximum_accepted_value of this VariablePresentation.
        :rtype: List[object]
        """
        return self._has_maximum_accepted_value

    @has_maximum_accepted_value.setter
    def has_maximum_accepted_value(self, has_maximum_accepted_value):
        """Sets the has_maximum_accepted_value of this VariablePresentation.

        Maximum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_maximum_accepted_value: The has_maximum_accepted_value of this VariablePresentation.
        :type has_maximum_accepted_value: List[object]
        """

        self._has_maximum_accepted_value = has_maximum_accepted_value

    @property
    def description(self):
        """Gets the description of this VariablePresentation.

        small description  # noqa: E501

        :return: The description of this VariablePresentation.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariablePresentation.

        small description  # noqa: E501

        :param description: The description of this VariablePresentation.
        :type description: List[str]
        """

        self._description = description

    @property
    def part_of_dataset(self):
        """Gets the part_of_dataset of this VariablePresentation.

        Associates a presentation with a dataset where the presentation occurs  # noqa: E501

        :return: The part_of_dataset of this VariablePresentation.
        :rtype: List[DatasetSpecification]
        """
        return self._part_of_dataset

    @part_of_dataset.setter
    def part_of_dataset(self, part_of_dataset):
        """Sets the part_of_dataset of this VariablePresentation.

        Associates a presentation with a dataset where the presentation occurs  # noqa: E501

        :param part_of_dataset: The part_of_dataset of this VariablePresentation.
        :type part_of_dataset: List[DatasetSpecification]
        """

        self._part_of_dataset = part_of_dataset

    @property
    def id(self):
        """Gets the id of this VariablePresentation.

        identifier  # noqa: E501

        :return: The id of this VariablePresentation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariablePresentation.

        identifier  # noqa: E501

        :param id: The id of this VariablePresentation.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this VariablePresentation.

        short description of the resource  # noqa: E501

        :return: The label of this VariablePresentation.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VariablePresentation.

        short description of the resource  # noqa: E501

        :param label: The label of this VariablePresentation.
        :type label: List[str]
        """

        self._label = label

    @property
    def uses_unit(self):
        """Gets the uses_unit of this VariablePresentation.

        Property used to link a variable presentation or time interval to the unit they are represented in  # noqa: E501

        :return: The uses_unit of this VariablePresentation.
        :rtype: List[Unit]
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this VariablePresentation.

        Property used to link a variable presentation or time interval to the unit they are represented in  # noqa: E501

        :param uses_unit: The uses_unit of this VariablePresentation.
        :type uses_unit: List[Unit]
        """

        self._uses_unit = uses_unit

    @property
    def type(self):
        """Gets the type of this VariablePresentation.

        type of the resource  # noqa: E501

        :return: The type of this VariablePresentation.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariablePresentation.

        type of the resource  # noqa: E501

        :param type: The type of this VariablePresentation.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_long_name(self):
        """Gets the has_long_name of this VariablePresentation.

        Properties that relate the variable representation to its long name. The long name is useful for context (e.g., precipitation is less ambiguous than P) but not as precise as the standard name.  # noqa: E501

        :return: The has_long_name of this VariablePresentation.
        :rtype: List[str]
        """
        return self._has_long_name

    @has_long_name.setter
    def has_long_name(self, has_long_name):
        """Sets the has_long_name of this VariablePresentation.

        Properties that relate the variable representation to its long name. The long name is useful for context (e.g., precipitation is less ambiguous than P) but not as precise as the standard name.  # noqa: E501

        :param has_long_name: The has_long_name of this VariablePresentation.
        :type has_long_name: List[str]
        """

        self._has_long_name = has_long_name
