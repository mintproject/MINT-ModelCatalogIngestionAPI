# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Image(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_dimensionality=None, has_format=None, path_location=None, has_file_structure=None, description=None, has_data_transformation=None, has_presentation=None, label=None, type=None, has_fixed_resource=None, had_primary_source=None, has_data_transformation_setup=None, position=None, id=None, value=None):  # noqa: E501
        """Image - a model defined in OpenAPI

        :param has_dimensionality: The has_dimensionality of this Image.  # noqa: E501
        :type has_dimensionality: List[int]
        :param has_format: The has_format of this Image.  # noqa: E501
        :type has_format: List[str]
        :param path_location: The path_location of this Image.  # noqa: E501
        :type path_location: List[str]
        :param has_file_structure: The has_file_structure of this Image.  # noqa: E501
        :type has_file_structure: List[object]
        :param description: The description of this Image.  # noqa: E501
        :type description: List[str]
        :param has_data_transformation: The has_data_transformation of this Image.  # noqa: E501
        :type has_data_transformation: List[DataTransformation]
        :param has_presentation: The has_presentation of this Image.  # noqa: E501
        :type has_presentation: List[VariablePresentation]
        :param label: The label of this Image.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Image.  # noqa: E501
        :type type: List[str]
        :param has_fixed_resource: The has_fixed_resource of this Image.  # noqa: E501
        :type has_fixed_resource: List[SampleResource]
        :param had_primary_source: The had_primary_source of this Image.  # noqa: E501
        :type had_primary_source: List[object]
        :param has_data_transformation_setup: The has_data_transformation_setup of this Image.  # noqa: E501
        :type has_data_transformation_setup: List[DataTransformationSetup]
        :param position: The position of this Image.  # noqa: E501
        :type position: List[int]
        :param id: The id of this Image.  # noqa: E501
        :type id: str
        :param value: The value of this Image.  # noqa: E501
        :type value: List[object]
        """
        from openapi_server.models.data_transformation import DataTransformation
        from openapi_server.models.data_transformation_setup import DataTransformationSetup
        from openapi_server.models.sample_resource import SampleResource
        from openapi_server.models.variable_presentation import VariablePresentation

          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'has_dimensionality': List[int],
            'has_format': List[str],
            'path_location': List[str],
            'has_file_structure': List[object],
            'description': List[str],
            'has_data_transformation': List[DataTransformation],
            'has_presentation': List[VariablePresentation],
            'label': List[str],
            'type': List[str],
            'has_fixed_resource': List[SampleResource],
            'had_primary_source': List[object],
            'has_data_transformation_setup': List[DataTransformationSetup],
            'position': List[int],
            'id': str,
            'value': List[object]
        }

        self.attribute_map = {
            'has_dimensionality': 'hasDimensionality',
            'has_format': 'hasFormat',
            'path_location': 'pathLocation',
            'has_file_structure': 'hasFileStructure',
            'description': 'description',
            'has_data_transformation': 'hasDataTransformation',
            'has_presentation': 'hasPresentation',
            'label': 'label',
            'type': 'type',
            'has_fixed_resource': 'hasFixedResource',
            'had_primary_source': 'hadPrimarySource',
            'has_data_transformation_setup': 'hasDataTransformationSetup',
            'position': 'position',
            'id': 'id',
            'value': 'value'
        }

        self._has_dimensionality = has_dimensionality
        self._has_format = has_format
        self._path_location = path_location
        self._has_file_structure = has_file_structure
        self._description = description
        self._has_data_transformation = has_data_transformation
        self._has_presentation = has_presentation
        self._label = label
        self._type = type
        self._has_fixed_resource = has_fixed_resource
        self._had_primary_source = had_primary_source
        self._has_data_transformation_setup = has_data_transformation_setup
        self._position = position
        self._id = id
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Image':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Image of this Image.  # noqa: E501
        :rtype: Image
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_dimensionality(self):
        """Gets the has_dimensionality of this Image.

        Property to indicate dimensionality of the input or output of a dataset specification  # noqa: E501

        :return: The has_dimensionality of this Image.
        :rtype: List[int]
        """
        return self._has_dimensionality

    @has_dimensionality.setter
    def has_dimensionality(self, has_dimensionality):
        """Sets the has_dimensionality of this Image.

        Property to indicate dimensionality of the input or output of a dataset specification  # noqa: E501

        :param has_dimensionality: The has_dimensionality of this Image.
        :type has_dimensionality: List[int]
        """

        self._has_dimensionality = has_dimensionality

    @property
    def has_format(self):
        """Gets the has_format of this Image.

        Format followed by a file. For example, txt, nc, etc.  # noqa: E501

        :return: The has_format of this Image.
        :rtype: List[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this Image.

        Format followed by a file. For example, txt, nc, etc.  # noqa: E501

        :param has_format: The has_format of this Image.
        :type has_format: List[str]
        """

        self._has_format = has_format

    @property
    def path_location(self):
        """Gets the path_location of this Image.

        Property that indicates the relative path of an input or output with respect to the folder structure of the executable.   For example, let's assume we have an input that has to exist in the folder `/datasets` or the executable will not work. This property ensures that this knowledge is captured for a given software component execution.  In this case the property would capture this as follows:  ``` :input_prep a sd:DatasetSpecification . :input_prep rdfs:label \"precipitation file\" . :input_precip sd:pathLocation \"/datasets/\". ```  # noqa: E501

        :return: The path_location of this Image.
        :rtype: List[str]
        """
        return self._path_location

    @path_location.setter
    def path_location(self, path_location):
        """Sets the path_location of this Image.

        Property that indicates the relative path of an input or output with respect to the folder structure of the executable.   For example, let's assume we have an input that has to exist in the folder `/datasets` or the executable will not work. This property ensures that this knowledge is captured for a given software component execution.  In this case the property would capture this as follows:  ``` :input_prep a sd:DatasetSpecification . :input_prep rdfs:label \"precipitation file\" . :input_precip sd:pathLocation \"/datasets/\". ```  # noqa: E501

        :param path_location: The path_location of this Image.
        :type path_location: List[str]
        """

        self._path_location = path_location

    @property
    def has_file_structure(self):
        """Gets the has_file_structure of this Image.

        Relates a dataset specification to the data structure definition  # noqa: E501

        :return: The has_file_structure of this Image.
        :rtype: List[object]
        """
        return self._has_file_structure

    @has_file_structure.setter
    def has_file_structure(self, has_file_structure):
        """Sets the has_file_structure of this Image.

        Relates a dataset specification to the data structure definition  # noqa: E501

        :param has_file_structure: The has_file_structure of this Image.
        :type has_file_structure: List[object]
        """

        self._has_file_structure = has_file_structure

    @property
    def description(self):
        """Gets the description of this Image.

        small description  # noqa: E501

        :return: The description of this Image.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Image.

        small description  # noqa: E501

        :param description: The description of this Image.
        :type description: List[str]
        """

        self._description = description

    @property
    def has_data_transformation(self):
        """Gets the has_data_transformation of this Image.

        Property that associates an input/output with their corresponding data transformation.  # noqa: E501

        :return: The has_data_transformation of this Image.
        :rtype: List[DataTransformation]
        """
        return self._has_data_transformation

    @has_data_transformation.setter
    def has_data_transformation(self, has_data_transformation):
        """Sets the has_data_transformation of this Image.

        Property that associates an input/output with their corresponding data transformation.  # noqa: E501

        :param has_data_transformation: The has_data_transformation of this Image.
        :type has_data_transformation: List[DataTransformation]
        """

        self._has_data_transformation = has_data_transformation

    @property
    def has_presentation(self):
        """Gets the has_presentation of this Image.

        Property that links an instance of a dataset (or a dataset specification) to the presentation of a variable contained (or expected to be contained) on it.  # noqa: E501

        :return: The has_presentation of this Image.
        :rtype: List[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this Image.

        Property that links an instance of a dataset (or a dataset specification) to the presentation of a variable contained (or expected to be contained) on it.  # noqa: E501

        :param has_presentation: The has_presentation of this Image.
        :type has_presentation: List[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def label(self):
        """Gets the label of this Image.

        short description of the resource  # noqa: E501

        :return: The label of this Image.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Image.

        short description of the resource  # noqa: E501

        :param label: The label of this Image.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Image.

        type of the resource  # noqa: E501

        :return: The type of this Image.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Image.

        type of the resource  # noqa: E501

        :param type: The type of this Image.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_fixed_resource(self):
        """Gets the has_fixed_resource of this Image.

        Property that links a parameter or an input to a fixed value. For example, in a given configuration a parameter with the planting date for a model could be fixed to avoid the user changing it for that region.  # noqa: E501

        :return: The has_fixed_resource of this Image.
        :rtype: List[SampleResource]
        """
        return self._has_fixed_resource

    @has_fixed_resource.setter
    def has_fixed_resource(self, has_fixed_resource):
        """Sets the has_fixed_resource of this Image.

        Property that links a parameter or an input to a fixed value. For example, in a given configuration a parameter with the planting date for a model could be fixed to avoid the user changing it for that region.  # noqa: E501

        :param has_fixed_resource: The has_fixed_resource of this Image.
        :type has_fixed_resource: List[SampleResource]
        """

        self._has_fixed_resource = has_fixed_resource

    @property
    def had_primary_source(self):
        """Gets the had_primary_source of this Image.

        had primary source  # noqa: E501

        :return: The had_primary_source of this Image.
        :rtype: List[object]
        """
        return self._had_primary_source

    @had_primary_source.setter
    def had_primary_source(self, had_primary_source):
        """Sets the had_primary_source of this Image.

        had primary source  # noqa: E501

        :param had_primary_source: The had_primary_source of this Image.
        :type had_primary_source: List[object]
        """

        self._had_primary_source = had_primary_source

    @property
    def has_data_transformation_setup(self):
        """Gets the has_data_transformation_setup of this Image.

        Property to link an input/output dataset to the specific data transformation (with URLs  # noqa: E501

        :return: The has_data_transformation_setup of this Image.
        :rtype: List[DataTransformationSetup]
        """
        return self._has_data_transformation_setup

    @has_data_transformation_setup.setter
    def has_data_transformation_setup(self, has_data_transformation_setup):
        """Sets the has_data_transformation_setup of this Image.

        Property to link an input/output dataset to the specific data transformation (with URLs  # noqa: E501

        :param has_data_transformation_setup: The has_data_transformation_setup of this Image.
        :type has_data_transformation_setup: List[DataTransformationSetup]
        """

        self._has_data_transformation_setup = has_data_transformation_setup

    @property
    def position(self):
        """Gets the position of this Image.

        Position of the parameter or input/output in the model configuration. This property is needed to know how to organize the I/O of the component on execution  # noqa: E501

        :return: The position of this Image.
        :rtype: List[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Image.

        Position of the parameter or input/output in the model configuration. This property is needed to know how to organize the I/O of the component on execution  # noqa: E501

        :param position: The position of this Image.
        :type position: List[int]
        """

        self._position = position

    @property
    def id(self):
        """Gets the id of this Image.

        identifier  # noqa: E501

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Image.

        identifier  # noqa: E501

        :param id: The id of this Image.
        :type id: str
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this Image.

        Value associated to the described entity  # noqa: E501

        :return: The value of this Image.
        :rtype: List[object]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Image.

        Value associated to the described entity  # noqa: E501

        :param value: The value of this Image.
        :type value: List[object]
        """

        self._value = value
