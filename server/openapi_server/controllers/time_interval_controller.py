import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TIMEINTERVAL_TYPE_NAME, TIMEINTERVAL_TYPE_URI

from openapi_server.models.time_interval import TimeInterval  # noqa: E501
from openapi_server import util

def timeintervals_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TimeInterval

    Gets a list of all instances of TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TimeInterval]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_id_delete(id, user):  # noqa: E501
    """Delete an existing TimeInterval

    Delete an existing TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval) # noqa: E501

    :param id: The ID of the TimeInterval to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_id_get(id, username=None):  # noqa: E501
    """Get a single TimeInterval by its id

    Gets the details of a given TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval) # noqa: E501

    :param id: The ID of the TimeInterval to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: TimeInterval
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_id_put(id, user, time_interval=None):  # noqa: E501
    """Update an existing TimeInterval

    Updates an existing TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval) # noqa: E501

    :param id: The ID of the TimeInterval to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param time_interval: An old TimeIntervalto be updated
    :type time_interval: dict | bytes

    :rtype: TimeInterval
    """

    if connexion.request.is_json:
        time_interval = TimeInterval.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=time_interval,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)

def timeintervals_post(user, time_interval=None):  # noqa: E501
    """Create one TimeInterval

    Create a new instance of TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval) # noqa: E501

    :param user: Username
    :type user: str
    :param time_interval: Information about the TimeIntervalto be created
    :type time_interval: dict | bytes

    :rtype: TimeInterval
    """

    if connexion.request.is_json:
        time_interval = TimeInterval.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=time_interval,
        rdf_type_uri=TIMEINTERVAL_TYPE_URI,
        rdf_type_name=TIMEINTERVAL_TYPE_NAME, 
        kls=TimeInterval)
