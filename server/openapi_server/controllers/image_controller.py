import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import IMAGE_TYPE_NAME, IMAGE_TYPE_URI

from openapi_server.models.image import Image  # noqa: E501
from openapi_server import util

def images_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Image

    Gets a list of all instances of Image (more information in https://w3id.org/okn/o/sd#Image) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Image]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_id_delete(id, user):  # noqa: E501
    """Delete an existing Image

    Delete an existing Image (more information in https://w3id.org/okn/o/sd#Image) # noqa: E501

    :param id: The ID of the Image to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_id_get(id, username=None):  # noqa: E501
    """Get a single Image by its id

    Gets the details of a given Image (more information in https://w3id.org/okn/o/sd#Image) # noqa: E501

    :param id: The ID of the Image to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Image
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_id_put(id, user, image=None):  # noqa: E501
    """Update an existing Image

    Updates an existing Image (more information in https://w3id.org/okn/o/sd#Image) # noqa: E501

    :param id: The ID of the Image to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param image: An old Imageto be updated
    :type image: dict | bytes

    :rtype: Image
    """

    if connexion.request.is_json:
        image = Image.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=image,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_post(user, image=None):  # noqa: E501
    """Create one Image

    Create a new instance of Image (more information in https://w3id.org/okn/o/sd#Image) # noqa: E501

    :param user: Username
    :type user: str
    :param image: Information about the Imageto be created
    :type image: dict | bytes

    :rtype: Image
    """

    if connexion.request.is_json:
        image = Image.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=image,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)
