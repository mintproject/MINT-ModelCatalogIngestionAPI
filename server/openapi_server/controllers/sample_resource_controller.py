import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SAMPLERESOURCE_TYPE_NAME, SAMPLERESOURCE_TYPE_URI

from openapi_server.models.sample_resource import SampleResource  # noqa: E501
from openapi_server import util

def sampleresources_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SampleResource

    Gets a list of all instances of SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SampleResource]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_id_delete(id, user):  # noqa: E501
    """Delete an existing SampleResource

    Delete an existing SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource) # noqa: E501

    :param id: The ID of the SampleResource to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_id_get(id, username=None):  # noqa: E501
    """Get a single SampleResource by its id

    Gets the details of a given SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource) # noqa: E501

    :param id: The ID of the SampleResource to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SampleResource
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_id_put(id, user, sample_resource=None):  # noqa: E501
    """Update an existing SampleResource

    Updates an existing SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource) # noqa: E501

    :param id: The ID of the SampleResource to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param sample_resource: An old SampleResourceto be updated
    :type sample_resource: dict | bytes

    :rtype: SampleResource
    """

    if connexion.request.is_json:
        sample_resource = SampleResource.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=sample_resource,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)

def sampleresources_post(user, sample_resource=None):  # noqa: E501
    """Create one SampleResource

    Create a new instance of SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource) # noqa: E501

    :param user: Username
    :type user: str
    :param sample_resource: Information about the SampleResourceto be created
    :type sample_resource: dict | bytes

    :rtype: SampleResource
    """

    if connexion.request.is_json:
        sample_resource = SampleResource.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=sample_resource,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME, 
        kls=SampleResource)
