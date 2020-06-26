import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NUMERICALINDEX_TYPE_NAME, NUMERICALINDEX_TYPE_URI

from openapi_server.models.numerical_index import NumericalIndex  # noqa: E501
from openapi_server import util

def numericalindexs_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NumericalIndex

    Gets a list of all instances of NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NumericalIndex]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_id_delete(id, user):  # noqa: E501
    """Delete an existing NumericalIndex

    Delete an existing NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex) # noqa: E501

    :param id: The ID of the NumericalIndex to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_id_get(id, username=None):  # noqa: E501
    """Get a single NumericalIndex by its id

    Gets the details of a given NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex) # noqa: E501

    :param id: The ID of the NumericalIndex to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: NumericalIndex
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_id_put(id, user, numerical_index=None):  # noqa: E501
    """Update an existing NumericalIndex

    Updates an existing NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex) # noqa: E501

    :param id: The ID of the NumericalIndex to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param numerical_index: An old NumericalIndexto be updated
    :type numerical_index: dict | bytes

    :rtype: NumericalIndex
    """

    if connexion.request.is_json:
        numerical_index = NumericalIndex.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=numerical_index,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)

def numericalindexs_post(user, numerical_index=None):  # noqa: E501
    """Create one NumericalIndex

    Create a new instance of NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex) # noqa: E501

    :param user: Username
    :type user: str
    :param numerical_index: Information about the NumericalIndexto be created
    :type numerical_index: dict | bytes

    :rtype: NumericalIndex
    """

    if connexion.request.is_json:
        numerical_index = NumericalIndex.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=numerical_index,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex)
