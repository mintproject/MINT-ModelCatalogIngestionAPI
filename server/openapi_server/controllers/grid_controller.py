import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GRID_TYPE_NAME, GRID_TYPE_URI

from openapi_server.models.grid import Grid  # noqa: E501
from openapi_server import util

def grids_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Grid

    Gets a list of all instances of Grid (more information in https://w3id.org/okn/o/sdm#Grid) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Grid]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_id_delete(id, user):  # noqa: E501
    """Delete an existing Grid

    Delete an existing Grid (more information in https://w3id.org/okn/o/sdm#Grid) # noqa: E501

    :param id: The ID of the Grid to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_id_get(id, username=None):  # noqa: E501
    """Get a single Grid by its id

    Gets the details of a given Grid (more information in https://w3id.org/okn/o/sdm#Grid) # noqa: E501

    :param id: The ID of the Grid to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Grid
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_id_put(id, user, grid=None):  # noqa: E501
    """Update an existing Grid

    Updates an existing Grid (more information in https://w3id.org/okn/o/sdm#Grid) # noqa: E501

    :param id: The ID of the Grid to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param grid: An old Gridto be updated
    :type grid: dict | bytes

    :rtype: Grid
    """

    if connexion.request.is_json:
        grid = Grid.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=grid,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)

def grids_post(user, grid=None):  # noqa: E501
    """Create one Grid

    Create a new instance of Grid (more information in https://w3id.org/okn/o/sdm#Grid) # noqa: E501

    :param user: Username
    :type user: str
    :param grid: Information about the Gridto be created
    :type grid: dict | bytes

    :rtype: Grid
    """

    if connexion.request.is_json:
        grid = Grid.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=grid,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME, 
        kls=Grid)
