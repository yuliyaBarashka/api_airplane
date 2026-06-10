CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS airplanes (
    id SERIAL PRIMARY KEY,
    callsign TEXT,
    country_id INTEGER REFERENCES countries(id),
    origin_country TEXT,
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    velocity DOUBLE PRECISION,
    heading DOUBLE PRECISION,
    altitude DOUBLE PRECISION
);