import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VARIABLE_TYPE_NAME, VARIABLE_TYPE_URI

from openapi_server.models.variable import Variable  # noqa: E501
from openapi_server import util

def variables_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Variable

    Gets a list of all instances of Variable (more information in https://w3id.org/okn/o/sd#Variable) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Variable]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_id_delete(id, user):  # noqa: E501
    """Delete an existing Variable

    Delete an existing Variable (more information in https://w3id.org/okn/o/sd#Variable) # noqa: E501

    :param id: The ID of the Variable to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_id_get(id, username=None):  # noqa: E501
    """Get a single Variable by its id

    Gets the details of a given Variable (more information in https://w3id.org/okn/o/sd#Variable) # noqa: E501

    :param id: The ID of the Variable to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Variable
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_id_put(id, user, variable=None):  # noqa: E501
    """Update an existing Variable

    Updates an existing Variable (more information in https://w3id.org/okn/o/sd#Variable) # noqa: E501

    :param id: The ID of the Variable to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param variable: An old Variableto be updated
    :type variable: dict | bytes

    :rtype: Variable
    """

    if connexion.request.is_json:
        variable = Variable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=variable,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_post(user, variable=None):  # noqa: E501
    """Create one Variable

    Create a new instance of Variable (more information in https://w3id.org/okn/o/sd#Variable) # noqa: E501

    :param user: Username
    :type user: str
    :param variable: Information about the Variableto be created
    :type variable: dict | bytes

    :rtype: Variable
    """

    if connexion.request.is_json:
        variable = Variable.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=variable,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)
