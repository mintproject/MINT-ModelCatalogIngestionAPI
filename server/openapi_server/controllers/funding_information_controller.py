import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FUNDINGINFORMATION_TYPE_NAME, FUNDINGINFORMATION_TYPE_URI

from openapi_server.models.funding_information import FundingInformation  # noqa: E501
from openapi_server import util

def fundinginformations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FundingInformation

    Gets a list of all instances of FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FundingInformation]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_id_delete(id, user):  # noqa: E501
    """Delete an existing FundingInformation

    Delete an existing FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation) # noqa: E501

    :param id: The ID of the FundingInformation to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_id_get(id, username=None):  # noqa: E501
    """Get a single FundingInformation by its id

    Gets the details of a given FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation) # noqa: E501

    :param id: The ID of the FundingInformation to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: FundingInformation
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_id_put(id, user, funding_information=None):  # noqa: E501
    """Update an existing FundingInformation

    Updates an existing FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation) # noqa: E501

    :param id: The ID of the FundingInformation to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param funding_information: An old FundingInformationto be updated
    :type funding_information: dict | bytes

    :rtype: FundingInformation
    """

    if connexion.request.is_json:
        funding_information = FundingInformation.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=funding_information,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_post(user, funding_information=None):  # noqa: E501
    """Create one FundingInformation

    Create a new instance of FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation) # noqa: E501

    :param user: Username
    :type user: str
    :param funding_information: Information about the FundingInformationto be created
    :type funding_information: dict | bytes

    :rtype: FundingInformation
    """

    if connexion.request.is_json:
        funding_information = FundingInformation.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=funding_information,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)
