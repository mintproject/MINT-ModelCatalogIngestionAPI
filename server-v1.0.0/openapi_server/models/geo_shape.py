# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GeoShape(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, elevation=None, latitude=None, box=None, id=None, label=None, type=None, longitude=None):  # noqa: E501
        """GeoShape - a model defined in OpenAPI

        :param elevation: The elevation of this GeoShape.  # noqa: E501
        :type elevation: List[str]
        :param latitude: The latitude of this GeoShape.  # noqa: E501
        :type latitude: List[str]
        :param box: The box of this GeoShape.  # noqa: E501
        :type box: List[str]
        :param id: The id of this GeoShape.  # noqa: E501
        :type id: str
        :param label: The label of this GeoShape.  # noqa: E501
        :type label: str
        :param type: The type of this GeoShape.  # noqa: E501
        :type type: List[str]
        :param longitude: The longitude of this GeoShape.  # noqa: E501
        :type longitude: List[str]
        """


        self.openapi_types = {
            'elevation': List[str],
            'latitude': List[str],
            'box': List[str],
            'id': str,
            'label': str,
            'type': List[str],
            'longitude': List[str]
        }

        self.attribute_map = {
            'elevation': 'elevation',
            'latitude': 'latitude',
            'box': 'box',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'longitude': 'longitude'
        }

        self._elevation = elevation
        self._latitude = latitude
        self._box = box
        self._id = id
        self._label = label
        self._type = type
        self._longitude = longitude

    @classmethod
    def from_dict(cls, dikt) -> 'GeoShape':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeoShape of this GeoShape.  # noqa: E501
        :rtype: GeoShape
        """
        return util.deserialize_model(dikt, cls)

    @property
    def elevation(self):
        """Gets the elevation of this GeoShape.


        :return: The elevation of this GeoShape.
        :rtype: List[str]
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this GeoShape.


        :param elevation: The elevation of this GeoShape.
        :type elevation: List[str]
        """

        self._elevation = elevation

    @property
    def latitude(self):
        """Gets the latitude of this GeoShape.


        :return: The latitude of this GeoShape.
        :rtype: List[str]
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this GeoShape.


        :param latitude: The latitude of this GeoShape.
        :type latitude: List[str]
        """

        self._latitude = latitude

    @property
    def box(self):
        """Gets the box of this GeoShape.


        :return: The box of this GeoShape.
        :rtype: List[str]
        """
        return self._box

    @box.setter
    def box(self, box):
        """Sets the box of this GeoShape.


        :param box: The box of this GeoShape.
        :type box: List[str]
        """

        self._box = box

    @property
    def id(self):
        """Gets the id of this GeoShape.


        :return: The id of this GeoShape.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeoShape.


        :param id: The id of this GeoShape.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this GeoShape.


        :return: The label of this GeoShape.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GeoShape.


        :param label: The label of this GeoShape.
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this GeoShape.


        :return: The type of this GeoShape.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeoShape.


        :param type: The type of this GeoShape.
        :type type: List[str]
        """

        self._type = type

    @property
    def longitude(self):
        """Gets the longitude of this GeoShape.


        :return: The longitude of this GeoShape.
        :rtype: List[str]
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this GeoShape.


        :param longitude: The longitude of this GeoShape.
        :type longitude: List[str]
        """

        self._longitude = longitude