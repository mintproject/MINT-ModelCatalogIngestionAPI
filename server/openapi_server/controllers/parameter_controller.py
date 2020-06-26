import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PARAMETER_TYPE_NAME, PARAMETER_TYPE_URI

from openapi_server.models.parameter import Parameter  # noqa: E501
from openapi_server import util

def parameters_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Parameter

    Gets a list of all instances of Parameter (more information in https://w3id.org/okn/o/sd#Parameter) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Parameter]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_id_delete(id, user):  # noqa: E501
    """Delete an existing Parameter

    Delete an existing Parameter (more information in https://w3id.org/okn/o/sd#Parameter) # noqa: E501

    :param id: The ID of the Parameter to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_id_get(id, username=None):  # noqa: E501
    """Get a single Parameter by its id

    Gets the details of a given Parameter (more information in https://w3id.org/okn/o/sd#Parameter) # noqa: E501

    :param id: The ID of the Parameter to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Parameter
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_id_put(id, user, parameter=None):  # noqa: E501
    """Update an existing Parameter

    Updates an existing Parameter (more information in https://w3id.org/okn/o/sd#Parameter) # noqa: E501

    :param id: The ID of the Parameter to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param parameter: An old Parameterto be updated
    :type parameter: dict | bytes

    :rtype: Parameter
    """

    if connexion.request.is_json:
        parameter = Parameter.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=parameter,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_post(user, parameter=None):  # noqa: E501
    """Create one Parameter

    Create a new instance of Parameter (more information in https://w3id.org/okn/o/sd#Parameter) # noqa: E501

    :param user: Username
    :type user: str
    :param parameter: Information about the Parameterto be created
    :type parameter: dict | bytes

    :rtype: Parameter
    """

    if connexion.request.is_json:
        parameter = Parameter.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=parameter,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)
