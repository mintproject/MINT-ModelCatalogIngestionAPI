import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INTERVENTION_TYPE_NAME, INTERVENTION_TYPE_URI

from openapi_server.models.intervention import Intervention  # noqa: E501
from openapi_server import util

def interventions_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Intervention

    Gets a list of all instances of Intervention (more information in https://w3id.org/okn/o/sdm#Intervention) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Intervention]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_id_delete(id, user):  # noqa: E501
    """Delete an existing Intervention

    Delete an existing Intervention (more information in https://w3id.org/okn/o/sdm#Intervention) # noqa: E501

    :param id: The ID of the Intervention to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_id_get(id, username=None):  # noqa: E501
    """Get a single Intervention by its id

    Gets the details of a given Intervention (more information in https://w3id.org/okn/o/sdm#Intervention) # noqa: E501

    :param id: The ID of the Intervention to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Intervention
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_id_put(id, user, intervention=None):  # noqa: E501
    """Update an existing Intervention

    Updates an existing Intervention (more information in https://w3id.org/okn/o/sdm#Intervention) # noqa: E501

    :param id: The ID of the Intervention to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param intervention: An old Interventionto be updated
    :type intervention: dict | bytes

    :rtype: Intervention
    """

    if connexion.request.is_json:
        intervention = Intervention.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=intervention,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)

def interventions_post(user, intervention=None):  # noqa: E501
    """Create one Intervention

    Create a new instance of Intervention (more information in https://w3id.org/okn/o/sdm#Intervention) # noqa: E501

    :param user: Username
    :type user: str
    :param intervention: Information about the Interventionto be created
    :type intervention: dict | bytes

    :rtype: Intervention
    """

    if connexion.request.is_json:
        intervention = Intervention.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=intervention,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention)
