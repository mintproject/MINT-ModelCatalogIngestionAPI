# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DataSet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, label=None, format=None, description=None, dimensionality=None, presentations=None, type=None, id=None):  # noqa: E501
        """DataSet - a model defined in OpenAPI

        :param label: The label of this DataSet.  # noqa: E501
        :type label: str
        :param format: The format of this DataSet.  # noqa: E501
        :type format: str
        :param description: The description of this DataSet.  # noqa: E501
        :type description: str
        :param dimensionality: The dimensionality of this DataSet.  # noqa: E501
        :type dimensionality: int
        :param presentations: The presentations of this DataSet.  # noqa: E501
        :type presentations: List[VariablePresentation]
        :param type: The type of this DataSet.  # noqa: E501
        :type type: List[str]
        :param id: The id of this DataSet.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'label': str,
            'format': str,
            'description': str,
            'dimensionality': int,
            'presentations': List[VariablePresentation],
            'type': List[str],
            'id': str
        }

        self.attribute_map = {
            'label': 'label',
            'format': 'format',
            'description': 'description',
            'dimensionality': 'dimensionality',
            'presentations': 'presentations',
            'type': 'type',
            'id': 'id'
        }

        self._label = label
        self._format = format
        self._description = description
        self._dimensionality = dimensionality
        self._presentations = presentations
        self._type = type
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'DataSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataSet of this DataSet.  # noqa: E501
        :rtype: DataSet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def label(self):
        """Gets the label of this DataSet.


        :return: The label of this DataSet.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DataSet.


        :param label: The label of this DataSet.
        :type label: str
        """

        self._label = label

    @property
    def format(self):
        """Gets the format of this DataSet.


        :return: The format of this DataSet.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this DataSet.


        :param format: The format of this DataSet.
        :type format: str
        """

        self._format = format

    @property
    def description(self):
        """Gets the description of this DataSet.


        :return: The description of this DataSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataSet.


        :param description: The description of this DataSet.
        :type description: str
        """

        self._description = description

    @property
    def dimensionality(self):
        """Gets the dimensionality of this DataSet.


        :return: The dimensionality of this DataSet.
        :rtype: int
        """
        return self._dimensionality

    @dimensionality.setter
    def dimensionality(self, dimensionality):
        """Sets the dimensionality of this DataSet.


        :param dimensionality: The dimensionality of this DataSet.
        :type dimensionality: int
        """

        self._dimensionality = dimensionality

    @property
    def presentations(self):
        """Gets the presentations of this DataSet.


        :return: The presentations of this DataSet.
        :rtype: List[VariablePresentation]
        """
        return self._presentations

    @presentations.setter
    def presentations(self, presentations):
        """Sets the presentations of this DataSet.


        :param presentations: The presentations of this DataSet.
        :type presentations: List[VariablePresentation]
        """

        self._presentations = presentations

    @property
    def type(self):
        """Gets the type of this DataSet.


        :return: The type of this DataSet.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataSet.


        :param type: The type of this DataSet.
        :type type: List[str]
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this DataSet.


        :return: The id of this DataSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSet.


        :param id: The id of this DataSet.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id
