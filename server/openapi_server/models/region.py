# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Region(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, geo=None, part_of=None, description=None, id=None, label=None, type=None):  # noqa: E501
        """Region - a model defined in OpenAPI

        :param geo: The geo of this Region.  # noqa: E501
        :type geo: List[object]
        :param part_of: The part_of of this Region.  # noqa: E501
        :type part_of: List[Region]
        :param description: The description of this Region.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Region.  # noqa: E501
        :type id: str
        :param label: The label of this Region.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Region.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'geo': List[object],
            'part_of': List[Region],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'geo': 'geo',
            'part_of': 'partOf',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._geo = geo
        self._part_of = part_of
        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Region':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Region of this Region.  # noqa: E501
        :rtype: Region
        """
        return util.deserialize_model(dikt, cls)

    @property
    def geo(self):
        """Gets the geo of this Region.

        Specific coordinates or shape associated with a region  # noqa: E501

        :return: The geo of this Region.
        :rtype: List[object]
        """
        return self._geo

    @geo.setter
    def geo(self, geo):
        """Sets the geo of this Region.

        Specific coordinates or shape associated with a region  # noqa: E501

        :param geo: The geo of this Region.
        :type geo: List[object]
        """

        self._geo = geo

    @property
    def part_of(self):
        """Gets the part_of of this Region.

        Indicates whether a region is part of another region  # noqa: E501

        :return: The part_of of this Region.
        :rtype: List[Region]
        """
        return self._part_of

    @part_of.setter
    def part_of(self, part_of):
        """Sets the part_of of this Region.

        Indicates whether a region is part of another region  # noqa: E501

        :param part_of: The part_of of this Region.
        :type part_of: List[Region]
        """

        self._part_of = part_of

    @property
    def description(self):
        """Gets the description of this Region.

        small description  # noqa: E501

        :return: The description of this Region.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Region.

        small description  # noqa: E501

        :param description: The description of this Region.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Region.

        identifier  # noqa: E501

        :return: The id of this Region.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Region.

        identifier  # noqa: E501

        :param id: The id of this Region.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Region.

        short description of the resource  # noqa: E501

        :return: The label of this Region.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Region.

        short description of the resource  # noqa: E501

        :param label: The label of this Region.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Region.

        type of the resource  # noqa: E501

        :return: The type of this Region.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Region.

        type of the resource  # noqa: E501

        :param type: The type of this Region.
        :type type: List[str]
        """

        self._type = type
