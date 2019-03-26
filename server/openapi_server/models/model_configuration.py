# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from openapi_server import util
from openapi_server.models.base_model_ import Model
from openapi_server.models.cag import CAG  # noqa: E501
from openapi_server.models.data_set import DataSet  # noqa: E501
from openapi_server.models.parameter import Parameter  # noqa: E501
from openapi_server.models.process import Process  # noqa: E501
from openapi_server.models.time_interval import TimeInterval  # noqa: E501


class ModelConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, type=None, label=None, inputs=None, outputs=None, description=None, cag=None, process=None, interval_time=None, implementation_script_location=None, container=None, constrain_t=None, parameters=None, component_location=None):  # noqa: E501
        """ModelConfiguration - a model defined in OpenAPI

        :param id: The id of this ModelConfiguration.  # noqa: E501
        :type id: str
        :param type: The type of this ModelConfiguration.  # noqa: E501
        :type type: List[str]
        :param label: The label of this ModelConfiguration.  # noqa: E501
        :type label: str
        :param inputs: The inputs of this ModelConfiguration.  # noqa: E501
        :type inputs: List[DataSet]
        :param outputs: The outputs of this ModelConfiguration.  # noqa: E501
        :type outputs: List[DataSet]
        :param description: The description of this ModelConfiguration.  # noqa: E501
        :type description: str
        :param cag: The cag of this ModelConfiguration.  # noqa: E501
        :type cag: List[CAG]
        :param process: The process of this ModelConfiguration.  # noqa: E501
        :type process: List[Process]
        :param interval_time: The interval_time of this ModelConfiguration.  # noqa: E501
        :type interval_time: List[TimeInterval]
        :param implementation_script_location: The implementation_script_location of this ModelConfiguration.  # noqa: E501
        :type implementation_script_location: str
        :param container: The container of this ModelConfiguration.  # noqa: E501
        :type container: str
        :param constrain_t: The constrain_t of this ModelConfiguration.  # noqa: E501
        :type constrain_t: str
        :param parameters: The parameters of this ModelConfiguration.  # noqa: E501
        :type parameters: List[Parameter]
        :param component_location: The component_location of this ModelConfiguration.  # noqa: E501
        :type component_location: str
        """
        self.openapi_types = {
            'id': str,
            'type': List[str],
            'label': str,
            'inputs': List[DataSet],
            'outputs': List[DataSet],
            'description': str,
            'cag': List[CAG],
            'process': List[Process],
            'interval_time': List[TimeInterval],
            'implementation_script_location': str,
            'container': str,
            'constrain_t': str,
            'parameters': List[Parameter],
            'component_location': str
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'label': 'label',
            'inputs': 'inputs',
            'outputs': 'outputs',
            'description': 'description',
            'cag': 'cag',
            'process': 'process',
            'interval_time': 'intervalTime',
            'implementation_script_location': 'implementationScriptLocation',
            'container': 'container',
            'constrain_t': 'constrainT',
            'parameters': 'parameters',
            'component_location': 'componentLocation'
        }

        self._id = id
        self._type = type
        self._label = label
        self._inputs = inputs
        self._outputs = outputs
        self._description = description
        self._cag = cag
        self._process = process
        self._interval_time = interval_time
        self._implementation_script_location = implementation_script_location
        self._container = container
        self._constrain_t = constrain_t
        self._parameters = parameters
        self._component_location = component_location

    @classmethod
    def from_dict(cls, dikt) -> 'ModelConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelConfiguration of this ModelConfiguration.  # noqa: E501
        :rtype: ModelConfiguration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ModelConfiguration.


        :return: The id of this ModelConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelConfiguration.


        :param id: The id of this ModelConfiguration.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this ModelConfiguration.


        :return: The type of this ModelConfiguration.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelConfiguration.


        :param type: The type of this ModelConfiguration.
        :type type: List[str]
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this ModelConfiguration.


        :return: The label of this ModelConfiguration.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelConfiguration.


        :param label: The label of this ModelConfiguration.
        :type label: str
        """

        self._label = label

    @property
    def inputs(self):
        """Gets the inputs of this ModelConfiguration.


        :return: The inputs of this ModelConfiguration.
        :rtype: List[DataSet]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ModelConfiguration.


        :param inputs: The inputs of this ModelConfiguration.
        :type inputs: List[DataSet]
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this ModelConfiguration.


        :return: The outputs of this ModelConfiguration.
        :rtype: List[DataSet]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ModelConfiguration.


        :param outputs: The outputs of this ModelConfiguration.
        :type outputs: List[DataSet]
        """

        self._outputs = outputs

    @property
    def description(self):
        """Gets the description of this ModelConfiguration.


        :return: The description of this ModelConfiguration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelConfiguration.


        :param description: The description of this ModelConfiguration.
        :type description: str
        """

        self._description = description

    @property
    def cag(self):
        """Gets the cag of this ModelConfiguration.


        :return: The cag of this ModelConfiguration.
        :rtype: List[CAG]
        """
        return self._cag

    @cag.setter
    def cag(self, cag):
        """Sets the cag of this ModelConfiguration.


        :param cag: The cag of this ModelConfiguration.
        :type cag: List[CAG]
        """

        self._cag = cag

    @property
    def process(self):
        """Gets the process of this ModelConfiguration.


        :return: The process of this ModelConfiguration.
        :rtype: List[Process]
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this ModelConfiguration.


        :param process: The process of this ModelConfiguration.
        :type process: List[Process]
        """

        self._process = process

    @property
    def interval_time(self):
        """Gets the interval_time of this ModelConfiguration.


        :return: The interval_time of this ModelConfiguration.
        :rtype: List[TimeInterval]
        """
        return self._interval_time

    @interval_time.setter
    def interval_time(self, interval_time):
        """Sets the interval_time of this ModelConfiguration.


        :param interval_time: The interval_time of this ModelConfiguration.
        :type interval_time: List[TimeInterval]
        """

        self._interval_time = interval_time

    @property
    def implementation_script_location(self):
        """Gets the implementation_script_location of this ModelConfiguration.


        :return: The implementation_script_location of this ModelConfiguration.
        :rtype: str
        """
        return self._implementation_script_location

    @implementation_script_location.setter
    def implementation_script_location(self, implementation_script_location):
        """Sets the implementation_script_location of this ModelConfiguration.


        :param implementation_script_location: The implementation_script_location of this ModelConfiguration.
        :type implementation_script_location: str
        """

        self._implementation_script_location = implementation_script_location

    @property
    def container(self):
        """Gets the container of this ModelConfiguration.


        :return: The container of this ModelConfiguration.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this ModelConfiguration.


        :param container: The container of this ModelConfiguration.
        :type container: str
        """

        self._container = container

    @property
    def constrain_t(self):
        """Gets the constrain_t of this ModelConfiguration.


        :return: The constrain_t of this ModelConfiguration.
        :rtype: str
        """
        return self._constrain_t

    @constrain_t.setter
    def constrain_t(self, constrain_t):
        """Sets the constrain_t of this ModelConfiguration.


        :param constrain_t: The constrain_t of this ModelConfiguration.
        :type constrain_t: str
        """

        self._constrain_t = constrain_t

    @property
    def parameters(self):
        """Gets the parameters of this ModelConfiguration.


        :return: The parameters of this ModelConfiguration.
        :rtype: List[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ModelConfiguration.


        :param parameters: The parameters of this ModelConfiguration.
        :type parameters: List[Parameter]
        """

        self._parameters = parameters

    @property
    def component_location(self):
        """Gets the component_location of this ModelConfiguration.


        :return: The component_location of this ModelConfiguration.
        :rtype: str
        """
        return self._component_location

    @component_location.setter
    def component_location(self, component_location):
        """Sets the component_location of this ModelConfiguration.


        :param component_location: The component_location of this ModelConfiguration.
        :type component_location: str
        """

        self._component_location = component_location
