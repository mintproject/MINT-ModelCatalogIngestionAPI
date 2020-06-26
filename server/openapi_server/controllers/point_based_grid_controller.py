import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POINTBASEDGRID_TYPE_NAME, POINTBASEDGRID_TYPE_URI

from openapi_server.models.point_based_grid import PointBasedGrid  # noqa: E501
from openapi_server import util

def pointbasedgrids_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PointBasedGrid

    Gets a list of all instances of PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PointBasedGrid]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_id_delete(id, user):  # noqa: E501
    """Delete an existing PointBasedGrid

    Delete an existing PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid) # noqa: E501

    :param id: The ID of the PointBasedGrid to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_id_get(id, username=None):  # noqa: E501
    """Get a single PointBasedGrid by its id

    Gets the details of a given PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid) # noqa: E501

    :param id: The ID of the PointBasedGrid to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: PointBasedGrid
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_id_put(id, user, point_based_grid=None):  # noqa: E501
    """Update an existing PointBasedGrid

    Updates an existing PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid) # noqa: E501

    :param id: The ID of the PointBasedGrid to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param point_based_grid: An old PointBasedGridto be updated
    :type point_based_grid: dict | bytes

    :rtype: PointBasedGrid
    """

    if connexion.request.is_json:
        point_based_grid = PointBasedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=point_based_grid,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)

def pointbasedgrids_post(user, point_based_grid=None):  # noqa: E501
    """Create one PointBasedGrid

    Create a new instance of PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid) # noqa: E501

    :param user: Username
    :type user: str
    :param point_based_grid: Information about the PointBasedGridto be created
    :type point_based_grid: dict | bytes

    :rtype: PointBasedGrid
    """

    if connexion.request.is_json:
        point_based_grid = PointBasedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=point_based_grid,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME, 
        kls=PointBasedGrid)
