-- script that lists all cities contained in the database hbtn_0d_usa.
SELECTcities.id, cities.name, states.name FROM cities
JOIN states
ON cities.state_id = state_id;
