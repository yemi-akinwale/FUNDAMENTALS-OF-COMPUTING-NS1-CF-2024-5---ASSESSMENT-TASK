import json
import re

class Planet:
    def __init__(self, name, mass, distance_from_sun, moons):
        self.name = name
        self.mass = mass  # in kg
        self.distance_from_sun = distance_from_sun  # in million km
        self.moons = moons  # list of moon names

    def __str__(self):
        return (f"Planet: {self.name}\n"
                f"Mass: {self.mass:,.2e} kg\n"
                f"Distance from Sun: {self.distance_from_sun} million km\n"
                f"Moons: {', '.join(self.moons) if self.moons else 'None'}")

class SolarSystem:
    def __init__(self):
        self.planets = {}

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for planet_data in data.get('planets', []):
                    planet_obj = Planet(
                        name=planet_data['name'],
                        mass=planet_data['mass'],
                        distance_from_sun=planet_data['distance_from_sun'],
                        moons=planet_data['moons']
                    )
                    self.planets[planet_obj.name.lower()] = planet_obj
            print("Data successfully loaded.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            self.planets = {}

    def query_planet(self, name):
        planet = self.planets.get(name.lower().strip())
        return str(planet) if planet else "Planet not found."

    def is_planet(self, name):
        return name.lower().strip() in self.planets

    def moons_count(self, name):
        planet = self.planets.get(name.lower().strip())
        return len(planet.moons) if planet else "Planet not found."

    def mass_of_planet(self, name):
        planet = self.planets.get(name.lower().strip())
        return f"{planet.name} has a mass of {planet.mass:,.2e} kg." if planet else "Planet not found."

    def handle_query(self, query):
        query = query.lower().strip()

        planet_match = re.search(r'about (\w+)', query)
        mass_match = re.search(r'how massive is (\w+)', query)
        moons_match = re.search(r'how many moons does (\w+) have', query)
        is_planet_match = re.search(r'is (\w+) in the list of planets', query)

        if planet_match:
            return self.query_planet(planet_match.group(1))
        elif mass_match:
            return self.mass_of_planet(mass_match.group(1))
        elif moons_match:
            return f"{moons_match.group(1).capitalize()} has {self.moons_count(moons_match.group(1))} moons."
        elif is_planet_match:
            return f"{is_planet_match.group(1).capitalize()} is {'a planet' if self.is_planet(is_planet_match.group(1)) else 'not a planet'}."
        else:
            return "Sorry, I didn't understand your query."


def main():
    solar_system = SolarSystem()
    solar_system.load_data('planets_data.json')

    while True:
        print("\nAsk a question about the solar system or type 'exit' to quit:")
        query = input("Your query: ")
        if query.lower() == 'exit':
            print("Exiting the program.")
            break
        print(solar_system.handle_query(query))

if __name__ == "__main__":
    main()
