import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import MODEL_TYPE_NAME, MODEL_TYPE_URI

from openapi_server.models.model import Model  # noqa: E501
from openapi_server import util

def models_get(username=None):  # noqa: E501
    """List all Model entities

    Gets a list of all Model entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[Model]
    """


    return get_resource(
        username=username,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_id_delete(id, user):  # noqa: E501
    """Delete a Model

    Delete an existing Model # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_id_get(id, username=None):  # noqa: E501
    """Get a Model

    Gets the details of a single instance of a Model # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Model
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_id_put(id, user, model=None):  # noqa: E501
    """Update a Model

    Updates an existing Model # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param model: An old Modelto be updated
    :type model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        model = Model.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=model,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_post(user, model=None):  # noqa: E501
    """Create a Model

    Create a new instance of a Model # noqa: E501

    :param user: Username
    :type user: str
    :param model: A new Modelto be created
    :type model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        model = Model.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=model,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)