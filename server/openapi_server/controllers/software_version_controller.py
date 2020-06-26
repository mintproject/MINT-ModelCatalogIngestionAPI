import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOFTWAREVERSION_TYPE_NAME, SOFTWAREVERSION_TYPE_URI

from openapi_server.models.software_version import SoftwareVersion  # noqa: E501
from openapi_server import util

def softwareversions_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoftwareVersion

    Gets a list of all instances of SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoftwareVersion]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_id_delete(id, user):  # noqa: E501
    """Delete an existing SoftwareVersion

    Delete an existing SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion) # noqa: E501

    :param id: The ID of the SoftwareVersion to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_id_get(id, username=None):  # noqa: E501
    """Get a single SoftwareVersion by its id

    Gets the details of a given SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion) # noqa: E501

    :param id: The ID of the SoftwareVersion to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SoftwareVersion
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_id_put(id, user, software_version=None):  # noqa: E501
    """Update an existing SoftwareVersion

    Updates an existing SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion) # noqa: E501

    :param id: The ID of the SoftwareVersion to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param software_version: An old SoftwareVersionto be updated
    :type software_version: dict | bytes

    :rtype: SoftwareVersion
    """

    if connexion.request.is_json:
        software_version = SoftwareVersion.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=software_version,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)

def softwareversions_post(user, software_version=None):  # noqa: E501
    """Create one SoftwareVersion

    Create a new instance of SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion) # noqa: E501

    :param user: Username
    :type user: str
    :param software_version: Information about the SoftwareVersionto be created
    :type software_version: dict | bytes

    :rtype: SoftwareVersion
    """

    if connexion.request.is_json:
        software_version = SoftwareVersion.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=software_version,
        rdf_type_uri=SOFTWAREVERSION_TYPE_URI,
        rdf_type_name=SOFTWAREVERSION_TYPE_NAME, 
        kls=SoftwareVersion)
