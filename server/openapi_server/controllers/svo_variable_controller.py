import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SVOVARIABLE_TYPE_NAME, SVOVARIABLE_TYPE_URI

from openapi_server.models.svo_variable import SVOVariable  # noqa: E501
from openapi_server import util

def svovariables_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SVOVariable

    Gets a list of all instances of SVOVariable (more information in https://w3id.org/okn/o/sd#SVOVariable) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SVOVariable]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_id_delete(id, user):  # noqa: E501
    """Delete an existing SVOVariable

    Delete an existing SVOVariable (more information in https://w3id.org/okn/o/sd#SVOVariable) # noqa: E501

    :param id: The ID of the SVOVariable to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_id_get(id, username=None):  # noqa: E501
    """Get a single SVOVariable by its id

    Gets the details of a given SVOVariable (more information in https://w3id.org/okn/o/sd#SVOVariable) # noqa: E501

    :param id: The ID of the SVOVariable to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SVOVariable
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_id_put(id, user, svo_variable=None):  # noqa: E501
    """Update an existing SVOVariable

    Updates an existing SVOVariable (more information in https://w3id.org/okn/o/sd#SVOVariable) # noqa: E501

    :param id: The ID of the SVOVariable to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param svo_variable: An old SVOVariableto be updated
    :type svo_variable: dict | bytes

    :rtype: SVOVariable
    """

    if connexion.request.is_json:
        svo_variable = SVOVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=svo_variable,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_post(user, svo_variable=None):  # noqa: E501
    """Create one SVOVariable

    Create a new instance of SVOVariable (more information in https://w3id.org/okn/o/sd#SVOVariable) # noqa: E501

    :param user: Username
    :type user: str
    :param svo_variable: Information about the SVOVariableto be created
    :type svo_variable: dict | bytes

    :rtype: SVOVariable
    """

    if connexion.request.is_json:
        svo_variable = SVOVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=svo_variable,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)
