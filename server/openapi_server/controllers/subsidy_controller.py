import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SUBSIDY_TYPE_NAME, SUBSIDY_TYPE_URI

from openapi_server.models.subsidy import Subsidy  # noqa: E501
from openapi_server import util

def subsidys_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Subsidy

    Gets a list of all instances of Subsidy (more information in https://w3id.org/okn/o/sdm#Subsidy) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Subsidy]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_id_delete(id, user):  # noqa: E501
    """Delete an existing Subsidy

    Delete an existing Subsidy (more information in https://w3id.org/okn/o/sdm#Subsidy) # noqa: E501

    :param id: The ID of the Subsidy to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_id_get(id, username=None):  # noqa: E501
    """Get a single Subsidy by its id

    Gets the details of a given Subsidy (more information in https://w3id.org/okn/o/sdm#Subsidy) # noqa: E501

    :param id: The ID of the Subsidy to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Subsidy
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_id_put(id, user, subsidy=None):  # noqa: E501
    """Update an existing Subsidy

    Updates an existing Subsidy (more information in https://w3id.org/okn/o/sdm#Subsidy) # noqa: E501

    :param id: The ID of the Subsidy to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param subsidy: An old Subsidyto be updated
    :type subsidy: dict | bytes

    :rtype: Subsidy
    """

    if connexion.request.is_json:
        subsidy = Subsidy.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=subsidy,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)

def subsidys_post(user, subsidy=None):  # noqa: E501
    """Create one Subsidy

    Create a new instance of Subsidy (more information in https://w3id.org/okn/o/sdm#Subsidy) # noqa: E501

    :param user: Username
    :type user: str
    :param subsidy: Information about the Subsidyto be created
    :type subsidy: dict | bytes

    :rtype: Subsidy
    """

    if connexion.request.is_json:
        subsidy = Subsidy.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=subsidy,
        rdf_type_uri=SUBSIDY_TYPE_URI,
        rdf_type_name=SUBSIDY_TYPE_NAME, 
        kls=Subsidy)
