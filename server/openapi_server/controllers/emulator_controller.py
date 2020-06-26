import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EMULATOR_TYPE_NAME, EMULATOR_TYPE_URI

from openapi_server.models.emulator import Emulator  # noqa: E501
from openapi_server import util

def emulators_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Emulator

    Gets a list of all instances of Emulator (more information in https://w3id.org/okn/o/sdm#Emulator) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Emulator]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_id_delete(id, user):  # noqa: E501
    """Delete an existing Emulator

    Delete an existing Emulator (more information in https://w3id.org/okn/o/sdm#Emulator) # noqa: E501

    :param id: The ID of the Emulator to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_id_get(id, username=None):  # noqa: E501
    """Get a single Emulator by its id

    Gets the details of a given Emulator (more information in https://w3id.org/okn/o/sdm#Emulator) # noqa: E501

    :param id: The ID of the Emulator to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Emulator
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_id_put(id, user, emulator=None):  # noqa: E501
    """Update an existing Emulator

    Updates an existing Emulator (more information in https://w3id.org/okn/o/sdm#Emulator) # noqa: E501

    :param id: The ID of the Emulator to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param emulator: An old Emulatorto be updated
    :type emulator: dict | bytes

    :rtype: Emulator
    """

    if connexion.request.is_json:
        emulator = Emulator.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=emulator,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)

def emulators_post(user, emulator=None):  # noqa: E501
    """Create one Emulator

    Create a new instance of Emulator (more information in https://w3id.org/okn/o/sdm#Emulator) # noqa: E501

    :param user: Username
    :type user: str
    :param emulator: Information about the Emulatorto be created
    :type emulator: dict | bytes

    :rtype: Emulator
    """

    if connexion.request.is_json:
        emulator = Emulator.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=emulator,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator)
