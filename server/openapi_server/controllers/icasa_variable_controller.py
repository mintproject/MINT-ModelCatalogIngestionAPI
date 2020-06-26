import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ICASAVARIABLE_TYPE_NAME, ICASAVARIABLE_TYPE_URI

from openapi_server.models.icasa_variable import ICASAVariable  # noqa: E501
from openapi_server import util

def icasavariables_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ICASAVariable

    Gets a list of all instances of ICASAVariable (more information in https://w3id.org/okn/o/sd#ICASAVariable) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ICASAVariable]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_id_delete(id, user):  # noqa: E501
    """Delete an existing ICASAVariable

    Delete an existing ICASAVariable (more information in https://w3id.org/okn/o/sd#ICASAVariable) # noqa: E501

    :param id: The ID of the ICASAVariable to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_id_get(id, username=None):  # noqa: E501
    """Get a single ICASAVariable by its id

    Gets the details of a given ICASAVariable (more information in https://w3id.org/okn/o/sd#ICASAVariable) # noqa: E501

    :param id: The ID of the ICASAVariable to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: ICASAVariable
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_id_put(id, user, icasa_variable=None):  # noqa: E501
    """Update an existing ICASAVariable

    Updates an existing ICASAVariable (more information in https://w3id.org/okn/o/sd#ICASAVariable) # noqa: E501

    :param id: The ID of the ICASAVariable to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param icasa_variable: An old ICASAVariableto be updated
    :type icasa_variable: dict | bytes

    :rtype: ICASAVariable
    """

    if connexion.request.is_json:
        icasa_variable = ICASAVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=icasa_variable,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_post(user, icasa_variable=None):  # noqa: E501
    """Create one ICASAVariable

    Create a new instance of ICASAVariable (more information in https://w3id.org/okn/o/sd#ICASAVariable) # noqa: E501

    :param user: Username
    :type user: str
    :param icasa_variable: Information about the ICASAVariableto be created
    :type icasa_variable: dict | bytes

    :rtype: ICASAVariable
    """

    if connexion.request.is_json:
        icasa_variable = ICASAVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=icasa_variable,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)
