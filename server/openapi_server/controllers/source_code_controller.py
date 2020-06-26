import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOURCECODE_TYPE_NAME, SOURCECODE_TYPE_URI

from openapi_server.models.source_code import SourceCode  # noqa: E501
from openapi_server import util

def sourcecodes_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SourceCode

    Gets a list of all instances of SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SourceCode]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_id_delete(id, user):  # noqa: E501
    """Delete an existing SourceCode

    Delete an existing SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode) # noqa: E501

    :param id: The ID of the SourceCode to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_id_get(id, username=None):  # noqa: E501
    """Get a single SourceCode by its id

    Gets the details of a given SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode) # noqa: E501

    :param id: The ID of the SourceCode to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: SourceCode
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_id_put(id, user, source_code=None):  # noqa: E501
    """Update an existing SourceCode

    Updates an existing SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode) # noqa: E501

    :param id: The ID of the SourceCode to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param source_code: An old SourceCodeto be updated
    :type source_code: dict | bytes

    :rtype: SourceCode
    """

    if connexion.request.is_json:
        source_code = SourceCode.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=source_code,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)

def sourcecodes_post(user, source_code=None):  # noqa: E501
    """Create one SourceCode

    Create a new instance of SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode) # noqa: E501

    :param user: Username
    :type user: str
    :param source_code: Information about the SourceCodeto be created
    :type source_code: dict | bytes

    :rtype: SourceCode
    """

    if connexion.request.is_json:
        source_code = SourceCode.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=source_code,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode)
