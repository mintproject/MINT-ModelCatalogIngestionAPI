import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CAUSALDIAGRAM_TYPE_NAME, CAUSALDIAGRAM_TYPE_URI

from openapi_server.models.causal_diagram import CausalDiagram  # noqa: E501
from openapi_server import util

def causaldiagrams_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CausalDiagram

    Gets a list of all instances of CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CausalDiagram]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_id_delete(id, user):  # noqa: E501
    """Delete an existing CausalDiagram

    Delete an existing CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram) # noqa: E501

    :param id: The ID of the CausalDiagram to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_id_get(id, username=None):  # noqa: E501
    """Get a single CausalDiagram by its id

    Gets the details of a given CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram) # noqa: E501

    :param id: The ID of the CausalDiagram to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: CausalDiagram
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_id_put(id, user, causal_diagram=None):  # noqa: E501
    """Update an existing CausalDiagram

    Updates an existing CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram) # noqa: E501

    :param id: The ID of the CausalDiagram to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param causal_diagram: An old CausalDiagramto be updated
    :type causal_diagram: dict | bytes

    :rtype: CausalDiagram
    """

    if connexion.request.is_json:
        causal_diagram = CausalDiagram.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=causal_diagram,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)

def causaldiagrams_post(user, causal_diagram=None):  # noqa: E501
    """Create one CausalDiagram

    Create a new instance of CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram) # noqa: E501

    :param user: Username
    :type user: str
    :param causal_diagram: Information about the CausalDiagramto be created
    :type causal_diagram: dict | bytes

    :rtype: CausalDiagram
    """

    if connexion.request.is_json:
        causal_diagram = CausalDiagram.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=causal_diagram,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram)
