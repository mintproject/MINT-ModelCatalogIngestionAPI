import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MODEL_TYPE_NAME, MODEL_TYPE_URI

from openapi_server.models.model import Model  # noqa: E501
from openapi_server import util

def custom_model_index_get(label, custom_query_name=None, username=None):  # noqa: E501
    """Get a Model

    Gets the details of a single instance of a Model # noqa: E501

    :param label: Label of NumericalIndex
    :type label: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str
    :param username: Username to query
    :type username: str

    :rtype: List[Model]
    """


    return query_manager.get_resource(
        custom_query_name=custom_query_name,
        username=username,
        label=label,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def custom_model_intervention_get(label, custom_query_name=None, username=None):  # noqa: E501
    """Get a Model

    Gets the details of a single instance of a Model # noqa: E501

    :param label: Label of intervation
    :type label: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str
    :param username: Username to query
    :type username: str

    :rtype: List[Model]
    """


    return query_manager.get_resource(
        custom_query_name=custom_query_name,
        username=username,
        label=label,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def custom_model_region_get(label, custom_query_name=None, username=None):  # noqa: E501
    """Get a Model

    Gets the details of a single instance of a Model # noqa: E501

    :param label: region to search
    :type label: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str
    :param username: Username to query
    :type username: str

    :rtype: List[Model]
    """


    return query_manager.get_resource(
        custom_query_name=custom_query_name,
        username=username,
        label=label,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def custom_models_standard_variable_get(label, custom_query_name=None, username=None):  # noqa: E501
    """Get a list of models

    Gets a list of model filter by the label of a standard variable # noqa: E501

    :param label: standard variable name
    :type label: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str
    :param username: Username to query
    :type username: str

    :rtype: List[Model]
    """


    return query_manager.get_resource(
        custom_query_name=custom_query_name,
        username=username,
        label=label,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def custom_models_variable_get(label, custom_query_name=None, username=None):  # noqa: E501
    """Get a list of Model

    Get models by variable name # noqa: E501

    :param label: variable to search
    :type label: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str
    :param username: Username to query
    :type username: str

    :rtype: List[Model]
    """


    return query_manager.get_resource(
        custom_query_name=custom_query_name,
        username=username,
        label=label,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Model

    Gets a list of all instances of Model (more information in https://w3id.org/okn/o/sdm#Model) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Model]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_id_delete(id, user):  # noqa: E501
    """Delete an existing Model

    Delete an existing Model (more information in https://w3id.org/okn/o/sdm#Model) # noqa: E501

    :param id: The ID of the Model to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_id_get(id, username=None):  # noqa: E501
    """Get a single Model by its id

    Gets the details of a given Model (more information in https://w3id.org/okn/o/sdm#Model) # noqa: E501

    :param id: The ID of the Model to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Model
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_id_put(id, user, model=None):  # noqa: E501
    """Update an existing Model

    Updates an existing Model (more information in https://w3id.org/okn/o/sdm#Model) # noqa: E501

    :param id: The ID of the Model to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param model: An old Modelto be updated
    :type model: dict | bytes

    :rtype: Model
    """

    if connexion.request.is_json:
        model = Model.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=model,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_post(user, model=None):  # noqa: E501
    """Create one Model

    Create a new instance of Model (more information in https://w3id.org/okn/o/sdm#Model) # noqa: E501

    :param user: Username
    :type user: str
    :param model: Information about the Modelto be created
    :type model: dict | bytes

    :rtype: Model
    """

    if connexion.request.is_json:
        model = Model.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=model,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)
