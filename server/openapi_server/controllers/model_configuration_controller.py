import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MODELCONFIGURATION_TYPE_NAME, MODELCONFIGURATION_TYPE_URI

from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server import util

def custom_modelconfigurations_id_get(id, username=None, custom_query_name=None):  # noqa: E501
    """Get a ModelConfiguration

    Gets the details of a single instance of a ModelConfiguration # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str
    :param custom_query_name: Name of the custom query
    :type custom_query_name: str

    :rtype: ModelConfiguration
    """


    return query_manager.get_resource(id=id,
        username=username,
        custom_query_name=custom_query_name,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ModelConfiguration

    Gets a list of all instances of ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ModelConfiguration]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_id_delete(id, user):  # noqa: E501
    """Delete an existing ModelConfiguration

    Delete an existing ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration) # noqa: E501

    :param id: The ID of the ModelConfiguration to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_id_get(id, username=None):  # noqa: E501
    """Get a single ModelConfiguration by its id

    Gets the details of a given ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration) # noqa: E501

    :param id: The ID of the ModelConfiguration to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: ModelConfiguration
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_id_put(id, user, model_configuration=None):  # noqa: E501
    """Update an existing ModelConfiguration

    Updates an existing ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration) # noqa: E501

    :param id: The ID of the ModelConfiguration to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param model_configuration: An old ModelConfigurationto be updated
    :type model_configuration: dict | bytes

    :rtype: ModelConfiguration
    """

    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)

def modelconfigurations_post(user, model_configuration=None):  # noqa: E501
    """Create one ModelConfiguration

    Create a new instance of ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration) # noqa: E501

    :param user: Username
    :type user: str
    :param model_configuration: Information about the ModelConfigurationto be created
    :type model_configuration: dict | bytes

    :rtype: ModelConfiguration
    """

    if connexion.request.is_json:
        model_configuration = ModelConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)
