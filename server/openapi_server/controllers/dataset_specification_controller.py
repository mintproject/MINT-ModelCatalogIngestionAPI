import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DATASETSPECIFICATION_TYPE_NAME, DATASETSPECIFICATION_TYPE_URI

from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: E501
from openapi_server import util

def datasetspecifications_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of DatasetSpecification

    Gets a list of all instances of DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[DatasetSpecification]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_id_delete(id, user):  # noqa: E501
    """Delete an existing DatasetSpecification

    Delete an existing DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification) # noqa: E501

    :param id: The ID of the DatasetSpecification to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_id_get(id, username=None):  # noqa: E501
    """Get a single DatasetSpecification by its id

    Gets the details of a given DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification) # noqa: E501

    :param id: The ID of the DatasetSpecification to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: DatasetSpecification
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_id_put(id, user, dataset_specification=None):  # noqa: E501
    """Update an existing DatasetSpecification

    Updates an existing DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification) # noqa: E501

    :param id: The ID of the DatasetSpecification to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param dataset_specification: An old DatasetSpecificationto be updated
    :type dataset_specification: dict | bytes

    :rtype: DatasetSpecification
    """

    if connexion.request.is_json:
        dataset_specification = DatasetSpecification.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=dataset_specification,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_post(user, dataset_specification=None):  # noqa: E501
    """Create one DatasetSpecification

    Create a new instance of DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification) # noqa: E501

    :param user: Username
    :type user: str
    :param dataset_specification: Information about the DatasetSpecificationto be created
    :type dataset_specification: dict | bytes

    :rtype: DatasetSpecification
    """

    if connexion.request.is_json:
        dataset_specification = DatasetSpecification.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=dataset_specification,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)
