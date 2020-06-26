import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GEOCOORDINATES_TYPE_NAME, GEOCOORDINATES_TYPE_URI

from openapi_server.models.geo_coordinates import GeoCoordinates  # noqa: E501
from openapi_server import util

def geocoordinatess_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GeoCoordinates

    Gets a list of all instances of GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GeoCoordinates]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_id_delete(id, user):  # noqa: E501
    """Delete an existing GeoCoordinates

    Delete an existing GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates) # noqa: E501

    :param id: The ID of the GeoCoordinates to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_id_get(id, username=None):  # noqa: E501
    """Get a single GeoCoordinates by its id

    Gets the details of a given GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates) # noqa: E501

    :param id: The ID of the GeoCoordinates to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: GeoCoordinates
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_id_put(id, user, geo_coordinates=None):  # noqa: E501
    """Update an existing GeoCoordinates

    Updates an existing GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates) # noqa: E501

    :param id: The ID of the GeoCoordinates to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param geo_coordinates: An old GeoCoordinatesto be updated
    :type geo_coordinates: dict | bytes

    :rtype: GeoCoordinates
    """

    if connexion.request.is_json:
        geo_coordinates = GeoCoordinates.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=geo_coordinates,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)

def geocoordinatess_post(user, geo_coordinates=None):  # noqa: E501
    """Create one GeoCoordinates

    Create a new instance of GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates) # noqa: E501

    :param user: Username
    :type user: str
    :param geo_coordinates: Information about the GeoCoordinatesto be created
    :type geo_coordinates: dict | bytes

    :rtype: GeoCoordinates
    """

    if connexion.request.is_json:
        geo_coordinates = GeoCoordinates.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=geo_coordinates,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates)
