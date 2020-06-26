import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GEOSHAPE_TYPE_NAME, GEOSHAPE_TYPE_URI

from openapi_server.models.geo_shape import GeoShape  # noqa: E501
from openapi_server import util

def geoshapes_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GeoShape

    Gets a list of all instances of GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GeoShape]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_id_delete(id, user):  # noqa: E501
    """Delete an existing GeoShape

    Delete an existing GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape) # noqa: E501

    :param id: The ID of the GeoShape to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_id_get(id, username=None):  # noqa: E501
    """Get a single GeoShape by its id

    Gets the details of a given GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape) # noqa: E501

    :param id: The ID of the GeoShape to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: GeoShape
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_id_put(id, user, geo_shape=None):  # noqa: E501
    """Update an existing GeoShape

    Updates an existing GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape) # noqa: E501

    :param id: The ID of the GeoShape to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param geo_shape: An old GeoShapeto be updated
    :type geo_shape: dict | bytes

    :rtype: GeoShape
    """

    if connexion.request.is_json:
        geo_shape = GeoShape.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=geo_shape,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)

def geoshapes_post(user, geo_shape=None):  # noqa: E501
    """Create one GeoShape

    Create a new instance of GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape) # noqa: E501

    :param user: Username
    :type user: str
    :param geo_shape: Information about the GeoShapeto be created
    :type geo_shape: dict | bytes

    :rtype: GeoShape
    """

    if connexion.request.is_json:
        geo_shape = GeoShape.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=geo_shape,
        rdf_type_uri=GEOSHAPE_TYPE_URI,
        rdf_type_name=GEOSHAPE_TYPE_NAME, 
        kls=GeoShape)
