import psycopg2

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="aviation",
            user="postgres",
            password="12345",
            host="localhost",
            port=5432
        )

    def get_countries_and_aeroplanes_count(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, COUNT(a.id)
                FROM countries c
                LEFT JOIN airplanes a ON c.id = a.country_id
                GROUP BY c.name
            """)
            return cur.fetchall()

    def get_all_aeroplanes(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT callsign, origin_country, velocity, altitude
                FROM airplanes
            """)
            return cur.fetchall()

    def get_avg_speed(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT AVG(velocity) FROM airplanes
            """)
            return cur.fetchone()[0]

    def get_aeroplanes_with_higher_speed(self):
        avg = self.get_avg_speed()

        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT callsign, velocity
                FROM airplanes
                WHERE velocity > %s
            """, (avg,))
            return cur.fetchall()

    def get_aeroplanes_with_keyword(self, keyword):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT callsign
                FROM airplanes
                WHERE callsign ILIKE %s
            """, (f"%{keyword}%",))
            return cur.fetchall()

    def close(self):
        self.conn.close()
