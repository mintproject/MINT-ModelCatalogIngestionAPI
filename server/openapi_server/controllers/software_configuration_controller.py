import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOFTWARECONFIGURATION_TYPE_NAME, SOFTWARECONFIGURATION_TYPE_URI

from openapi_server.models.software_configuration import SoftwareConfiguration  # noqa: E501
from openapi_server import util

def softwareconfigurations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoftwareConfiguration

    Gets a list of all instances of SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoftwareConfiguration]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_id_delete(id, user):  # noqa: E501
    """Delete an existing SoftwareConfiguration

    Delete an existing SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration) # noqa: E501

    :param id: The ID of the SoftwareConfiguration to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_id_get(id, username=None):  # noqa: E501
    """Get a single SoftwareConfiguration by its id

    Gets the details of a given SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration) # noqa: E501

    :param id: The ID of the SoftwareConfiguration to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SoftwareConfiguration
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_id_put(id, user, software_configuration=None):  # noqa: E501
    """Update an existing SoftwareConfiguration

    Updates an existing SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration) # noqa: E501

    :param id: The ID of the SoftwareConfiguration to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param software_configuration: An old SoftwareConfigurationto be updated
    :type software_configuration: dict | bytes

    :rtype: SoftwareConfiguration
    """

    if connexion.request.is_json:
        software_configuration = SoftwareConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=software_configuration,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)

def softwareconfigurations_post(user, software_configuration=None):  # noqa: E501
    """Create one SoftwareConfiguration

    Create a new instance of SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration) # noqa: E501

    :param user: Username
    :type user: str
    :param software_configuration: Information about the SoftwareConfigurationto be created
    :type software_configuration: dict | bytes

    :rtype: SoftwareConfiguration
    """

    if connexion.request.is_json:
        software_configuration = SoftwareConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=software_configuration,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration)
