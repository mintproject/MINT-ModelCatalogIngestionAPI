import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VISUALIZATION_TYPE_NAME, VISUALIZATION_TYPE_URI

from openapi_server.models.visualization import Visualization  # noqa: E501
from openapi_server import util

def visualizations_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Visualization

    Gets a list of all instances of Visualization (more information in https://w3id.org/okn/o/sd#Visualization) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Visualization]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_id_delete(id, user):  # noqa: E501
    """Delete an existing Visualization

    Delete an existing Visualization (more information in https://w3id.org/okn/o/sd#Visualization) # noqa: E501

    :param id: The ID of the Visualization to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_id_get(id, username=None):  # noqa: E501
    """Get a single Visualization by its id

    Gets the details of a given Visualization (more information in https://w3id.org/okn/o/sd#Visualization) # noqa: E501

    :param id: The ID of the Visualization to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Visualization
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_id_put(id, user, visualization=None):  # noqa: E501
    """Update an existing Visualization

    Updates an existing Visualization (more information in https://w3id.org/okn/o/sd#Visualization) # noqa: E501

    :param id: The ID of the Visualization to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param visualization: An old Visualizationto be updated
    :type visualization: dict | bytes

    :rtype: Visualization
    """

    if connexion.request.is_json:
        visualization = Visualization.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=visualization,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)

def visualizations_post(user, visualization=None):  # noqa: E501
    """Create one Visualization

    Create a new instance of Visualization (more information in https://w3id.org/okn/o/sd#Visualization) # noqa: E501

    :param user: Username
    :type user: str
    :param visualization: Information about the Visualizationto be created
    :type visualization: dict | bytes

    :rtype: Visualization
    """

    if connexion.request.is_json:
        visualization = Visualization.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=visualization,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization)
