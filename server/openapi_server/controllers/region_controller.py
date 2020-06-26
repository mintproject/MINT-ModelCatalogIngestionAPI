import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import REGION_TYPE_NAME, REGION_TYPE_URI

from openapi_server.models.region import Region  # noqa: E501
from openapi_server import util

def regions_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Region

    Gets a list of all instances of Region (more information in https://w3id.org/okn/o/sdm#Region) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Region]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_id_delete(id, user):  # noqa: E501
    """Delete an existing Region

    Delete an existing Region (more information in https://w3id.org/okn/o/sdm#Region) # noqa: E501

    :param id: The ID of the Region to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_id_get(id, username=None):  # noqa: E501
    """Get a single Region by its id

    Gets the details of a given Region (more information in https://w3id.org/okn/o/sdm#Region) # noqa: E501

    :param id: The ID of the Region to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Region
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_id_put(id, user, region=None):  # noqa: E501
    """Update an existing Region

    Updates an existing Region (more information in https://w3id.org/okn/o/sdm#Region) # noqa: E501

    :param id: The ID of the Region to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param region: An old Regionto be updated
    :type region: dict | bytes

    :rtype: Region
    """

    if connexion.request.is_json:
        region = Region.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=region,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_post(user, region=None):  # noqa: E501
    """Create one Region

    Create a new instance of Region (more information in https://w3id.org/okn/o/sdm#Region) # noqa: E501

    :param user: Username
    :type user: str
    :param region: Information about the Regionto be created
    :type region: dict | bytes

    :rtype: Region
    """

    if connexion.request.is_json:
        region = Region.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=region,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)
