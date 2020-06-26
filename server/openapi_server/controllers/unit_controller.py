import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import UNIT_TYPE_NAME, UNIT_TYPE_URI

from openapi_server.models.unit import Unit  # noqa: E501
from openapi_server import util

def units_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Unit

    Gets a list of all instances of Unit (more information in https://w3id.org/okn/o/sd#Unit) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Unit]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_id_delete(id, user):  # noqa: E501
    """Delete an existing Unit

    Delete an existing Unit (more information in https://w3id.org/okn/o/sd#Unit) # noqa: E501

    :param id: The ID of the Unit to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_id_get(id, username=None):  # noqa: E501
    """Get a single Unit by its id

    Gets the details of a given Unit (more information in https://w3id.org/okn/o/sd#Unit) # noqa: E501

    :param id: The ID of the Unit to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Unit
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_id_put(id, user, unit=None):  # noqa: E501
    """Update an existing Unit

    Updates an existing Unit (more information in https://w3id.org/okn/o/sd#Unit) # noqa: E501

    :param id: The ID of the Unit to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param unit: An old Unitto be updated
    :type unit: dict | bytes

    :rtype: Unit
    """

    if connexion.request.is_json:
        unit = Unit.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=unit,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)

def units_post(user, unit=None):  # noqa: E501
    """Create one Unit

    Create a new instance of Unit (more information in https://w3id.org/okn/o/sd#Unit) # noqa: E501

    :param user: Username
    :type user: str
    :param unit: Information about the Unitto be created
    :type unit: dict | bytes

    :rtype: Unit
    """

    if connexion.request.is_json:
        unit = Unit.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=unit,
        rdf_type_uri=UNIT_TYPE_URI,
        rdf_type_name=UNIT_TYPE_NAME, 
        kls=Unit)
