# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Grid(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, has_coordinate_system=None, has_data_transformation=None, has_data_transformation_setup=None, has_dimension=None, has_dimensionality=None, has_file_structure=None, has_fixed_resource=None, has_format=None, has_presentation=None, has_shape=None, has_spatial_resolution=None, id=None, is_transformed_from=None, label=None, path_location=None, position=None, type=None):  # noqa: E501
        """Grid - a model defined in OpenAPI

        :param description: The description of this Grid.  # noqa: E501
        :type description: List[str]
        :param has_coordinate_system: The has_coordinate_system of this Grid.  # noqa: E501
        :type has_coordinate_system: List[str]
        :param has_data_transformation: The has_data_transformation of this Grid.  # noqa: E501
        :type has_data_transformation: List[DataTransformation]
        :param has_data_transformation_setup: The has_data_transformation_setup of this Grid.  # noqa: E501
        :type has_data_transformation_setup: List[DataTransformationSetup]
        :param has_dimension: The has_dimension of this Grid.  # noqa: E501
        :type has_dimension: List[str]
        :param has_dimensionality: The has_dimensionality of this Grid.  # noqa: E501
        :type has_dimensionality: List[int]
        :param has_file_structure: The has_file_structure of this Grid.  # noqa: E501
        :type has_file_structure: List[object]
        :param has_fixed_resource: The has_fixed_resource of this Grid.  # noqa: E501
        :type has_fixed_resource: List[SampleResource]
        :param has_format: The has_format of this Grid.  # noqa: E501
        :type has_format: List[str]
        :param has_presentation: The has_presentation of this Grid.  # noqa: E501
        :type has_presentation: List[VariablePresentation]
        :param has_shape: The has_shape of this Grid.  # noqa: E501
        :type has_shape: List[str]
        :param has_spatial_resolution: The has_spatial_resolution of this Grid.  # noqa: E501
        :type has_spatial_resolution: List[str]
        :param id: The id of this Grid.  # noqa: E501
        :type id: str
        :param is_transformed_from: The is_transformed_from of this Grid.  # noqa: E501
        :type is_transformed_from: List[DatasetSpecification]
        :param label: The label of this Grid.  # noqa: E501
        :type label: List[str]
        :param path_location: The path_location of this Grid.  # noqa: E501
        :type path_location: List[str]
        :param position: The position of this Grid.  # noqa: E501
        :type position: List[int]
        :param type: The type of this Grid.  # noqa: E501
        :type type: List[str]
        """
        from openapi_server.models.data_transformation import DataTransformation
        from openapi_server.models.data_transformation_setup import DataTransformationSetup
        from openapi_server.models.dataset_specification import DatasetSpecification
        from openapi_server.models.sample_resource import SampleResource
        from openapi_server.models.variable_presentation import VariablePresentation

          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'description': List[str],
            'has_coordinate_system': List[str],
            'has_data_transformation': List[DataTransformation],
            'has_data_transformation_setup': List[DataTransformationSetup],
            'has_dimension': List[str],
            'has_dimensionality': List[int],
            'has_file_structure': List[object],
            'has_fixed_resource': List[SampleResource],
            'has_format': List[str],
            'has_presentation': List[VariablePresentation],
            'has_shape': List[str],
            'has_spatial_resolution': List[str],
            'id': str,
            'is_transformed_from': List[DatasetSpecification],
            'label': List[str],
            'path_location': List[str],
            'position': List[int],
            'type': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'has_coordinate_system': 'hasCoordinateSystem',
            'has_data_transformation': 'hasDataTransformation',
            'has_data_transformation_setup': 'hasDataTransformationSetup',
            'has_dimension': 'hasDimension',
            'has_dimensionality': 'hasDimensionality',
            'has_file_structure': 'hasFileStructure',
            'has_fixed_resource': 'hasFixedResource',
            'has_format': 'hasFormat',
            'has_presentation': 'hasPresentation',
            'has_shape': 'hasShape',
            'has_spatial_resolution': 'hasSpatialResolution',
            'id': 'id',
            'is_transformed_from': 'isTransformedFrom',
            'label': 'label',
            'path_location': 'pathLocation',
            'position': 'position',
            'type': 'type'
        }

        self._description = description
        self._has_coordinate_system = has_coordinate_system
        self._has_data_transformation = has_data_transformation
        self._has_data_transformation_setup = has_data_transformation_setup
        self._has_dimension = has_dimension
        self._has_dimensionality = has_dimensionality
        self._has_file_structure = has_file_structure
        self._has_fixed_resource = has_fixed_resource
        self._has_format = has_format
        self._has_presentation = has_presentation
        self._has_shape = has_shape
        self._has_spatial_resolution = has_spatial_resolution
        self._id = id
        self._is_transformed_from = is_transformed_from
        self._label = label
        self._path_location = path_location
        self._position = position
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Grid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Grid of this Grid.  # noqa: E501
        :rtype: Grid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Grid.

        small description  # noqa: E501

        :return: The description of this Grid.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Grid.

        small description  # noqa: E501

        :param description: The description of this Grid.
        :type description: List[str]
        """

        self._description = description

    @property
    def has_coordinate_system(self):
        """Gets the has_coordinate_system of this Grid.

        Coordinate system used in a grid  # noqa: E501

        :return: The has_coordinate_system of this Grid.
        :rtype: List[str]
        """
        return self._has_coordinate_system

    @has_coordinate_system.setter
    def has_coordinate_system(self, has_coordinate_system):
        """Sets the has_coordinate_system of this Grid.

        Coordinate system used in a grid  # noqa: E501

        :param has_coordinate_system: The has_coordinate_system of this Grid.
        :type has_coordinate_system: List[str]
        """

        self._has_coordinate_system = has_coordinate_system

    @property
    def has_data_transformation(self):
        """Gets the has_data_transformation of this Grid.

        Description not available  # noqa: E501

        :return: The has_data_transformation of this Grid.
        :rtype: List[DataTransformation]
        """
        return self._has_data_transformation

    @has_data_transformation.setter
    def has_data_transformation(self, has_data_transformation):
        """Sets the has_data_transformation of this Grid.

        Description not available  # noqa: E501

        :param has_data_transformation: The has_data_transformation of this Grid.
        :type has_data_transformation: List[DataTransformation]
        """

        self._has_data_transformation = has_data_transformation

    @property
    def has_data_transformation_setup(self):
        """Gets the has_data_transformation_setup of this Grid.

        Description not available  # noqa: E501

        :return: The has_data_transformation_setup of this Grid.
        :rtype: List[DataTransformationSetup]
        """
        return self._has_data_transformation_setup

    @has_data_transformation_setup.setter
    def has_data_transformation_setup(self, has_data_transformation_setup):
        """Sets the has_data_transformation_setup of this Grid.

        Description not available  # noqa: E501

        :param has_data_transformation_setup: The has_data_transformation_setup of this Grid.
        :type has_data_transformation_setup: List[DataTransformationSetup]
        """

        self._has_data_transformation_setup = has_data_transformation_setup

    @property
    def has_dimension(self):
        """Gets the has_dimension of this Grid.

        Dimension of the grid (2D, 3D)  # noqa: E501

        :return: The has_dimension of this Grid.
        :rtype: List[str]
        """
        return self._has_dimension

    @has_dimension.setter
    def has_dimension(self, has_dimension):
        """Sets the has_dimension of this Grid.

        Dimension of the grid (2D, 3D)  # noqa: E501

        :param has_dimension: The has_dimension of this Grid.
        :type has_dimension: List[str]
        """

        self._has_dimension = has_dimension

    @property
    def has_dimensionality(self):
        """Gets the has_dimensionality of this Grid.

        Description not available  # noqa: E501

        :return: The has_dimensionality of this Grid.
        :rtype: List[int]
        """
        return self._has_dimensionality

    @has_dimensionality.setter
    def has_dimensionality(self, has_dimensionality):
        """Sets the has_dimensionality of this Grid.

        Description not available  # noqa: E501

        :param has_dimensionality: The has_dimensionality of this Grid.
        :type has_dimensionality: List[int]
        """

        self._has_dimensionality = has_dimensionality

    @property
    def has_file_structure(self):
        """Gets the has_file_structure of this Grid.

        Description not available  # noqa: E501

        :return: The has_file_structure of this Grid.
        :rtype: List[object]
        """
        return self._has_file_structure

    @has_file_structure.setter
    def has_file_structure(self, has_file_structure):
        """Sets the has_file_structure of this Grid.

        Description not available  # noqa: E501

        :param has_file_structure: The has_file_structure of this Grid.
        :type has_file_structure: List[object]
        """

        self._has_file_structure = has_file_structure

    @property
    def has_fixed_resource(self):
        """Gets the has_fixed_resource of this Grid.

        Description not available  # noqa: E501

        :return: The has_fixed_resource of this Grid.
        :rtype: List[SampleResource]
        """
        return self._has_fixed_resource

    @has_fixed_resource.setter
    def has_fixed_resource(self, has_fixed_resource):
        """Sets the has_fixed_resource of this Grid.

        Description not available  # noqa: E501

        :param has_fixed_resource: The has_fixed_resource of this Grid.
        :type has_fixed_resource: List[SampleResource]
        """

        self._has_fixed_resource = has_fixed_resource

    @property
    def has_format(self):
        """Gets the has_format of this Grid.

        Description not available  # noqa: E501

        :return: The has_format of this Grid.
        :rtype: List[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this Grid.

        Description not available  # noqa: E501

        :param has_format: The has_format of this Grid.
        :type has_format: List[str]
        """

        self._has_format = has_format

    @property
    def has_presentation(self):
        """Gets the has_presentation of this Grid.

        Description not available  # noqa: E501

        :return: The has_presentation of this Grid.
        :rtype: List[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this Grid.

        Description not available  # noqa: E501

        :param has_presentation: The has_presentation of this Grid.
        :type has_presentation: List[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def has_shape(self):
        """Gets the has_shape of this Grid.

        Grids may be: rectangular, triangular, hexagonal, hybrid, unstructured, block structure, etc.  # noqa: E501

        :return: The has_shape of this Grid.
        :rtype: List[str]
        """
        return self._has_shape

    @has_shape.setter
    def has_shape(self, has_shape):
        """Sets the has_shape of this Grid.

        Grids may be: rectangular, triangular, hexagonal, hybrid, unstructured, block structure, etc.  # noqa: E501

        :param has_shape: The has_shape of this Grid.
        :type has_shape: List[str]
        """

        self._has_shape = has_shape

    @property
    def has_spatial_resolution(self):
        """Gets the has_spatial_resolution of this Grid.

        Spatial resolution of a grid (e.g., 50m)  # noqa: E501

        :return: The has_spatial_resolution of this Grid.
        :rtype: List[str]
        """
        return self._has_spatial_resolution

    @has_spatial_resolution.setter
    def has_spatial_resolution(self, has_spatial_resolution):
        """Sets the has_spatial_resolution of this Grid.

        Spatial resolution of a grid (e.g., 50m)  # noqa: E501

        :param has_spatial_resolution: The has_spatial_resolution of this Grid.
        :type has_spatial_resolution: List[str]
        """

        self._has_spatial_resolution = has_spatial_resolution

    @property
    def id(self):
        """Gets the id of this Grid.

        identifier  # noqa: E501

        :return: The id of this Grid.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Grid.

        identifier  # noqa: E501

        :param id: The id of this Grid.
        :type id: str
        """

        self._id = id

    @property
    def is_transformed_from(self):
        """Gets the is_transformed_from of this Grid.

        Description not available  # noqa: E501

        :return: The is_transformed_from of this Grid.
        :rtype: List[DatasetSpecification]
        """
        return self._is_transformed_from

    @is_transformed_from.setter
    def is_transformed_from(self, is_transformed_from):
        """Sets the is_transformed_from of this Grid.

        Description not available  # noqa: E501

        :param is_transformed_from: The is_transformed_from of this Grid.
        :type is_transformed_from: List[DatasetSpecification]
        """

        self._is_transformed_from = is_transformed_from

    @property
    def label(self):
        """Gets the label of this Grid.

        short description of the resource  # noqa: E501

        :return: The label of this Grid.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Grid.

        short description of the resource  # noqa: E501

        :param label: The label of this Grid.
        :type label: List[str]
        """

        self._label = label

    @property
    def path_location(self):
        """Gets the path_location of this Grid.

        Description not available  # noqa: E501

        :return: The path_location of this Grid.
        :rtype: List[str]
        """
        return self._path_location

    @path_location.setter
    def path_location(self, path_location):
        """Sets the path_location of this Grid.

        Description not available  # noqa: E501

        :param path_location: The path_location of this Grid.
        :type path_location: List[str]
        """

        self._path_location = path_location

    @property
    def position(self):
        """Gets the position of this Grid.

        Description not available  # noqa: E501

        :return: The position of this Grid.
        :rtype: List[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Grid.

        Description not available  # noqa: E501

        :param position: The position of this Grid.
        :type position: List[int]
        """

        self._position = position

    @property
    def type(self):
        """Gets the type of this Grid.

        type of the resource  # noqa: E501

        :return: The type of this Grid.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Grid.

        type of the resource  # noqa: E501

        :param type: The type of this Grid.
        :type type: List[str]
        """

        self._type = type
