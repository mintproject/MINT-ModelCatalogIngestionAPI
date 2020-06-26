import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPATIALRESOLUTION_TYPE_NAME, SPATIALRESOLUTION_TYPE_URI

from openapi_server.models.spatial_resolution import SpatialResolution  # noqa: E501
from openapi_server import util

def spatialresolutions_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpatialResolution

    Gets a list of all instances of SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpatialResolution]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_id_delete(id, user):  # noqa: E501
    """Delete an existing SpatialResolution

    Delete an existing SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution) # noqa: E501

    :param id: The ID of the SpatialResolution to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_id_get(id, username=None):  # noqa: E501
    """Get a single SpatialResolution by its id

    Gets the details of a given SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution) # noqa: E501

    :param id: The ID of the SpatialResolution to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SpatialResolution
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_id_put(id, user, spatial_resolution=None):  # noqa: E501
    """Update an existing SpatialResolution

    Updates an existing SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution) # noqa: E501

    :param id: The ID of the SpatialResolution to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param spatial_resolution: An old SpatialResolutionto be updated
    :type spatial_resolution: dict | bytes

    :rtype: SpatialResolution
    """

    if connexion.request.is_json:
        spatial_resolution = SpatialResolution.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=spatial_resolution,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)

def spatialresolutions_post(user, spatial_resolution=None):  # noqa: E501
    """Create one SpatialResolution

    Create a new instance of SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution) # noqa: E501

    :param user: Username
    :type user: str
    :param spatial_resolution: Information about the SpatialResolutionto be created
    :type spatial_resolution: dict | bytes

    :rtype: SpatialResolution
    """

    if connexion.request.is_json:
        spatial_resolution = SpatialResolution.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=spatial_resolution,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution)
