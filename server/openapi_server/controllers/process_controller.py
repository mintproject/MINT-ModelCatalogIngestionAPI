import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROCESS_TYPE_NAME, PROCESS_TYPE_URI

from openapi_server.models.process import Process  # noqa: E501
from openapi_server import util

def processs_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Process

    Gets a list of all instances of Process (more information in https://w3id.org/okn/o/sdm#Process) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Process]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_id_delete(id, user):  # noqa: E501
    """Delete an existing Process

    Delete an existing Process (more information in https://w3id.org/okn/o/sdm#Process) # noqa: E501

    :param id: The ID of the Process to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_id_get(id, username=None):  # noqa: E501
    """Get a single Process by its id

    Gets the details of a given Process (more information in https://w3id.org/okn/o/sdm#Process) # noqa: E501

    :param id: The ID of the Process to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Process
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_id_put(id, user, process=None):  # noqa: E501
    """Update an existing Process

    Updates an existing Process (more information in https://w3id.org/okn/o/sdm#Process) # noqa: E501

    :param id: The ID of the Process to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param process: An old Processto be updated
    :type process: dict | bytes

    :rtype: Process
    """

    if connexion.request.is_json:
        process = Process.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=process,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)

def processs_post(user, process=None):  # noqa: E501
    """Create one Process

    Create a new instance of Process (more information in https://w3id.org/okn/o/sdm#Process) # noqa: E501

    :param user: Username
    :type user: str
    :param process: Information about the Processto be created
    :type process: dict | bytes

    :rtype: Process
    """

    if connexion.request.is_json:
        process = Process.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=process,
        rdf_type_uri=PROCESS_TYPE_URI,
        rdf_type_name=PROCESS_TYPE_NAME, 
        kls=Process)
