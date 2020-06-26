import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import THEORYGUIDEDMODEL_TYPE_NAME, THEORYGUIDEDMODEL_TYPE_URI

from openapi_server.models.theory_guided_model import TheoryGuidedModel  # noqa: E501
from openapi_server import util

def theory_guidedmodels_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Theory-GuidedModel

    Gets a list of all instances of Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TheoryGuidedModel]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_id_delete(id, user):  # noqa: E501
    """Delete an existing Theory-GuidedModel

    Delete an existing Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel) # noqa: E501

    :param id: The ID of the Theory-GuidedModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_id_get(id, username=None):  # noqa: E501
    """Get a single Theory-GuidedModel by its id

    Gets the details of a given Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel) # noqa: E501

    :param id: The ID of the Theory-GuidedModel to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: TheoryGuidedModel
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_id_put(id, user, theory_guided_model=None):  # noqa: E501
    """Update an existing Theory-GuidedModel

    Updates an existing Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel) # noqa: E501

    :param id: The ID of the Theory-GuidedModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param theory_guided_model: An old Theory-GuidedModelto be updated
    :type theory_guided_model: dict | bytes

    :rtype: TheoryGuidedModel
    """

    if connexion.request.is_json:
        theory_guided_model = TheoryGuidedModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=theory_guided_model,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_post(user, theory_guided_model=None):  # noqa: E501
    """Create one Theory-GuidedModel

    Create a new instance of Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel) # noqa: E501

    :param user: Username
    :type user: str
    :param theory_guided_model: Information about the Theory-GuidedModelto be created
    :type theory_guided_model: dict | bytes

    :rtype: TheoryGuidedModel
    """

    if connexion.request.is_json:
        theory_guided_model = TheoryGuidedModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=theory_guided_model,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)
