import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CONFIGURATIONSETUP_TYPE_NAME, CONFIGURATIONSETUP_TYPE_URI

from openapi_server.models.configuration_setup import ConfigurationSetup  # noqa: E501
from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server import util

def configurationsetups_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ConfigurationSetup

    Gets a list of all instances of ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ConfigurationSetup]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_id_delete(id, user):  # noqa: E501
    """Delete an existing ConfigurationSetup

    Delete an existing ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup) # noqa: E501

    :param id: The ID of the ConfigurationSetup to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_id_get(id, username=None):  # noqa: E501
    """Get a single ConfigurationSetup by its id

    Gets the details of a given ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup) # noqa: E501

    :param id: The ID of the ConfigurationSetup to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: ConfigurationSetup
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_id_put(id, user, configuration_setup=None):  # noqa: E501
    """Update an existing ConfigurationSetup

    Updates an existing ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup) # noqa: E501

    :param id: The ID of the ConfigurationSetup to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param configuration_setup: An old ConfigurationSetupto be updated
    :type configuration_setup: dict | bytes

    :rtype: ConfigurationSetup
    """

    if connexion.request.is_json:
        configuration_setup = ConfigurationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=configuration_setup,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def configurationsetups_post(user, configuration_setup=None):  # noqa: E501
    """Create one ConfigurationSetup

    Create a new instance of ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup) # noqa: E501

    :param user: Username
    :type user: str
    :param configuration_setup: Information about the ConfigurationSetupto be created
    :type configuration_setup: dict | bytes

    :rtype: ConfigurationSetup
    """

    if connexion.request.is_json:
        configuration_setup = ConfigurationSetup.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=configuration_setup,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)

def custom_configurationsetups_id_get(id, username=None, custom_query_name=None):  # noqa: E501
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


    return query_manager.get_resource(id=id,
        username=username,
        custom_query_name=custom_query_name,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup)
