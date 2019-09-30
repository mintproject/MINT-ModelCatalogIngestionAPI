# coding: utf-8

from __future__ import absolute_import

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util
from openapi_server.models.parameter import Parameter  # noqa: E501


class CAG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, type=["https://w3id.org/mint/modelCatalog#CAG"], has_part=None, label=None):  # noqa: E501
        """CAG - a model defined in OpenAPI

        :param id: The id of this CAG.  # noqa: E501
        :type id: str
        :param type: The type of this CAG.  # noqa: E501
        :type type: List[str]
        :param has_part: The has_part of this CAG.  # noqa: E501
        :type has_part: List[Parameter]
        :param label: The label of this CAG.  # noqa: E501
        :type label: str
        """
        self.openapi_types = {
            'id': str,
            'type': List[str],
            'has_part': List[Parameter],
            'label': str
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'has_part': 'hasPart',
            'label': 'label'
        }

        self._id = id
        self._type = type
        self._has_part = has_part
        self._label = label

    @classmethod
    def from_dict(cls, dikt) -> 'CAG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CAG of this CAG.  # noqa: E501
        :rtype: CAG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CAG.


        :return: The id of this CAG.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CAG.


        :param id: The id of this CAG.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this CAG.


        :return: The type of this CAG.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CAG.


        :param type: The type of this CAG.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_part(self):
        """Gets the has_part of this CAG.

        Array of Parameter or Variables  # noqa: E501

        :return: The has_part of this CAG.
        :rtype: List[Parameter]
        """
        return self._has_part

    @has_part.setter
    def has_part(self, has_part):
        """Sets the has_part of this CAG.

        Array of Parameter or Variables  # noqa: E501

        :param has_part: The has_part of this CAG.
        :type has_part: List[Parameter]
        """

        self._has_part = has_part

    @property
    def label(self):
        """Gets the label of this CAG.


        :return: The label of this CAG.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CAG.


        :param label: The label of this CAG.
        :type label: str
        """

        self._label = label