# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SpatiallyDistributedGrid(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_shape=None, has_dimension=None, id=None, label=None, type=None, has_spatial_resolution=None, has_coordinate_system=None):  # noqa: E501
        """SpatiallyDistributedGrid - a model defined in OpenAPI

        :param has_shape: The has_shape of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_shape: List[str]
        :param has_dimension: The has_dimension of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_dimension: List[str]
        :param id: The id of this SpatiallyDistributedGrid.  # noqa: E501
        :type id: List[str]
        :param label: The label of this SpatiallyDistributedGrid.  # noqa: E501
        :type label: List[str]
        :param type: The type of this SpatiallyDistributedGrid.  # noqa: E501
        :type type: List[str]
        :param has_spatial_resolution: The has_spatial_resolution of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_spatial_resolution: List[str]
        :param has_coordinate_system: The has_coordinate_system of this SpatiallyDistributedGrid.  # noqa: E501
        :type has_coordinate_system: List[str]
        """
        self.openapi_types = {
            'has_shape': List[str],
            'has_dimension': List[str],
            'id': List[str],
            'label': List[str],
            'type': List[str],
            'has_spatial_resolution': List[str],
            'has_coordinate_system': List[str]
        }

        self.attribute_map = {
            'has_shape': 'hasShape',
            'has_dimension': 'hasDimension',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_spatial_resolution': 'hasSpatialResolution',
            'has_coordinate_system': 'hasCoordinateSystem'
        }

        self._has_shape = has_shape
        self._has_dimension = has_dimension
        self._id = id
        self._label = label
        self._type = type
        self._has_spatial_resolution = has_spatial_resolution
        self._has_coordinate_system = has_coordinate_system

    @classmethod
    def from_dict(cls, dikt) -> 'SpatiallyDistributedGrid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpatiallyDistributedGrid of this SpatiallyDistributedGrid.  # noqa: E501
        :rtype: SpatiallyDistributedGrid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_shape(self):
        """Gets the has_shape of this SpatiallyDistributedGrid.


        :return: The has_shape of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_shape

    @has_shape.setter
    def has_shape(self, has_shape):
        """Sets the has_shape of this SpatiallyDistributedGrid.


        :param has_shape: The has_shape of this SpatiallyDistributedGrid.
        :type has_shape: List[str]
        """

        self._has_shape = has_shape

    @property
    def has_dimension(self):
        """Gets the has_dimension of this SpatiallyDistributedGrid.


        :return: The has_dimension of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_dimension

    @has_dimension.setter
    def has_dimension(self, has_dimension):
        """Sets the has_dimension of this SpatiallyDistributedGrid.


        :param has_dimension: The has_dimension of this SpatiallyDistributedGrid.
        :type has_dimension: List[str]
        """

        self._has_dimension = has_dimension

    @property
    def id(self):
        """Gets the id of this SpatiallyDistributedGrid.


        :return: The id of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpatiallyDistributedGrid.


        :param id: The id of this SpatiallyDistributedGrid.
        :type id: List[str]
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this SpatiallyDistributedGrid.


        :return: The label of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SpatiallyDistributedGrid.


        :param label: The label of this SpatiallyDistributedGrid.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SpatiallyDistributedGrid.


        :return: The type of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpatiallyDistributedGrid.


        :param type: The type of this SpatiallyDistributedGrid.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_spatial_resolution(self):
        """Gets the has_spatial_resolution of this SpatiallyDistributedGrid.


        :return: The has_spatial_resolution of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_spatial_resolution

    @has_spatial_resolution.setter
    def has_spatial_resolution(self, has_spatial_resolution):
        """Sets the has_spatial_resolution of this SpatiallyDistributedGrid.


        :param has_spatial_resolution: The has_spatial_resolution of this SpatiallyDistributedGrid.
        :type has_spatial_resolution: List[str]
        """

        self._has_spatial_resolution = has_spatial_resolution

    @property
    def has_coordinate_system(self):
        """Gets the has_coordinate_system of this SpatiallyDistributedGrid.


        :return: The has_coordinate_system of this SpatiallyDistributedGrid.
        :rtype: List[str]
        """
        return self._has_coordinate_system

    @has_coordinate_system.setter
    def has_coordinate_system(self, has_coordinate_system):
        """Sets the has_coordinate_system of this SpatiallyDistributedGrid.


        :param has_coordinate_system: The has_coordinate_system of this SpatiallyDistributedGrid.
        :type has_coordinate_system: List[str]
        """

        self._has_coordinate_system = has_coordinate_system