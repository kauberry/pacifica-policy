"""CherryPy Status Policy object class."""
from cherrypy import tools
import requests
from policy import METADATA_ENDPOINT, validate_user


# pylint: disable=too-few-public-methods
class ProposalUserSearch(object):
    """Retrieves proposal list for a given user."""

    exposed = True

    @staticmethod
    def _get_proposals_for_user(user_id=None):
        """Return a list with all the proposals involving this user."""
        md_url = '{0}/proposalinfo/by_user_id/{1}'.format(
            METADATA_ENDPOINT, user_id
        )
        response = requests.get(url=md_url)

        return response.json()

    # CherryPy requires these named methods
    # Add HEAD (basically Get without returning body
    # pylint: disable=invalid-name
    @staticmethod
    @tools.json_out()
    @validate_user()
    def GET(user_id=None):
        """CherryPy GET method."""
        return ProposalUserSearch._get_proposals_for_user(user_id)
# pylint: enable=too-few-public-methods