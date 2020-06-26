import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STANDARDVARIABLE_TYPE_NAME, STANDARDVARIABLE_TYPE_URI

from openapi_server.models.standard_variable import StandardVariable  # noqa: E501
from openapi_server import util

def standardvariables_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of StandardVariable

    Gets a list of all instances of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[StandardVariable]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_id_delete(id, user):  # noqa: E501
    """Delete an existing StandardVariable

    Delete an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable) # noqa: E501

    :param id: The ID of the StandardVariable to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_id_get(id, username=None):  # noqa: E501
    """Get a single StandardVariable by its id

    Gets the details of a given StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable) # noqa: E501

    :param id: The ID of the StandardVariable to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: StandardVariable
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_id_put(id, user, standard_variable=None):  # noqa: E501
    """Update an existing StandardVariable

    Updates an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable) # noqa: E501

    :param id: The ID of the StandardVariable to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param standard_variable: An old StandardVariableto be updated
    :type standard_variable: dict | bytes

    :rtype: StandardVariable
    """

    if connexion.request.is_json:
        standard_variable = StandardVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=standard_variable,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_post(user, standard_variable=None):  # noqa: E501
    """Create one StandardVariable

    Create a new instance of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable) # noqa: E501

    :param user: Username
    :type user: str
    :param standard_variable: Information about the StandardVariableto be created
    :type standard_variable: dict | bytes

    :rtype: StandardVariable
    """

    if connexion.request.is_json:
        standard_variable = StandardVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=standard_variable,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)
