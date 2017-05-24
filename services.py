from resources import Resource
from units import GalaxyUnit


class ResourceManager(object):
    """Resource Manager class

    Attributes:
        galaxy_unit (GalaxyUnit): Instance of GalaxyUnit to control units
                                  between resources.
        resources (dict): Dictionary to hold instantiated resources
    """
    def __init__(self):
        super(ResourceManager, self).__init__()
        self.galaxy_unit = GalaxyUnit()
        self.resources = dict()

    def get_or_create_resource(self, type):
        """Retrieves or creates a new instance of a Resource by its type name

        Args:
            type (str): Resource type name.

        Returns:
            An instance of a Resource Type.
        """
        if type not in self.resources:
            self.resources[type] = Resource.factory(type)

        return self.resources[type]

    def get_resource_worth_in_credits(self, galaxy_units, type):
        """Calculates an amount of credits for a given resource type and galaxy_units

        Args:
            galaxy_units (str): Units in Galaxy format (synonyms).
            type (str): Resource type name.

        Returns:
            Result of calculation.
        """
        units = self.galaxy_unit.to_int(galaxy_units)
        return int(self.resources[type].credits_per_unit * units)

    def set_resource_credits(self, credits, galaxy_units, type):
        """Calculates and defines a resource amount of credits per unit based
        on a given credit number and units.

        Args:
            credits (str): Number of credits.
            galaxy_units (str): Units in Galaxy format (synonyms).
            type (str): Resource type name.
        """
        units = self.galaxy_unit.to_int(galaxy_units)
        resource = self.get_or_create_resource(type)
        resource.credits_per_unit = float(credits) / units
        self.resources[type] = resource
