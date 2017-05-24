from exception import UnknownResource


class Resource(object):
    """Represents a resource

    Attributes:
        credits_per_unit (float): Amount of credits per galaxy unit
    """
    credits_per_unit = 0

    def __init__(self, credits_per_unit=0):
        self.credits_per_unit = credits_per_unit

    @staticmethod
    def factory(type):
        """Factory method to create a given type of Resource

        Args:
            type (str): Resource type name.

        Returns:
            An instance of a Resource Type.

        Raises:
            UnknownResource if no type found.
        """
        if type == "Silver":
            return Silver()
        if type == "Gold":
            return Gold()
        if type == "Iron":
            return Iron()
        raise UnknownResource(type)


class Silver(Resource):
    pass


class Gold(Resource):
    pass


class Iron(Resource):
    pass
