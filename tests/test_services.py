import unittest

from services import ResourceManager


class ResourceManagerTestCase(unittest.TestCase):

    def setUp(self):
        super(ResourceManagerTestCase, self).setUp()
        self.manager = ResourceManager()
        self.manager.galaxy_unit.set_synonym('glob', 'I')
        self.manager.galaxy_unit.set_synonym('prok', 'V')

    def test_get_or_create_resource(self):
        resource = self.manager.get_or_create_resource('Silver')
        self.assertEqual(resource.credits_per_unit, 0)
        self.manager.resources['Silver'].credits_per_unit = 12
        resource = self.manager.get_or_create_resource('Silver')
        self.assertEqual(resource.credits_per_unit, 12)

    def test_set_resource_credits(self):
        self.manager.set_resource_credits(12, 'prok glob', 'Iron')
        resource = self.manager.get_or_create_resource('Iron')
        self.assertEqual(resource.credits_per_unit, 2)

    def test_get_resource_worth_in_credits(self):
        self.manager.set_resource_credits(34900, 'prok', 'Gold')
        credits = self.manager.get_resource_worth_in_credits('glob', 'Gold')
        self.assertEqual(credits, 6980)
