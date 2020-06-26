import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HYBRIDMODEL_TYPE_NAME, HYBRIDMODEL_TYPE_URI

from openapi_server.models.hybrid_model import HybridModel  # noqa: E501
from openapi_server import util

def hybridmodels_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HybridModel

    Gets a list of all instances of HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HybridModel]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_id_delete(id, user):  # noqa: E501
    """Delete an existing HybridModel

    Delete an existing HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel) # noqa: E501

    :param id: The ID of the HybridModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_id_get(id, username=None):  # noqa: E501
    """Get a single HybridModel by its id

    Gets the details of a given HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel) # noqa: E501

    :param id: The ID of the HybridModel to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: HybridModel
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_id_put(id, user, hybrid_model=None):  # noqa: E501
    """Update an existing HybridModel

    Updates an existing HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel) # noqa: E501

    :param id: The ID of the HybridModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param hybrid_model: An old HybridModelto be updated
    :type hybrid_model: dict | bytes

    :rtype: HybridModel
    """

    if connexion.request.is_json:
        hybrid_model = HybridModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=hybrid_model,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_post(user, hybrid_model=None):  # noqa: E501
    """Create one HybridModel

    Create a new instance of HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel) # noqa: E501

    :param user: Username
    :type user: str
    :param hybrid_model: Information about the HybridModelto be created
    :type hybrid_model: dict | bytes

    :rtype: HybridModel
    """

    if connexion.request.is_json:
        hybrid_model = HybridModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=hybrid_model,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)
