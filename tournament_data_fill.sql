
--######################################################################
--#
--#  Written by: Marvin Fuller
--#  Date: Oct 12, 2015
--#  Filename: tournament_data_fill.sql
--#  Purpose:
--#          Test data that can be used to test database functionality
--#             of the tournament project.
--#
--######################################################################

-- Connect to database:
--\c tournament
\c mftour

SET ROLE web; 

-- Insert some practice fictitious data, just for purpose of testing
--     the database application.

-- insert data
BEGIN;
INSERT INTO players (pl_name) VALUES ('Tim Burr');
INSERT INTO players (pl_name) VALUES ('Willie Leak');
INSERT INTO players (pl_name) VALUES ('Owen Cash');
INSERT INTO players (pl_name) VALUES ('Walter Melon');
INSERT INTO players (pl_name) VALUES ('Luke Warm');
INSERT INTO players (pl_name) VALUES ('Mike Easter');
INSERT INTO players (pl_name) VALUES ('Andrew Fuller');
INSERT INTO players (pl_name) VALUES ('Heidi Clare');
COMMIT;


-- insert some dummy matches
BEGIN;
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (1,2,1,False);
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (3,4,3,False);
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (5,6,5,False);
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (7,8,7,False);
COMMIT;

-- insert some dummy 2nd round matches
BEGIN;
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (1,3,1,False);
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (5,7,5,False);
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (2,4,2,False);
INSERT INTO matches (player_a, player_b, winner, draw) VALUES (6,8,6,False);
COMMIT;
