# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Constraint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, id=None, label=None, type=None, has_rule=None, has_variable=None):  # noqa: E501
        """Constraint - a model defined in OpenAPI

        :param description: The description of this Constraint.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Constraint.  # noqa: E501
        :type id: str
        :param label: The label of this Constraint.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Constraint.  # noqa: E501
        :type type: List[str]
        :param has_rule: The has_rule of this Constraint.  # noqa: E501
        :type has_rule: List[str]
        :param has_variable: The has_variable of this Constraint.  # noqa: E501
        :type has_variable: List[VariablePresentation]
        """
        from openapi_server.models.variable_presentation import VariablePresentation

          # noqa: E501

        self.openapi_types = {
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str],
            'has_rule': List[str],
            'has_variable': List[VariablePresentation]
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_rule': 'hasRule',
            'has_variable': 'hasVariable'
        }

        self._description = description
        self._id = id
        self._label = label
        self._type = type
        self._has_rule = has_rule
        self._has_variable = has_variable

    @classmethod
    def from_dict(cls, dikt) -> 'Constraint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Constraint of this Constraint.  # noqa: E501
        :rtype: Constraint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Constraint.

        small description  # noqa: E501

        :return: The description of this Constraint.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Constraint.

        small description  # noqa: E501

        :param description: The description of this Constraint.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Constraint.

        identifier  # noqa: E501

        :return: The id of this Constraint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Constraint.

        identifier  # noqa: E501

        :param id: The id of this Constraint.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Constraint.

        short description of the resource  # noqa: E501

        :return: The label of this Constraint.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Constraint.

        short description of the resource  # noqa: E501

        :param label: The label of this Constraint.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Constraint.

        type of the resource  # noqa: E501

        :return: The type of this Constraint.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Constraint.

        type of the resource  # noqa: E501

        :param type: The type of this Constraint.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_rule(self):
        """Gets the has_rule of this Constraint.

        Rule that defines this constraint  # noqa: E501

        :return: The has_rule of this Constraint.
        :rtype: List[str]
        """
        return self._has_rule

    @has_rule.setter
    def has_rule(self, has_rule):
        """Sets the has_rule of this Constraint.

        Rule that defines this constraint  # noqa: E501

        :param has_rule: The has_rule of this Constraint.
        :type has_rule: List[str]
        """

        self._has_rule = has_rule

    @property
    def has_variable(self):
        """Gets the has_variable of this Constraint.

        Property that links a rule and the variable that will test it  # noqa: E501

        :return: The has_variable of this Constraint.
        :rtype: List[VariablePresentation]
        """
        return self._has_variable

    @has_variable.setter
    def has_variable(self, has_variable):
        """Sets the has_variable of this Constraint.

        Property that links a rule and the variable that will test it  # noqa: E501

        :param has_variable: The has_variable of this Constraint.
        :type has_variable: List[VariablePresentation]
        """

        self._has_variable = has_variable
