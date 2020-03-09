import json

import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import MODELCONFIGURATION_TYPE_NAME, MODELCONFIGURATION_TYPE_URI

from openapi_server.models.model_configuration import ModelConfiguration  # noqa: E501
from openapi_server import util

def modelconfigurations_post(user, model_configuration=None):  # noqa: E501
    """Create a ModelConfiguration

    Create a new instance of a ModelConfiguration # noqa: E501

    :param user: Username
    :type user: str
    :param model_configuration: A new ModelConfigurationto be created
    :type model_configuration: dict | bytes

    :rtype: ModelConfiguration
    """

    model_configuration = ModelConfiguration.from_dict(data)  # noqa: E501
    return post_resource(user=user,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration)


#configuration_json = "input_tests/cycles-0.9.4-alpha-without-id.json"
configuration_json = "input_tests/test_file.json"
with open(configuration_json, 'r') as file:
    data = json.load(file)
    user = "dhruvrpa@usc.edu"
    #Create a modelconfiguration
    m = modelconfigurations_post(user, data)
    print(m)
