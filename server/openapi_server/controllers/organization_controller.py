import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ORGANIZATION_TYPE_NAME, ORGANIZATION_TYPE_URI

from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server import util

def organizations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Organization

    Gets a list of all instances of Organization (more information in https://w3id.org/okn/o/sd#Organization) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Organization]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_id_delete(id, user):  # noqa: E501
    """Delete an existing Organization

    Delete an existing Organization (more information in https://w3id.org/okn/o/sd#Organization) # noqa: E501

    :param id: The ID of the Organization to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_id_get(id, username=None):  # noqa: E501
    """Get a single Organization by its id

    Gets the details of a given Organization (more information in https://w3id.org/okn/o/sd#Organization) # noqa: E501

    :param id: The ID of the Organization to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Organization
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_id_put(id, user, organization=None):  # noqa: E501
    """Update an existing Organization

    Updates an existing Organization (more information in https://w3id.org/okn/o/sd#Organization) # noqa: E501

    :param id: The ID of the Organization to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param organization: An old Organizationto be updated
    :type organization: dict | bytes

    :rtype: Organization
    """

    if connexion.request.is_json:
        organization = Organization.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=organization,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)

def organizations_post(user, organization=None):  # noqa: E501
    """Create one Organization

    Create a new instance of Organization (more information in https://w3id.org/okn/o/sd#Organization) # noqa: E501

    :param user: Username
    :type user: str
    :param organization: Information about the Organizationto be created
    :type organization: dict | bytes

    :rtype: Organization
    """

    if connexion.request.is_json:
        organization = Organization.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=organization,
        rdf_type_uri=ORGANIZATION_TYPE_URI,
        rdf_type_name=ORGANIZATION_TYPE_NAME, 
        kls=Organization)
