import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EMPIRICALMODEL_TYPE_NAME, EMPIRICALMODEL_TYPE_URI

from openapi_server.models.empirical_model import EmpiricalModel  # noqa: E501
from openapi_server import util

def empiricalmodels_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of EmpiricalModel

    Gets a list of all instances of EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[EmpiricalModel]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_id_delete(id, user):  # noqa: E501
    """Delete an existing EmpiricalModel

    Delete an existing EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel) # noqa: E501

    :param id: The ID of the EmpiricalModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_id_get(id, username=None):  # noqa: E501
    """Get a single EmpiricalModel by its id

    Gets the details of a given EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel) # noqa: E501

    :param id: The ID of the EmpiricalModel to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: EmpiricalModel
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_id_put(id, user, empirical_model=None):  # noqa: E501
    """Update an existing EmpiricalModel

    Updates an existing EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel) # noqa: E501

    :param id: The ID of the EmpiricalModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param empirical_model: An old EmpiricalModelto be updated
    :type empirical_model: dict | bytes

    :rtype: EmpiricalModel
    """

    if connexion.request.is_json:
        empirical_model = EmpiricalModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=empirical_model,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_post(user, empirical_model=None):  # noqa: E501
    """Create one EmpiricalModel

    Create a new instance of EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel) # noqa: E501

    :param user: Username
    :type user: str
    :param empirical_model: Information about the EmpiricalModelto be created
    :type empirical_model: dict | bytes

    :rtype: EmpiricalModel
    """

    if connexion.request.is_json:
        empirical_model = EmpiricalModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=empirical_model,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)
