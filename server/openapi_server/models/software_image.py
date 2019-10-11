# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SoftwareImage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_funding=None, has_documentation=None, keywords=None, software_requirements=None, has_version=None, has_typical_data_source=None, has_download_url=None, reference_publication=None, description=None, screenshot=None, type=None, has_installation_instructions=None, date_created=None, compatible_visualization_software=None, contributor=None, has_faq=None, logo=None, has_contact_person=None, has_purpose=None, id=None, has_sample_visualization=None, memory_requirements=None, identifier=None, website=None, citation=None, author=None, processor_requirements=None, has_usage_notes=None, short_description=None, label=None, has_execution_command=None, has_assumption=None, date_published=None, license=None, operating_systems=None, has_source_code=None, has_example=None, publisher=None):  # noqa: E501
        """SoftwareImage - a model defined in OpenAPI

        :param has_funding: The has_funding of this SoftwareImage.  # noqa: E501
        :type has_funding: List[FundingInformation]
        :param has_documentation: The has_documentation of this SoftwareImage.  # noqa: E501
        :type has_documentation: List[str]
        :param keywords: The keywords of this SoftwareImage.  # noqa: E501
        :type keywords: List[str]
        :param software_requirements: The software_requirements of this SoftwareImage.  # noqa: E501
        :type software_requirements: List[str]
        :param has_version: The has_version of this SoftwareImage.  # noqa: E501
        :type has_version: List[SoftwareVersion]
        :param has_typical_data_source: The has_typical_data_source of this SoftwareImage.  # noqa: E501
        :type has_typical_data_source: List[str]
        :param has_download_url: The has_download_url of this SoftwareImage.  # noqa: E501
        :type has_download_url: List[str]
        :param reference_publication: The reference_publication of this SoftwareImage.  # noqa: E501
        :type reference_publication: List[str]
        :param description: The description of this SoftwareImage.  # noqa: E501
        :type description: List[str]
        :param screenshot: The screenshot of this SoftwareImage.  # noqa: E501
        :type screenshot: List[Image]
        :param type: The type of this SoftwareImage.  # noqa: E501
        :type type: List[str]
        :param has_installation_instructions: The has_installation_instructions of this SoftwareImage.  # noqa: E501
        :type has_installation_instructions: List[str]
        :param date_created: The date_created of this SoftwareImage.  # noqa: E501
        :type date_created: List[str]
        :param compatible_visualization_software: The compatible_visualization_software of this SoftwareImage.  # noqa: E501
        :type compatible_visualization_software: List[Software]
        :param contributor: The contributor of this SoftwareImage.  # noqa: E501
        :type contributor: List[Person]
        :param has_faq: The has_faq of this SoftwareImage.  # noqa: E501
        :type has_faq: List[str]
        :param logo: The logo of this SoftwareImage.  # noqa: E501
        :type logo: List[Image]
        :param has_contact_person: The has_contact_person of this SoftwareImage.  # noqa: E501
        :type has_contact_person: List[object]
        :param has_purpose: The has_purpose of this SoftwareImage.  # noqa: E501
        :type has_purpose: List[str]
        :param id: The id of this SoftwareImage.  # noqa: E501
        :type id: str
        :param has_sample_visualization: The has_sample_visualization of this SoftwareImage.  # noqa: E501
        :type has_sample_visualization: List[Visualization]
        :param memory_requirements: The memory_requirements of this SoftwareImage.  # noqa: E501
        :type memory_requirements: List[str]
        :param identifier: The identifier of this SoftwareImage.  # noqa: E501
        :type identifier: List[str]
        :param website: The website of this SoftwareImage.  # noqa: E501
        :type website: List[str]
        :param citation: The citation of this SoftwareImage.  # noqa: E501
        :type citation: List[str]
        :param author: The author of this SoftwareImage.  # noqa: E501
        :type author: List[object]
        :param processor_requirements: The processor_requirements of this SoftwareImage.  # noqa: E501
        :type processor_requirements: List[str]
        :param has_usage_notes: The has_usage_notes of this SoftwareImage.  # noqa: E501
        :type has_usage_notes: List[str]
        :param short_description: The short_description of this SoftwareImage.  # noqa: E501
        :type short_description: List[str]
        :param label: The label of this SoftwareImage.  # noqa: E501
        :type label: List[str]
        :param has_execution_command: The has_execution_command of this SoftwareImage.  # noqa: E501
        :type has_execution_command: List[str]
        :param has_assumption: The has_assumption of this SoftwareImage.  # noqa: E501
        :type has_assumption: List[str]
        :param date_published: The date_published of this SoftwareImage.  # noqa: E501
        :type date_published: List[str]
        :param license: The license of this SoftwareImage.  # noqa: E501
        :type license: List[str]
        :param operating_systems: The operating_systems of this SoftwareImage.  # noqa: E501
        :type operating_systems: List[str]
        :param has_source_code: The has_source_code of this SoftwareImage.  # noqa: E501
        :type has_source_code: List[SourceCode]
        :param has_example: The has_example of this SoftwareImage.  # noqa: E501
        :type has_example: List[str]
        :param publisher: The publisher of this SoftwareImage.  # noqa: E501
        :type publisher: List[object]
        """
        from openapi_server.models.funding_information import FundingInformation
        from openapi_server.models.image import Image
        from openapi_server.models.person import Person
        from openapi_server.models.software import Software
        from openapi_server.models.software_version import SoftwareVersion
        from openapi_server.models.source_code import SourceCode
        from openapi_server.models.visualization import Visualization

          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501
          # noqa: E501

        self.openapi_types = {
            'has_funding': List[FundingInformation],
            'has_documentation': List[str],
            'keywords': List[str],
            'software_requirements': List[str],
            'has_version': List[SoftwareVersion],
            'has_typical_data_source': List[str],
            'has_download_url': List[str],
            'reference_publication': List[str],
            'description': List[str],
            'screenshot': List[Image],
            'type': List[str],
            'has_installation_instructions': List[str],
            'date_created': List[str],
            'compatible_visualization_software': List[Software],
            'contributor': List[Person],
            'has_faq': List[str],
            'logo': List[Image],
            'has_contact_person': List[object],
            'has_purpose': List[str],
            'id': str,
            'has_sample_visualization': List[Visualization],
            'memory_requirements': List[str],
            'identifier': List[str],
            'website': List[str],
            'citation': List[str],
            'author': List[object],
            'processor_requirements': List[str],
            'has_usage_notes': List[str],
            'short_description': List[str],
            'label': List[str],
            'has_execution_command': List[str],
            'has_assumption': List[str],
            'date_published': List[str],
            'license': List[str],
            'operating_systems': List[str],
            'has_source_code': List[SourceCode],
            'has_example': List[str],
            'publisher': List[object]
        }

        self.attribute_map = {
            'has_funding': 'hasFunding',
            'has_documentation': 'hasDocumentation',
            'keywords': 'keywords',
            'software_requirements': 'softwareRequirements',
            'has_version': 'hasVersion',
            'has_typical_data_source': 'hasTypicalDataSource',
            'has_download_url': 'hasDownloadURL',
            'reference_publication': 'referencePublication',
            'description': 'description',
            'screenshot': 'screenshot',
            'type': 'type',
            'has_installation_instructions': 'hasInstallationInstructions',
            'date_created': 'dateCreated',
            'compatible_visualization_software': 'compatibleVisualizationSoftware',
            'contributor': 'contributor',
            'has_faq': 'hasFAQ',
            'logo': 'logo',
            'has_contact_person': 'hasContactPerson',
            'has_purpose': 'hasPurpose',
            'id': 'id',
            'has_sample_visualization': 'hasSampleVisualization',
            'memory_requirements': 'memoryRequirements',
            'identifier': 'identifier',
            'website': 'website',
            'citation': 'citation',
            'author': 'author',
            'processor_requirements': 'processorRequirements',
            'has_usage_notes': 'hasUsageNotes',
            'short_description': 'shortDescription',
            'label': 'label',
            'has_execution_command': 'hasExecutionCommand',
            'has_assumption': 'hasAssumption',
            'date_published': 'datePublished',
            'license': 'license',
            'operating_systems': 'operatingSystems',
            'has_source_code': 'hasSourceCode',
            'has_example': 'hasExample',
            'publisher': 'publisher'
        }

        self._has_funding = has_funding
        self._has_documentation = has_documentation
        self._keywords = keywords
        self._software_requirements = software_requirements
        self._has_version = has_version
        self._has_typical_data_source = has_typical_data_source
        self._has_download_url = has_download_url
        self._reference_publication = reference_publication
        self._description = description
        self._screenshot = screenshot
        self._type = type
        self._has_installation_instructions = has_installation_instructions
        self._date_created = date_created
        self._compatible_visualization_software = compatible_visualization_software
        self._contributor = contributor
        self._has_faq = has_faq
        self._logo = logo
        self._has_contact_person = has_contact_person
        self._has_purpose = has_purpose
        self._id = id
        self._has_sample_visualization = has_sample_visualization
        self._memory_requirements = memory_requirements
        self._identifier = identifier
        self._website = website
        self._citation = citation
        self._author = author
        self._processor_requirements = processor_requirements
        self._has_usage_notes = has_usage_notes
        self._short_description = short_description
        self._label = label
        self._has_execution_command = has_execution_command
        self._has_assumption = has_assumption
        self._date_published = date_published
        self._license = license
        self._operating_systems = operating_systems
        self._has_source_code = has_source_code
        self._has_example = has_example
        self._publisher = publisher

    @classmethod
    def from_dict(cls, dikt) -> 'SoftwareImage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SoftwareImage of this SoftwareImage.  # noqa: E501
        :rtype: SoftwareImage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_funding(self):
        """Gets the has_funding of this SoftwareImage.


        :return: The has_funding of this SoftwareImage.
        :rtype: List[FundingInformation]
        """
        return self._has_funding

    @has_funding.setter
    def has_funding(self, has_funding):
        """Sets the has_funding of this SoftwareImage.


        :param has_funding: The has_funding of this SoftwareImage.
        :type has_funding: List[FundingInformation]
        """

        self._has_funding = has_funding

    @property
    def has_documentation(self):
        """Gets the has_documentation of this SoftwareImage.


        :return: The has_documentation of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this SoftwareImage.


        :param has_documentation: The has_documentation of this SoftwareImage.
        :type has_documentation: List[str]
        """

        self._has_documentation = has_documentation

    @property
    def keywords(self):
        """Gets the keywords of this SoftwareImage.


        :return: The keywords of this SoftwareImage.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this SoftwareImage.


        :param keywords: The keywords of this SoftwareImage.
        :type keywords: List[str]
        """

        self._keywords = keywords

    @property
    def software_requirements(self):
        """Gets the software_requirements of this SoftwareImage.


        :return: The software_requirements of this SoftwareImage.
        :rtype: List[str]
        """
        return self._software_requirements

    @software_requirements.setter
    def software_requirements(self, software_requirements):
        """Sets the software_requirements of this SoftwareImage.


        :param software_requirements: The software_requirements of this SoftwareImage.
        :type software_requirements: List[str]
        """

        self._software_requirements = software_requirements

    @property
    def has_version(self):
        """Gets the has_version of this SoftwareImage.


        :return: The has_version of this SoftwareImage.
        :rtype: List[SoftwareVersion]
        """
        return self._has_version

    @has_version.setter
    def has_version(self, has_version):
        """Sets the has_version of this SoftwareImage.


        :param has_version: The has_version of this SoftwareImage.
        :type has_version: List[SoftwareVersion]
        """

        self._has_version = has_version

    @property
    def has_typical_data_source(self):
        """Gets the has_typical_data_source of this SoftwareImage.


        :return: The has_typical_data_source of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_typical_data_source

    @has_typical_data_source.setter
    def has_typical_data_source(self, has_typical_data_source):
        """Sets the has_typical_data_source of this SoftwareImage.


        :param has_typical_data_source: The has_typical_data_source of this SoftwareImage.
        :type has_typical_data_source: List[str]
        """

        self._has_typical_data_source = has_typical_data_source

    @property
    def has_download_url(self):
        """Gets the has_download_url of this SoftwareImage.


        :return: The has_download_url of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_download_url

    @has_download_url.setter
    def has_download_url(self, has_download_url):
        """Sets the has_download_url of this SoftwareImage.


        :param has_download_url: The has_download_url of this SoftwareImage.
        :type has_download_url: List[str]
        """

        self._has_download_url = has_download_url

    @property
    def reference_publication(self):
        """Gets the reference_publication of this SoftwareImage.


        :return: The reference_publication of this SoftwareImage.
        :rtype: List[str]
        """
        return self._reference_publication

    @reference_publication.setter
    def reference_publication(self, reference_publication):
        """Sets the reference_publication of this SoftwareImage.


        :param reference_publication: The reference_publication of this SoftwareImage.
        :type reference_publication: List[str]
        """

        self._reference_publication = reference_publication

    @property
    def description(self):
        """Gets the description of this SoftwareImage.


        :return: The description of this SoftwareImage.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SoftwareImage.


        :param description: The description of this SoftwareImage.
        :type description: List[str]
        """

        self._description = description

    @property
    def screenshot(self):
        """Gets the screenshot of this SoftwareImage.


        :return: The screenshot of this SoftwareImage.
        :rtype: List[Image]
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """Sets the screenshot of this SoftwareImage.


        :param screenshot: The screenshot of this SoftwareImage.
        :type screenshot: List[Image]
        """

        self._screenshot = screenshot

    @property
    def type(self):
        """Gets the type of this SoftwareImage.


        :return: The type of this SoftwareImage.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SoftwareImage.


        :param type: The type of this SoftwareImage.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_installation_instructions(self):
        """Gets the has_installation_instructions of this SoftwareImage.


        :return: The has_installation_instructions of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_installation_instructions

    @has_installation_instructions.setter
    def has_installation_instructions(self, has_installation_instructions):
        """Sets the has_installation_instructions of this SoftwareImage.


        :param has_installation_instructions: The has_installation_instructions of this SoftwareImage.
        :type has_installation_instructions: List[str]
        """

        self._has_installation_instructions = has_installation_instructions

    @property
    def date_created(self):
        """Gets the date_created of this SoftwareImage.


        :return: The date_created of this SoftwareImage.
        :rtype: List[str]
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SoftwareImage.


        :param date_created: The date_created of this SoftwareImage.
        :type date_created: List[str]
        """

        self._date_created = date_created

    @property
    def compatible_visualization_software(self):
        """Gets the compatible_visualization_software of this SoftwareImage.


        :return: The compatible_visualization_software of this SoftwareImage.
        :rtype: List[Software]
        """
        return self._compatible_visualization_software

    @compatible_visualization_software.setter
    def compatible_visualization_software(self, compatible_visualization_software):
        """Sets the compatible_visualization_software of this SoftwareImage.


        :param compatible_visualization_software: The compatible_visualization_software of this SoftwareImage.
        :type compatible_visualization_software: List[Software]
        """

        self._compatible_visualization_software = compatible_visualization_software

    @property
    def contributor(self):
        """Gets the contributor of this SoftwareImage.


        :return: The contributor of this SoftwareImage.
        :rtype: List[Person]
        """
        return self._contributor

    @contributor.setter
    def contributor(self, contributor):
        """Sets the contributor of this SoftwareImage.


        :param contributor: The contributor of this SoftwareImage.
        :type contributor: List[Person]
        """

        self._contributor = contributor

    @property
    def has_faq(self):
        """Gets the has_faq of this SoftwareImage.


        :return: The has_faq of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_faq

    @has_faq.setter
    def has_faq(self, has_faq):
        """Sets the has_faq of this SoftwareImage.


        :param has_faq: The has_faq of this SoftwareImage.
        :type has_faq: List[str]
        """

        self._has_faq = has_faq

    @property
    def logo(self):
        """Gets the logo of this SoftwareImage.


        :return: The logo of this SoftwareImage.
        :rtype: List[Image]
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this SoftwareImage.


        :param logo: The logo of this SoftwareImage.
        :type logo: List[Image]
        """

        self._logo = logo

    @property
    def has_contact_person(self):
        """Gets the has_contact_person of this SoftwareImage.


        :return: The has_contact_person of this SoftwareImage.
        :rtype: List[object]
        """
        return self._has_contact_person

    @has_contact_person.setter
    def has_contact_person(self, has_contact_person):
        """Sets the has_contact_person of this SoftwareImage.


        :param has_contact_person: The has_contact_person of this SoftwareImage.
        :type has_contact_person: List[object]
        """

        self._has_contact_person = has_contact_person

    @property
    def has_purpose(self):
        """Gets the has_purpose of this SoftwareImage.


        :return: The has_purpose of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_purpose

    @has_purpose.setter
    def has_purpose(self, has_purpose):
        """Sets the has_purpose of this SoftwareImage.


        :param has_purpose: The has_purpose of this SoftwareImage.
        :type has_purpose: List[str]
        """

        self._has_purpose = has_purpose

    @property
    def id(self):
        """Gets the id of this SoftwareImage.


        :return: The id of this SoftwareImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SoftwareImage.


        :param id: The id of this SoftwareImage.
        :type id: str
        """

        self._id = id

    @property
    def has_sample_visualization(self):
        """Gets the has_sample_visualization of this SoftwareImage.


        :return: The has_sample_visualization of this SoftwareImage.
        :rtype: List[Visualization]
        """
        return self._has_sample_visualization

    @has_sample_visualization.setter
    def has_sample_visualization(self, has_sample_visualization):
        """Sets the has_sample_visualization of this SoftwareImage.


        :param has_sample_visualization: The has_sample_visualization of this SoftwareImage.
        :type has_sample_visualization: List[Visualization]
        """

        self._has_sample_visualization = has_sample_visualization

    @property
    def memory_requirements(self):
        """Gets the memory_requirements of this SoftwareImage.


        :return: The memory_requirements of this SoftwareImage.
        :rtype: List[str]
        """
        return self._memory_requirements

    @memory_requirements.setter
    def memory_requirements(self, memory_requirements):
        """Sets the memory_requirements of this SoftwareImage.


        :param memory_requirements: The memory_requirements of this SoftwareImage.
        :type memory_requirements: List[str]
        """

        self._memory_requirements = memory_requirements

    @property
    def identifier(self):
        """Gets the identifier of this SoftwareImage.


        :return: The identifier of this SoftwareImage.
        :rtype: List[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this SoftwareImage.


        :param identifier: The identifier of this SoftwareImage.
        :type identifier: List[str]
        """

        self._identifier = identifier

    @property
    def website(self):
        """Gets the website of this SoftwareImage.


        :return: The website of this SoftwareImage.
        :rtype: List[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this SoftwareImage.


        :param website: The website of this SoftwareImage.
        :type website: List[str]
        """

        self._website = website

    @property
    def citation(self):
        """Gets the citation of this SoftwareImage.


        :return: The citation of this SoftwareImage.
        :rtype: List[str]
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this SoftwareImage.


        :param citation: The citation of this SoftwareImage.
        :type citation: List[str]
        """

        self._citation = citation

    @property
    def author(self):
        """Gets the author of this SoftwareImage.


        :return: The author of this SoftwareImage.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this SoftwareImage.


        :param author: The author of this SoftwareImage.
        :type author: List[object]
        """

        self._author = author

    @property
    def processor_requirements(self):
        """Gets the processor_requirements of this SoftwareImage.


        :return: The processor_requirements of this SoftwareImage.
        :rtype: List[str]
        """
        return self._processor_requirements

    @processor_requirements.setter
    def processor_requirements(self, processor_requirements):
        """Sets the processor_requirements of this SoftwareImage.


        :param processor_requirements: The processor_requirements of this SoftwareImage.
        :type processor_requirements: List[str]
        """

        self._processor_requirements = processor_requirements

    @property
    def has_usage_notes(self):
        """Gets the has_usage_notes of this SoftwareImage.


        :return: The has_usage_notes of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_usage_notes

    @has_usage_notes.setter
    def has_usage_notes(self, has_usage_notes):
        """Sets the has_usage_notes of this SoftwareImage.


        :param has_usage_notes: The has_usage_notes of this SoftwareImage.
        :type has_usage_notes: List[str]
        """

        self._has_usage_notes = has_usage_notes

    @property
    def short_description(self):
        """Gets the short_description of this SoftwareImage.


        :return: The short_description of this SoftwareImage.
        :rtype: List[str]
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this SoftwareImage.


        :param short_description: The short_description of this SoftwareImage.
        :type short_description: List[str]
        """

        self._short_description = short_description

    @property
    def label(self):
        """Gets the label of this SoftwareImage.


        :return: The label of this SoftwareImage.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SoftwareImage.


        :param label: The label of this SoftwareImage.
        :type label: List[str]
        """

        self._label = label

    @property
    def has_execution_command(self):
        """Gets the has_execution_command of this SoftwareImage.


        :return: The has_execution_command of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_execution_command

    @has_execution_command.setter
    def has_execution_command(self, has_execution_command):
        """Sets the has_execution_command of this SoftwareImage.


        :param has_execution_command: The has_execution_command of this SoftwareImage.
        :type has_execution_command: List[str]
        """

        self._has_execution_command = has_execution_command

    @property
    def has_assumption(self):
        """Gets the has_assumption of this SoftwareImage.


        :return: The has_assumption of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_assumption

    @has_assumption.setter
    def has_assumption(self, has_assumption):
        """Sets the has_assumption of this SoftwareImage.


        :param has_assumption: The has_assumption of this SoftwareImage.
        :type has_assumption: List[str]
        """

        self._has_assumption = has_assumption

    @property
    def date_published(self):
        """Gets the date_published of this SoftwareImage.


        :return: The date_published of this SoftwareImage.
        :rtype: List[str]
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this SoftwareImage.


        :param date_published: The date_published of this SoftwareImage.
        :type date_published: List[str]
        """

        self._date_published = date_published

    @property
    def license(self):
        """Gets the license of this SoftwareImage.


        :return: The license of this SoftwareImage.
        :rtype: List[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this SoftwareImage.


        :param license: The license of this SoftwareImage.
        :type license: List[str]
        """

        self._license = license

    @property
    def operating_systems(self):
        """Gets the operating_systems of this SoftwareImage.


        :return: The operating_systems of this SoftwareImage.
        :rtype: List[str]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """Sets the operating_systems of this SoftwareImage.


        :param operating_systems: The operating_systems of this SoftwareImage.
        :type operating_systems: List[str]
        """

        self._operating_systems = operating_systems

    @property
    def has_source_code(self):
        """Gets the has_source_code of this SoftwareImage.


        :return: The has_source_code of this SoftwareImage.
        :rtype: List[SourceCode]
        """
        return self._has_source_code

    @has_source_code.setter
    def has_source_code(self, has_source_code):
        """Sets the has_source_code of this SoftwareImage.


        :param has_source_code: The has_source_code of this SoftwareImage.
        :type has_source_code: List[SourceCode]
        """

        self._has_source_code = has_source_code

    @property
    def has_example(self):
        """Gets the has_example of this SoftwareImage.


        :return: The has_example of this SoftwareImage.
        :rtype: List[str]
        """
        return self._has_example

    @has_example.setter
    def has_example(self, has_example):
        """Sets the has_example of this SoftwareImage.


        :param has_example: The has_example of this SoftwareImage.
        :type has_example: List[str]
        """

        self._has_example = has_example

    @property
    def publisher(self):
        """Gets the publisher of this SoftwareImage.


        :return: The publisher of this SoftwareImage.
        :rtype: List[object]
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this SoftwareImage.


        :param publisher: The publisher of this SoftwareImage.
        :type publisher: List[object]
        """

        self._publisher = publisher
