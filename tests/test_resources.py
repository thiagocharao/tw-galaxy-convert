import unittest

from resources import Resource, Silver, UnknownResource


class ResourceTestCase(unittest.TestCase):

    def test_factory(self):
        resource = Resource.factory('Silver')
        self.assertIsInstance(resource, Silver)
        with self.assertRaises(UnknownResource):
            Resource.factory('Adamantium')
