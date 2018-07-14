"""Define classes to support locations on the map

The help goes here.
This is helpful.
"""

class Place():
    """A place on the game map

    The Place represents a spot on the map.
    It has a name and directions, where    directions are routes
    away from one place to another place.  Each place also has
    a link to its origin.
    """

    def __init__(self, name):
        """Creates instance variables for directions and name"""
        self._directions = {}
        self._name = name
        self._prior = None

    def get_directions(self):
        """return the internal representation of directions"""
        return self._directions

    def get_name(self):
        """return the name"""
        return self._name

    def add_direction(self, direction, place):
        """Add a place in a specified direction

        direction - the name of the direction
        place - the Place found it that direction
        """

        self._directions[direction] = place
        place.set_prior_place(self)

    def get_directions_list(self):
        """Get a list of available directions and the places there."""
        return list(self._directions.keys())

    def get_place_for_direction(self, direction):
        """Get the place in given direction"""
        return self._directions[direction]

    def set_prior_place(self, prior):
        """set the prior place"""
        self._prior = prior

    def get_prior_place(self):
        """gwt the prior place"""
        return self._prior

    def get_origin(self):
        """get the originating place"""
        if self._prior is None:
            return self
        return self._prior.get_origin()

    def get_dump(self):
        """return a string representsation of this Place"""
        return """
////////
////{}
////{}
////////""".format(self._name, self._directions)

    def get_map(self):
        """return a heirarchical string representation of the map"""

        def get_map_level(place, level):
            """return the map for this level"""
            spacing = "     "
            indent = spacing * level
            newdata = indent + "+--->[" + place.get_name() + ']\n'
            for direction in place.get_directions_list():
                newdata = newdata + spacing + indent + direction + '\n'
                nextplace = place.get_directions()[direction]
                newdata += get_map_level(nextplace, level + 1)
            return newdata

        origin = self.get_origin()
        return get_map_level(origin, 0)
