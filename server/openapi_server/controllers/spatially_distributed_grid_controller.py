import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, SPATIALLYDISTRIBUTEDGRID_TYPE_URI

from openapi_server.models.spatially_distributed_grid import SpatiallyDistributedGrid  # noqa: E501
from openapi_server import util

def spatiallydistributedgrids_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpatiallyDistributedGrid

    Gets a list of all instances of SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpatiallyDistributedGrid]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_id_delete(id, user):  # noqa: E501
    """Delete an existing SpatiallyDistributedGrid

    Delete an existing SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid) # noqa: E501

    :param id: The ID of the SpatiallyDistributedGrid to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_id_get(id, username=None):  # noqa: E501
    """Get a single SpatiallyDistributedGrid by its id

    Gets the details of a given SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid) # noqa: E501

    :param id: The ID of the SpatiallyDistributedGrid to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SpatiallyDistributedGrid
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=None):  # noqa: E501
    """Update an existing SpatiallyDistributedGrid

    Updates an existing SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid) # noqa: E501

    :param id: The ID of the SpatiallyDistributedGrid to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param spatially_distributed_grid: An old SpatiallyDistributedGridto be updated
    :type spatially_distributed_grid: dict | bytes

    :rtype: SpatiallyDistributedGrid
    """

    if connexion.request.is_json:
        spatially_distributed_grid = SpatiallyDistributedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=spatially_distributed_grid,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)

def spatiallydistributedgrids_post(user, spatially_distributed_grid=None):  # noqa: E501
    """Create one SpatiallyDistributedGrid

    Create a new instance of SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid) # noqa: E501

    :param user: Username
    :type user: str
    :param spatially_distributed_grid: Information about the SpatiallyDistributedGridto be created
    :type spatially_distributed_grid: dict | bytes

    :rtype: SpatiallyDistributedGrid
    """

    if connexion.request.is_json:
        spatially_distributed_grid = SpatiallyDistributedGrid.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=spatially_distributed_grid,
        rdf_type_uri=SPATIALLYDISTRIBUTEDGRID_TYPE_URI,
        rdf_type_name=SPATIALLYDISTRIBUTEDGRID_TYPE_NAME, 
        kls=SpatiallyDistributedGrid)
