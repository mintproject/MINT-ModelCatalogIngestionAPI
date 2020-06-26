import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SAMPLEEXECUTION_TYPE_NAME, SAMPLEEXECUTION_TYPE_URI

from openapi_server.models.sample_execution import SampleExecution  # noqa: E501
from openapi_server import util

def sampleexecutions_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SampleExecution

    Gets a list of all instances of SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SampleExecution]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_id_delete(id, user):  # noqa: E501
    """Delete an existing SampleExecution

    Delete an existing SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution) # noqa: E501

    :param id: The ID of the SampleExecution to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_id_get(id, username=None):  # noqa: E501
    """Get a single SampleExecution by its id

    Gets the details of a given SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution) # noqa: E501

    :param id: The ID of the SampleExecution to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SampleExecution
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_id_put(id, user, sample_execution=None):  # noqa: E501
    """Update an existing SampleExecution

    Updates an existing SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution) # noqa: E501

    :param id: The ID of the SampleExecution to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param sample_execution: An old SampleExecutionto be updated
    :type sample_execution: dict | bytes

    :rtype: SampleExecution
    """

    if connexion.request.is_json:
        sample_execution = SampleExecution.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=sample_execution,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)

def sampleexecutions_post(user, sample_execution=None):  # noqa: E501
    """Create one SampleExecution

    Create a new instance of SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution) # noqa: E501

    :param user: Username
    :type user: str
    :param sample_execution: Information about the SampleExecutionto be created
    :type sample_execution: dict | bytes

    :rtype: SampleExecution
    """

    if connexion.request.is_json:
        sample_execution = SampleExecution.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=sample_execution,
        rdf_type_uri=SAMPLEEXECUTION_TYPE_URI,
        rdf_type_name=SAMPLEEXECUTION_TYPE_NAME, 
        kls=SampleExecution)
