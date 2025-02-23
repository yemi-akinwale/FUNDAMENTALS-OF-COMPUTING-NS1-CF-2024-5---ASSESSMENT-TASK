import unittest
import json
from Solar_System import Planet, SolarSystem

# Assuming the classes Planet and SolarSystem are defined in a module named solar_system
# from solar_system import Planet, SolarSystem

class TestPlanetAndSolarSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load test data for the SolarSystem
        cls.solar_system = SolarSystem()
        cls.solar_system.load_data('planets_data.json')

    def test_planet_creation(self):
        # Test creation of a Planet object
        earth = Planet("Earth", 5.97237e24, 149.6, ["Moon"])
        self.assertEqual(earth.name, "Earth")
        self.assertEqual(earth.mass, 5.97237e24)
        self.assertEqual(earth.distance_from_sun, 149.6)
        self.assertEqual(earth.moons, ["Moon"])

    def test_data_loading(self):
        # Test if planets are loaded correctly
        self.assertIn("earth", self.solar_system.planets)
        self.assertIn("mars", self.solar_system.planets)
        self.assertEqual(len(self.solar_system.planets), 9)  # Check for 9 planets

    def test_query_functionality(self):
        # Test querying planet information
        saturn_info = self.solar_system.query_planet("Saturn")
        expected_info = ("Planet: Saturn\n"
                         "Mass: 5.6834e+26 kg\n"
                         "Distance from Sun: 1427 million km\n"
                         "Moons: Titan, Rhea, Iapetus")
        self.assertEqual(saturn_info, expected_info)

    def test_planet_existence_check(self):
        # Test for existing and non-existing planets
        self.assertTrue(self.solar_system.is_planet("Neptune"))
        self.assertFalse(self.solar_system.is_planet("Xena"))  # Xena is not a planet

    def test_moons_count(self):
        # Test counting moons of known planets
        self.assertEqual(self.solar_system.moons_count("Earth"), 1)
        self.assertEqual(self.solar_system.moons_count("Jupiter"), 4)
        self.assertEqual(self.solar_system.moons_count("Pluto"), 1)

    def test_invalid_planet_name(self):
        # Test querying a non-existing planet
        result = self.solar_system.query_planet("InvalidPlanet")
        self.assertEqual(result, "Planet not found.")

    def test_invalid_moons_count(self):
        # Test counting moons for a non-existing planet
        result = self.solar_system.moons_count("InvalidPlanet")
        self.assertEqual(result, "Planet not found.")

if __name__ == "__main__":
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
  