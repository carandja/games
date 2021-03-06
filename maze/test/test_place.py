"""Tests for the Place class"""
import unittest
from maze.place import Place

class TestPlace(unittest.TestCase):
    """Methods to test the Place class"""

    def test_init_place(self):
        """test place initialisation"""
        place = Place('House')
        self.assertEqual('House', place.get_name())

    def test_init_place_noargs(self):
        """test that place will throw an exception if no argument passed to constructor"""
        self.assertRaises(TypeError, Place)

    def test_add_direction(self):
        """test adding a direction"""
        place = Place('House')
        hall = Place('Hall')
        place.add_direction("In", hall)
        self.assertEqual(place.get_directions(), {"In": hall})

    def test_get_directions_list(self):
        """add directions and test the result"""
        place = Place('House')
        place.add_direction("up", Place("1"))
        place.add_direction("down", Place("2"))
        place.add_direction("left", Place("3"))
        place.add_direction("right", Place("4"))
        self.assertEqual(place.get_directions_list(), ["up", "down", "left", "right"])

    def test_get_place_for_direction(self):
        """test getting a place based on a direction"""
        place = Place('House')
        hall = Place('Hall')
        place.add_direction("Up", hall)
        room = Place("Room")
        place.add_direction("Down", room)
        self.assertEqual(place.get_place_for_direction("Up"), hall)
        self.assertEqual(place.get_place_for_direction("Down"), room)

    def test_get_prior_place(self):
        """test getting the prior place"""
        place = Place('House')
        hall = Place('Hall')
        place.add_direction("Up", hall)
        room = Place("Room")
        hall.add_direction("Down", room)
        self.assertEqual(room.get_prior_place(), hall)
        self.assertEqual(hall.get_prior_place(), place)

    def test_set_prior_place(self):
        """test setting the prior place"""
        place = Place('House')
        hall = Place('Hall')
        place.add_direction("Up", hall)
        self.assertEqual(hall.get_prior_place(), place)

    def test_get_origin(self):
        """test getting the origin place"""
        place = Place('House')
        hall = Place('Hall')
        place.add_direction("Up", hall)
        room = Place("Room")
        hall.add_direction("Down", room)
        self.assertEqual(room.get_origin(), place)

    def test_get_map(self):
        """test that the map displays properly"""
        place = Place("House")
        place.add_direction("Up", Place("Hall"))
        place.add_direction("Down", Place("Cellar"))
        place.add_direction("Forward", Place("Study"))
        place.get_place_for_direction("Up").add_direction("Left", Place("Library"))
        place.get_place_for_direction("Up").get_place_for_direction("Left") \
            .add_direction("Right", Place("Kitchen"))
        place.get_place_for_direction("Down").add_direction("Curving right", Place("Dungeon"))
        expected = """+--->[House]
     Up
     +--->[Hall]
          Left
          +--->[Library]
               Right
               +--->[Kitchen]
     Down
     +--->[Cellar]
          Curving right
          +--->[Dungeon]
     Forward
     +--->[Study]
"""
        actual = place.get_map()
        with open("actual.txt", 'w') as output:
            output.write(actual)
        with open("expected.txt", 'w') as output:
            output.write(expected)
        self.assertEqual(actual, expected)

    def test_dump(self):
        """test dumping the object"""
        name = "House"
        place = Place(name)
        hall = Place("Hall")
        direction_string = "Up"
        place.add_direction(direction_string, hall)
        expected = """
////////
////{}
////{}
////////""".format(name, place.get_directions())
        self.assertEqual(expected, place.get_dump())
