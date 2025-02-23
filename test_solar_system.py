import unittest
from Solar_System import SolarSystem, Planet

class TestSolarSystem(unittest.TestCase):

    def setUp(self):
        """Sets up a mock solar system for testing."""
        self.solar_system = SolarSystem()
        self.solar_system.planets = {
            "saturn": Planet("Saturn", 5.683e26, 1433.5, ["Titan", "Enceladus"]),
            "neptune": Planet("Neptune", 1.024e26, 4495.1, ["Triton"]),
            "earth": Planet("Earth", 5.972e24, 149.6, ["Moon"]),
            "pluto": Planet("Pluto", 1.309e22, 5906.4, [])  # Including Pluto for testing
        }

    def test_query_planet(self):
        """Tests retrieval of planet details."""
        expected_output = ("Planet: Saturn\n"
                           "Mass: 5.683e+26 kg\n"
                           "Distance from Sun: 1433.5 million km\n"
                           "Moons: Titan, Enceladus")
        self.assertEqual(self.solar_system.query_planet("Saturn"), expected_output)

    def test_planet_mass(self):
        """Tests mass retrieval for a planet."""
        saturn_info = self.solar_system.query_planet("Saturn")
        self.assertIn("Mass: 5.683e+26 kg", saturn_info)

    def test_is_planet(self):
        """Tests whether a name is a planet."""
        self.assertTrue(self.solar_system.is_planet("Neptune"))
        self.assertFalse(self.solar_system.is_planet("Ceres"))  # Should return False

    def test_moons_count(self):
        """Tests moon count retrieval."""
        self.assertEqual(self.solar_system.moons_count("Earth"), 1)
        self.assertEqual(self.solar_system.moons_count("Pluto"), 0)
        self.assertEqual(self.solar_system.moons_count("Neptune"), 1)

    def test_non_existent_planet(self):
        """Tests queries for a non-existent planet."""
        self.assertEqual(self.solar_system.query_planet("Vulcan"), "Planet not found.")
        self.assertEqual(self.solar_system.moons_count("Vulcan"), "Planet not found.")
        self.assertFalse(self.solar_system.is_planet("Vulcan"))

if __name__ == "__main__":
    unittest.main()
