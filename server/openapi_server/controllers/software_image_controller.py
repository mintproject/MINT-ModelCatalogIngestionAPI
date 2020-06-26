import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOFTWAREIMAGE_TYPE_NAME, SOFTWAREIMAGE_TYPE_URI

from openapi_server.models.software_image import SoftwareImage  # noqa: E501
from openapi_server import util

def softwareimages_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoftwareImage

    Gets a list of all instances of SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoftwareImage]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_id_delete(id, user):  # noqa: E501
    """Delete an existing SoftwareImage

    Delete an existing SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage) # noqa: E501

    :param id: The ID of the SoftwareImage to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_id_get(id, username=None):  # noqa: E501
    """Get a single SoftwareImage by its id

    Gets the details of a given SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage) # noqa: E501

    :param id: The ID of the SoftwareImage to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SoftwareImage
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_id_put(id, user, software_image=None):  # noqa: E501
    """Update an existing SoftwareImage

    Updates an existing SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage) # noqa: E501

    :param id: The ID of the SoftwareImage to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param software_image: An old SoftwareImageto be updated
    :type software_image: dict | bytes

    :rtype: SoftwareImage
    """

    if connexion.request.is_json:
        software_image = SoftwareImage.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=software_image,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_post(user, software_image=None):  # noqa: E501
    """Create one SoftwareImage

    Create a new instance of SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage) # noqa: E501

    :param user: Username
    :type user: str
    :param software_image: Information about the SoftwareImageto be created
    :type software_image: dict | bytes

    :rtype: SoftwareImage
    """

    if connexion.request.is_json:
        software_image = SoftwareImage.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=software_image,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)
