import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SAMPLECOLLECTION_TYPE_NAME, SAMPLECOLLECTION_TYPE_URI

from openapi_server.models.sample_collection import SampleCollection  # noqa: E501
from openapi_server import util

def samplecollections_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SampleCollection

    Gets a list of all instances of SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SampleCollection]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_id_delete(id, user):  # noqa: E501
    """Delete an existing SampleCollection

    Delete an existing SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection) # noqa: E501

    :param id: The ID of the SampleCollection to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_id_get(id, username=None):  # noqa: E501
    """Get a single SampleCollection by its id

    Gets the details of a given SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection) # noqa: E501

    :param id: The ID of the SampleCollection to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SampleCollection
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_id_put(id, user, sample_collection=None):  # noqa: E501
    """Update an existing SampleCollection

    Updates an existing SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection) # noqa: E501

    :param id: The ID of the SampleCollection to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param sample_collection: An old SampleCollectionto be updated
    :type sample_collection: dict | bytes

    :rtype: SampleCollection
    """

    if connexion.request.is_json:
        sample_collection = SampleCollection.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=sample_collection,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)

def samplecollections_post(user, sample_collection=None):  # noqa: E501
    """Create one SampleCollection

    Create a new instance of SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection) # noqa: E501

    :param user: Username
    :type user: str
    :param sample_collection: Information about the SampleCollectionto be created
    :type sample_collection: dict | bytes

    :rtype: SampleCollection
    """

    if connexion.request.is_json:
        sample_collection = SampleCollection.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=sample_collection,
        rdf_type_uri=SAMPLECOLLECTION_TYPE_URI,
        rdf_type_name=SAMPLECOLLECTION_TYPE_NAME, 
        kls=SampleCollection)
