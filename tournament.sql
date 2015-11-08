--######################################################################
--#
--#  Written by: Marvin Fuller
--#  Date: Oct 12, 2015
--#  Filename: tournament.sql
--#  Purpose:
--#          Table & Views definitions for the tournament project.
--#
--######################################################################


SET ROLE web;

-- create table : players
DROP TABLE IF EXISTS players CASCADE;
CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  pl_name TEXT,
  wins INTEGER DEFAULT 0,
  matches INTEGER DEFAULT 0,
  draws INTEGER Default 0
);
ALTER TABLE players OWNER TO web;


-- create table : matches
DROP TABLE IF EXISTS matches CASCADE;
CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  player_a INTEGER,
  player_b INTEGER,
  winner INTEGER DEFAULT NULL,
  draw BOOLEAN DEFAULT FALSE
);
ALTER TABLE matches OWNER TO web;


-- create views for listing tables and databases
-- create view
DROP VIEW IF EXISTS view_standings;
CREATE VIEW view_standings AS
    SELECT * FROM players ORDER BY wins DESC;
ALTER VIEW view_standings OWNER TO web;


-- create view
DROP VIEW IF EXISTS view_players;
CREATE VIEW view_players AS
    SELECT id,pl_name AS Player FROM players ORDER BY id ASC;
ALTER VIEW view_standings OWNER TO web;
