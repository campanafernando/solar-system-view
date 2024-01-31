from skyfield.api import Loader, Topos

def get_planetary_positions(latitude, longitude):
    load = Loader('~/.skyfield-data')
    planets = load('de421.bsp')
    ts = load.timescale()

    location = Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    time = ts.now()

    earth = planets['earth']
    observer = earth + location

    planet_names = {
        'Mercury': 'MERCURY BARYCENTER',
        'Venus': 'VENUS BARYCENTER',
        'Mars': 'MARS BARYCENTER',
        'Jupiter': 'JUPITER BARYCENTER',
        'Saturn': 'SATURN BARYCENTER',
        'Uranus': 'URANUS BARYCENTER',
        'Neptune': 'NEPTUNE BARYCENTER'
    }
    positions = []

    for name, planet_key in planet_names.items():
        planet = planets[planet_key]
        astrometric = observer.at(time).observe(planet)
        alt, az, d = astrometric.apparent().altaz()

        if alt.degrees > 0: 
            positions.append({
                'name': name,
                'azimuth': az.degrees,
                'altitude': alt.degrees
            })

    return positions
