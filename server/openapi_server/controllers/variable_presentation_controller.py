import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VARIABLEPRESENTATION_TYPE_NAME, VARIABLEPRESENTATION_TYPE_URI

from openapi_server.models.variable_presentation import VariablePresentation  # noqa: E501
from openapi_server import util

def variablepresentations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VariablePresentation

    Gets a list of all instances of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VariablePresentation]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_id_delete(id, user):  # noqa: E501
    """Delete an existing VariablePresentation

    Delete an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation) # noqa: E501

    :param id: The ID of the VariablePresentation to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_id_get(id, username=None):  # noqa: E501
    """Get a single VariablePresentation by its id

    Gets the details of a given VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation) # noqa: E501

    :param id: The ID of the VariablePresentation to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: VariablePresentation
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_id_put(id, user, variable_presentation=None):  # noqa: E501
    """Update an existing VariablePresentation

    Updates an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation) # noqa: E501

    :param id: The ID of the VariablePresentation to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param variable_presentation: An old VariablePresentationto be updated
    :type variable_presentation: dict | bytes

    :rtype: VariablePresentation
    """

    if connexion.request.is_json:
        variable_presentation = VariablePresentation.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=variable_presentation,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_post(user, variable_presentation=None):  # noqa: E501
    """Create one VariablePresentation

    Create a new instance of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation) # noqa: E501

    :param user: Username
    :type user: str
    :param variable_presentation: Information about the VariablePresentationto be created
    :type variable_presentation: dict | bytes

    :rtype: VariablePresentation
    """

    if connexion.request.is_json:
        variable_presentation = VariablePresentation.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=variable_presentation,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)
