import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOFTWARE_TYPE_NAME, SOFTWARE_TYPE_URI

from openapi_server.models.software import Software  # noqa: E501
from openapi_server import util

def softwares_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Software

    Gets a list of all instances of Software (more information in https://w3id.org/okn/o/sd#Software) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Software]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_id_delete(id, user):  # noqa: E501
    """Delete an existing Software

    Delete an existing Software (more information in https://w3id.org/okn/o/sd#Software) # noqa: E501

    :param id: The ID of the Software to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_id_get(id, username=None):  # noqa: E501
    """Get a single Software by its id

    Gets the details of a given Software (more information in https://w3id.org/okn/o/sd#Software) # noqa: E501

    :param id: The ID of the Software to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Software
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_id_put(id, user, software=None):  # noqa: E501
    """Update an existing Software

    Updates an existing Software (more information in https://w3id.org/okn/o/sd#Software) # noqa: E501

    :param id: The ID of the Software to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param software: An old Softwareto be updated
    :type software: dict | bytes

    :rtype: Software
    """

    if connexion.request.is_json:
        software = Software.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=software,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_post(user, software=None):  # noqa: E501
    """Create one Software

    Create a new instance of Software (more information in https://w3id.org/okn/o/sd#Software) # noqa: E501

    :param user: Username
    :type user: str
    :param software: Information about the Softwareto be created
    :type software: dict | bytes

    :rtype: Software
    """

    if connexion.request.is_json:
        software = Software.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=software,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)
