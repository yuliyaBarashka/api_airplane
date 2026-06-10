from db.connection import get_connection
from services.nominatim_api import get_country_coordinates
from services.opensky_api import get_airplanes

COUNTRIES = [
    "Germany",
    "France",
    "Italy",
    "Spain"
]

def init_countries():
    conn = get_connection()
    cur = conn.cursor()

    for country in COUNTRIES:
        lat, lon = get_country_coordinates(country)

        cur.execute("""
            INSERT INTO countries (name, latitude, longitude)
            VALUES (%s, %s, %s)
            ON CONFLICT (name) DO NOTHING
        """, (country, lat, lon))

    conn.commit()
    conn.close()

def load_airplanes():
    conn = get_connection()
    cur = conn.cursor()

    states = get_airplanes()

    for s in states:
        if not s:
            continue

        callsign = s[1]
        origin_country = s[2]
        longitude = s[5]
        latitude = s[6]
        velocity = s[9]
        heading = s[10]
        altitude = s[7]

        cur.execute("""
            SELECT id FROM countries WHERE name = %s
        """, (origin_country,))

        country = cur.fetchone()

        if country:
            country_id = country[0]

            cur.execute("""
                INSERT INTO airplanes (
                    callsign, country_id, origin_country,
                    longitude, latitude, velocity, heading, altitude
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                callsign, country_id, origin_country,
                longitude, latitude, velocity, heading, altitude
            ))

    conn.commit()
    conn.close()

