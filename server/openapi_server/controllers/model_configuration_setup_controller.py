import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import MODELCONFIGURATIONSETUP_TYPE_NAME, MODELCONFIGURATIONSETUP_TYPE_URI

from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server import util

def custom_modelconfigurationsetups_id_get(id, username=None, custom_query_name=None):  # noqa: E501
    """Get a ModelConfigurationSetup

    Gets the details of a single instance of a ModelConfigurationSetup # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str

    :rtype: ModelConfigurationSetup
    """


    return get_resource(id=id,
        username=username,
        custom_query_name=custom_query_name,
        rdf_type_uri=MODELCONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=MODELCONFIGURATIONSETUP_TYPE_NAME, 
        kls=ModelConfigurationSetup)

def custom_modelconfigurationsetups_variable_get(label, custom_query_name=None, username=None):  # noqa: E501
    """Get a list  Model

    Get model configurations by variable name # noqa: E501

    :param label: variable to search
    :type label: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str
    :param username: Username to query
    :type username: str

    :rtype: List[ModelConfigurationSetup]
    """


    return get_resource(
        custom_query_name=custom_query_name,
        username=username,
        label=label,
        rdf_type_uri=MODELCONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=MODELCONFIGURATIONSETUP_TYPE_NAME, 
        kls=ModelConfigurationSetup)

def modelconfigurationsetups_get(username=None, label=None):  # noqa: E501
    """List all ModelConfigurationSetup entities

    Gets a list of all ModelConfigurationSetup entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[ModelConfigurationSetup]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=MODELCONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=MODELCONFIGURATIONSETUP_TYPE_NAME, 
        kls=ModelConfigurationSetup)

def modelconfigurationsetups_id_delete(id, user):  # noqa: E501
    """Delete a ModelConfigurationSetup

    Delete an existing ModelConfigurationSetup # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=MODELCONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=MODELCONFIGURATIONSETUP_TYPE_NAME, 
        kls=ModelConfigurationSetup)

def modelconfigurationsetups_id_get(id, username=None):  # noqa: E501
    """Get a ModelConfigurationSetup

    Gets the details of a single instance of a ModelConfigurationSetup # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: ModelConfigurationSetup
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=MODELCONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=MODELCONFIGURATIONSETUP_TYPE_NAME, 
        kls=ModelConfigurationSetup)

def modelconfigurationsetups_id_put(id, user, model_configuration_setup=None):  # noqa: E501
    """Update a ModelConfigurationSetup

    Updates an existing ModelConfigurationSetup # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param model_configuration_setup: An old ModelConfigurationSetupto be updated
    :type model_configuration_setup: dict | bytes

    :rtype: ModelConfigurationSetup
    """

    if connexion.request.is_json:
        model_configuration_setup = ModelConfigurationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=model_configuration_setup,
        rdf_type_uri=MODELCONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=MODELCONFIGURATIONSETUP_TYPE_NAME, 
        kls=ModelConfigurationSetup)

def modelconfigurationsetups_post(user, model_configuration_setup=None):  # noqa: E501
    """Create a ModelConfigurationSetup

    Create a new instance of a ModelConfigurationSetup # noqa: E501

    :param user: Username
    :type user: str
    :param model_configuration_setup: A new ModelConfigurationSetupto be created
    :type model_configuration_setup: dict | bytes

    :rtype: ModelConfigurationSetup
    """

    if connexion.request.is_json:
        model_configuration_setup = ModelConfigurationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=model_configuration_setup,
        rdf_type_uri=MODELCONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=MODELCONFIGURATIONSETUP_TYPE_NAME, 
        kls=ModelConfigurationSetup)
