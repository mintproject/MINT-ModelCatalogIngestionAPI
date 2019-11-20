# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SampleCollection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data_catalog_identifier=None, has_part=None, description=None, id=None, label=None, type=None, value=None):  # noqa: E501
        """SampleCollection - a model defined in OpenAPI

        :param data_catalog_identifier: The data_catalog_identifier of this SampleCollection.  # noqa: E501
        :type data_catalog_identifier: List[str]
        :param has_part: The has_part of this SampleCollection.  # noqa: E501
        :type has_part: List[SampleResource]
        :param description: The description of this SampleCollection.  # noqa: E501
        :type description: List[str]
        :param id: The id of this SampleCollection.  # noqa: E501
        :type id: str
        :param label: The label of this SampleCollection.  # noqa: E501
        :type label: List[str]
        :param type: The type of this SampleCollection.  # noqa: E501
        :type type: List[str]
        :param value: The value of this SampleCollection.  # noqa: E501
        :type value: List[str]
        """
        from openapi_server.models.sample_resource import SampleResource

          # noqa: E501

        self.openapi_types = {
            'data_catalog_identifier': List[str],
            'has_part': List[SampleResource],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str],
            'value': List[str]
        }

        self.attribute_map = {
            'data_catalog_identifier': 'dataCatalogIdentifier',
            'has_part': 'hasPart',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'value': 'value'
        }

        self._data_catalog_identifier = data_catalog_identifier
        self._has_part = has_part
        self._description = description
        self._id = id
        self._label = label
        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'SampleCollection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SampleCollection of this SampleCollection.  # noqa: E501
        :rtype: SampleCollection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_catalog_identifier(self):
        """Gets the data_catalog_identifier of this SampleCollection.


        :return: The data_catalog_identifier of this SampleCollection.
        :rtype: List[str]
        """
        return self._data_catalog_identifier

    @data_catalog_identifier.setter
    def data_catalog_identifier(self, data_catalog_identifier):
        """Sets the data_catalog_identifier of this SampleCollection.


        :param data_catalog_identifier: The data_catalog_identifier of this SampleCollection.
        :type data_catalog_identifier: List[str]
        """

        self._data_catalog_identifier = data_catalog_identifier

    @property
    def has_part(self):
        """Gets the has_part of this SampleCollection.


        :return: The has_part of this SampleCollection.
        :rtype: List[SampleResource]
        """
        return self._has_part

    @has_part.setter
    def has_part(self, has_part):
        """Sets the has_part of this SampleCollection.


        :param has_part: The has_part of this SampleCollection.
        :type has_part: List[SampleResource]
        """

        self._has_part = has_part

    @property
    def description(self):
        """Gets the description of this SampleCollection.


        :return: The description of this SampleCollection.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SampleCollection.


        :param description: The description of this SampleCollection.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this SampleCollection.


        :return: The id of this SampleCollection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleCollection.


        :param id: The id of this SampleCollection.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SampleCollection.


        :return: The label of this SampleCollection.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SampleCollection.


        :param label: The label of this SampleCollection.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SampleCollection.


        :return: The type of this SampleCollection.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SampleCollection.


        :param type: The type of this SampleCollection.
        :type type: List[str]
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this SampleCollection.


        :return: The value of this SampleCollection.
        :rtype: List[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SampleCollection.


        :param value: The value of this SampleCollection.
        :type value: List[str]
        """

        self._value = value