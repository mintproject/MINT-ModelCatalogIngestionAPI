import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PERSON_TYPE_NAME, PERSON_TYPE_URI

from openapi_server.models.person import Person  # noqa: E501
from openapi_server import util

def persons_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Person

    Gets a list of all instances of Person (more information in https://w3id.org/okn/o/sd#Person) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Person]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_id_delete(id, user):  # noqa: E501
    """Delete an existing Person

    Delete an existing Person (more information in https://w3id.org/okn/o/sd#Person) # noqa: E501

    :param id: The ID of the Person to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_id_get(id, username=None):  # noqa: E501
    """Get a single Person by its id

    Gets the details of a given Person (more information in https://w3id.org/okn/o/sd#Person) # noqa: E501

    :param id: The ID of the Person to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Person
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_id_put(id, user, person=None):  # noqa: E501
    """Update an existing Person

    Updates an existing Person (more information in https://w3id.org/okn/o/sd#Person) # noqa: E501

    :param id: The ID of the Person to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param person: An old Personto be updated
    :type person: dict | bytes

    :rtype: Person
    """

    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=person,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_post(user, person=None):  # noqa: E501
    """Create one Person

    Create a new instance of Person (more information in https://w3id.org/okn/o/sd#Person) # noqa: E501

    :param user: Username
    :type user: str
    :param person: Information about the Personto be created
    :type person: dict | bytes

    :rtype: Person
    """

    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=person,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)
