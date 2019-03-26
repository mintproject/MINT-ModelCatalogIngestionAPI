# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Model(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, uri=None, label=None, type=None, versions=None, categories=None, documentation=None):  # noqa: E501
        """Model - a model defined in OpenAPI

        :param uri: The uri of this Model.  # noqa: E501
        :type uri: str
        :param label: The label of this Model.  # noqa: E501
        :type label: str
        :param type: The type of this Model.  # noqa: E501
        :type type: List[str]
        :param versions: The versions of this Model.  # noqa: E501
        :type versions: List[str]
        :param categories: The categories of this Model.  # noqa: E501
        :type categories: List[str]
        :param documentation: The documentation of this Model.  # noqa: E501
        :type documentation: List[str]
        """
        self.openapi_types = {
            'uri': str,
            'label': str,
            'type': List[str],
            'versions': List[str],
            'categories': List[str],
            'documentation': List[str]
        }

        self.attribute_map = {
            'uri': 'uri',
            'label': 'label',
            'type': 'type',
            'versions': 'versions',
            'categories': 'categories',
            'documentation': 'documentation'
        }

        self._uri = uri
        self._label = label
        self._type = type
        self._versions = versions
        self._categories = categories
        self._documentation = documentation

    @classmethod
    def from_dict(cls, dikt) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.  # noqa: E501
        :rtype: Model
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self):
        """Gets the uri of this Model.


        :return: The uri of this Model.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Model.


        :param uri: The uri of this Model.
        :type uri: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def label(self):
        """Gets the label of this Model.


        :return: The label of this Model.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Model.


        :param label: The label of this Model.
        :type label: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Model.


        :return: The type of this Model.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Model.


        :param type: The type of this Model.
        :type type: List[str]
        """

        self._type = type

    @property
    def versions(self):
        """Gets the versions of this Model.


        :return: The versions of this Model.
        :rtype: List[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Model.


        :param versions: The versions of this Model.
        :type versions: List[str]
        """

        self._versions = versions

    @property
    def categories(self):
        """Gets the categories of this Model.


        :return: The categories of this Model.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Model.


        :param categories: The categories of this Model.
        :type categories: List[str]
        """

        self._categories = categories

    @property
    def documentation(self):
        """Gets the documentation of this Model.


        :return: The documentation of this Model.
        :rtype: List[str]
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation):
        """Sets the documentation of this Model.


        :param documentation: The documentation of this Model.
        :type documentation: List[str]
        """

        self._documentation = documentation
