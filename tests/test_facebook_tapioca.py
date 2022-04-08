
import unittest

from aiotapioca_facebook import Facebook


def test_resource_access():

    wrapper = Facebook(client_id='client_id', access_token='access_token')

    resource = wrapper.user_feed(id='me')

    assert resource.data == 'https://graph.facebook.com/me/feed'

