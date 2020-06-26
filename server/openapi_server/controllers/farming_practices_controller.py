import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FARMINGPRACTICES_TYPE_NAME, FARMINGPRACTICES_TYPE_URI

from openapi_server.models.farming_practices import FarmingPractices  # noqa: E501
from openapi_server import util

def farmingpracticess_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FarmingPractices

    Gets a list of all instances of FarmingPractices (more information in https://w3id.org/okn/o/sdm#FarmingPractices) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FarmingPractices]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_id_delete(id, user):  # noqa: E501
    """Delete an existing FarmingPractices

    Delete an existing FarmingPractices (more information in https://w3id.org/okn/o/sdm#FarmingPractices) # noqa: E501

    :param id: The ID of the FarmingPractices to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_id_get(id, username=None):  # noqa: E501
    """Get a single FarmingPractices by its id

    Gets the details of a given FarmingPractices (more information in https://w3id.org/okn/o/sdm#FarmingPractices) # noqa: E501

    :param id: The ID of the FarmingPractices to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: FarmingPractices
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_id_put(id, user, farming_practices=None):  # noqa: E501
    """Update an existing FarmingPractices

    Updates an existing FarmingPractices (more information in https://w3id.org/okn/o/sdm#FarmingPractices) # noqa: E501

    :param id: The ID of the FarmingPractices to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param farming_practices: An old FarmingPracticesto be updated
    :type farming_practices: dict | bytes

    :rtype: FarmingPractices
    """

    if connexion.request.is_json:
        farming_practices = FarmingPractices.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=farming_practices,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)

def farmingpracticess_post(user, farming_practices=None):  # noqa: E501
    """Create one FarmingPractices

    Create a new instance of FarmingPractices (more information in https://w3id.org/okn/o/sdm#FarmingPractices) # noqa: E501

    :param user: Username
    :type user: str
    :param farming_practices: Information about the FarmingPracticesto be created
    :type farming_practices: dict | bytes

    :rtype: FarmingPractices
    """

    if connexion.request.is_json:
        farming_practices = FarmingPractices.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=farming_practices,
        rdf_type_uri=FARMINGPRACTICES_TYPE_URI,
        rdf_type_name=FARMINGPRACTICES_TYPE_NAME, 
        kls=FarmingPractices)
