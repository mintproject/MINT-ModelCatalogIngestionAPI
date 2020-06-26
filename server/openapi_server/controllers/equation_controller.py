import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EQUATION_TYPE_NAME, EQUATION_TYPE_URI

from openapi_server.models.equation import Equation  # noqa: E501
from openapi_server import util

def equations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Equation

    Gets a list of all instances of Equation (more information in https://w3id.org/okn/o/sdm#Equation) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Equation]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_id_delete(id, user):  # noqa: E501
    """Delete an existing Equation

    Delete an existing Equation (more information in https://w3id.org/okn/o/sdm#Equation) # noqa: E501

    :param id: The ID of the Equation to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_id_get(id, username=None):  # noqa: E501
    """Get a single Equation by its id

    Gets the details of a given Equation (more information in https://w3id.org/okn/o/sdm#Equation) # noqa: E501

    :param id: The ID of the Equation to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Equation
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_id_put(id, user, equation=None):  # noqa: E501
    """Update an existing Equation

    Updates an existing Equation (more information in https://w3id.org/okn/o/sdm#Equation) # noqa: E501

    :param id: The ID of the Equation to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param equation: An old Equationto be updated
    :type equation: dict | bytes

    :rtype: Equation
    """

    if connexion.request.is_json:
        equation = Equation.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=equation,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_post(user, equation=None):  # noqa: E501
    """Create one Equation

    Create a new instance of Equation (more information in https://w3id.org/okn/o/sdm#Equation) # noqa: E501

    :param user: Username
    :type user: str
    :param equation: Information about the Equationto be created
    :type equation: dict | bytes

    :rtype: Equation
    """

    if connexion.request.is_json:
        equation = Equation.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=equation,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)
