######################################################################
#
#  Written by: Marvin Fuller
#  Date: Oct 12, 2015
#  Filename: mftour.py  then later tournament.py --
#  Purpose:
"""         The purpose of this module is an implementation of a
             Swiss-system tournament in python to interact with a PostgreSQL
             database.  This module will define all the functions needed
             to manage the tournament per the design rules of the project.
"""
#
######################################################################
# !/usr/bin/python
# -*- coding: utf-8 -*-

#   import libraries
import psycopg2.extras


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    # variables
    dbtable = 'players'
    pgdatabase = 'mftour'
    pghost = '10.0.1.38'
    pguser = 'sid'
    pguserpass = 'foo.bar'

    # establish connection to db
    return psycopg2.connect(host = pghost,
                            user = pguser,
                        password = pguserpass,
                        database = pgdatabase)


def countPlayers():
    """Returns the number of players currently registered."""
    conn = None
    cur = None
    mod_error = "Error: Unable to fetch data in function: countPlayers()"
    results = None
    # establish connection
    conn = connect()
    # establish cursor
    cur = conn.cursor()
    # First Query
    sql = "SELECT * FROM view_players;"
    try:
        # Execute query and count rows
        cur.execute(sql)
        num_rows = cur.rowcount
    except:
        raise ValueError(mod_error)

    # close database and disconnect from server
    cur.close()
    conn.close()
    return num_rows


def deleteMatches():
    """Remove all the match records from the database."""
    conn = None
    cur = None
    mod_error = "Error: unable to fetch data in function: deleteMatches()"
    results = None
    # establish connection
    conn = connect()
    # establish cursor
    cur = conn.cursor()
    # First Query
    sql = "TRUNCATE TABLE matches RESTART IDENTITY;"
    try:
        # Execute query and count rows
        cur.execute(sql)
        conn.commit()
    except:
        raise ValueError(mod_error)

    # close database and disconnect from server
    cur.close()
    conn.close()
    return


def deletePlayers():
    """Remove all the player records from the database."""
    conn = None
    cur = None
    mod_error = "Error: Unable to fetch data in function: deleteMatches()"
    results = None
    # establish connection
    conn = connect()
    # establish cursor
    cur = conn.cursor()
    # First Query
    sql = "TRUNCATE TABLE players RESTART IDENTITY;"
    try:
        # Execute query and count rows
        cur.execute(sql)
        conn.commit()
    except:
        raise ValueError(mod_error)

    # close database and disconnect from server
    cur.close()
    conn.close()
    return


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = None
    cur = None
    mod_error = "Error: Unable to fetch data in function: registerPlayer()"
    results = None
    # establish connection
    conn = connect()
    # establish cursor
    cur = conn.cursor()
    # First Query
    sql = "INSERT INTO players (pl_name) VALUES (%s);"
    data = (name, )
    try:
        # Execute query and count rows
        cur.execute(sql, data)
        conn.commit()
    except:
        raise ValueError(mod_error)

    # close database and disconnect from server
    cur.close()
    conn.close()
    return

def reportDraw(pl_x, pl_y):
    """Records a 'Draw' as the outcome of a single match between two players.

    Args:
      pl_x:  the id number of one of the players
      pl_y:  the id number of another player
    """
    # Reference Documentation
    #      http://initd.org/psycopg/docs/usage.html#query-parameters
    #
    conn = None
    cur = None
    mod_error = "Error: Unable to fetch data in function: reportDraw()"
    results = None

    # establish connection
    conn = connect()
    # establish cursor
    cur = conn.cursor()
    # First Query
    sql = "INSERT INTO matches (player_a, player_b, draw) VALUES (%s, %s, %s);"
    data = (pl_x, pl_y, True)
    try:
        # Execute query and count rows
        cur.execute(sql, data)
        conn.commit()
    except:
        raise ValueError(mod_error)

    # close database and disconnect from server
    cur.close()
    conn.close()
    return


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Reference Documentation
    #      http://initd.org/psycopg/docs/usage.html#query-parameters
    #
    conn = None
    cur = None
    mod_error = "Error: Unable to fetch data in function: reportMatch()"
    results = None

    # establish connection
    conn = connect()
    # establish cursor
    cur = conn.cursor()
    # First Query
    sql = "INSERT INTO matches (player_a, player_b, winner) VALUES (%s, %s, %s);"  # noqa
    data = (winner, loser, winner)
    try:
        # Execute query and count rows
        cur.execute(sql, data)
        conn.commit()
    except:
        raise ValueError(mod_error)

    # close database and disconnect from server
    cur.close()
    conn.close()
    return


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Variables
    num_players = None
    conn = None
    cur = None
    results = None
    mod_error = "Error: Unable to fetch data in function: playerStandings()"

    # determine number of players in tournament
    num_players = countPlayers()
    # establish connection
    conn = connect()
    # establish dictionary cursor
    cur = conn.cursor()

    # For each player in tournament:
    #       1. Count / Store the number of Wins
    #       2. Count / Store the number of matches
    #
    for i in range(1, num_players+1):
        # 1st query to count wins for each player
        sql = "SELECT count(*) FROM matches WHERE winner = (%s);"
        data = (i,)
        try:
            cur.execute(sql, data)
            (num_wins, ) = cur.fetchone()
            conn.commit()
        except:
            raise ValueError(mod_error)

        # 2nd Query to UPDATE number of wins into player table
        sql = "UPDATE players SET wins = (%s) WHERE id = (%s);"
        data = (num_wins, i, )
        try:
            # Execute query and count rows
            cur.execute(sql, data)
            conn.commit()
        except:
            raise ValueError(mod_error)

        # 3rd query to count matches for each player
        sql = "SELECT count(*) FROM matches \
               WHERE (player_a = (%s)) OR (player_B = (%s));"
        data = (i, i, )
        try:
            cur.execute(sql, data)
            (num_matches, ) = cur.fetchone()
        except:
            raise ValueError(mod_error)

        # 4th Query to update number of matches into player table
        sql = "UPDATE players SET matches = (%s) WHERE id = (%s);"
        data = (num_matches, i,)
        try:
            # Execute query and count rows
            cur.execute(sql, data)
            conn.commit()
        except:
            raise ValueError(mod_error)

        # 5th query to count draws for each player
        sql = "SELECT count(*) FROM matches \
        WHERE (draw = True) and ((player_a = (%s)) or (player_b = (%s)));"
        data = (i, i)
        try:
            cur.execute(sql, data)
            (num_draws, ) = cur.fetchone()
        except:
            raise ValueError(mod_error)

        # 6th Query to UPDATE number of draws into player table
        sql = "UPDATE players SET draws = (%s) WHERE id = (%s);"
        data = (num_draws, i, )
        try:
            # Execute query and count rows
            cur.execute(sql, data)
            conn.commit()
        except:
            raise ValueError(mod_error)

    # 7th Query return new updated player table
    sql = "SELECT * FROM  view_standings;"
    try:
        # Execute query and count rows
        cur.execute(sql)
        results = cur.fetchall()
    except:
        raise ValueError(mod_error)

    # for each player count the number of wins in matches.winner
    # for each player pull their name from players

    # close database and disconnect from server
    cur.close()
    conn.close()
    return results


def getPlName(plyr):
    """Performs a query on the given player ID and returns
        the ID and the player's name from the players table
        of the database.

       Args:
        plyr: id number of the player for which the name is needed

       Return:
          Return a list containing the player ID and their name.
    """
    # variables
    conn = None
    dict_cur = None
    mod_error = "Error: unable to fetch data in Module function: getPlName()"
    output = None
    playerName = None

    # establish connection
    conn = connect()
    # establish cursor
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # First Query
    sql = "SELECT pl_name FROM players WHERE id = (%s);"
    data = (plyr,)
    try:
        # Execute query
        dict_cur.execute(sql, data)
    except:
        raise ValueError(mod_error)

    playerName = dict_cur.fetchone()
    playerName = playerName[0]

    # close database and disconnect from server
    dict_cur.close()
    conn.close()
    return plyr, playerName


def isRematch(pl_x, pl_y):
    """Checks the matches table to determine if this player combination is
        a rematch of the players provided.

       Args:
        pl_x: id number of 1st player to be checked for previous pairing
        pl_y: id number of 2nd player to be checked for previous pairing

       Return:
          Return a boolean True if the pair is a rematch otherwise False.
    """
    # variables
    conn = None
    dict_cur = None
    mod_error = "Error: unable to fetch data in Module function: isRematch()"
    output = None
    result = 0

    # establish connection
    conn = connect()
    # establish cursor
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # First Query
    sql = "SELECT count(*) \
         FROM matches WHERE \
         (player_a = (%s) AND player_b = (%s)) OR \
         (player_a = (%s) AND player_b = (%s));"
    data = (pl_x, pl_y, pl_y, pl_x)
    try:
        # Execute query
        dict_cur.execute(sql, data)
    except:
        raise ValueError(mod_error)

    (result, ) = dict_cur.fetchone()
    if (result > 0):
        output = True
    else:
        output = False

    # close database and disconnect from server
    dict_cur.close()
    conn.close()
    return output


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # variables
    targetFound = None
    playersPaired = []
    unpairedRows = []
    pairedRows = []
    targetRow = []
    targetPlayer = []
    compareRow = []
    comparePlayer = []

    # Get the current standings and number of Players
    currentStandings = playerStandings()  # returns a list if tuples
    numPlayers = countPlayers()

    # Create a list of unPaired Players  (player ID, numWins)
    for i in range(0, numPlayers):
        curRow = currentStandings[i]
        curWins = curRow[2:3]
        curWins = curWins[0]        # converts the list value to integer
        curPlayer = curRow[0:1]
        curPlayer = curPlayer[0]    # converts the list value to integer
        unpairedRows.append((curPlayer, curWins))  # (player#,wins)

    # >>> Create a pair routine
    # establish offset  (offset = 0 means, exact number of wins)
    offset = -1                      # preps the offset to be 0 on first pass
    numUnpaired = len(unpairedRows)  # determine number of players unpaired

    while ((len(unpairedRows)) > 0):
        # start on row 0 and establish a target player and target numWins
        #     assumes player at top of list is target
        targetRow = unpairedRows[0]
        targetWins = targetRow[1:2]
        targetWins = targetWins[0]      # converts the list value to integer
        targetPlayer = targetRow[0:1]
        targetPlayer = targetPlayer[0]  # converts the list value to integer
        offset = offset + 1
        if offset > numPlayers:
            # error occurred - infinite loop prevention
            raise ValueError('Error detected with data.  Infinite loop ',
                             'detected in swissPairings().')
            break

        # target wins is now established,
        #    now search remaining list for wins match
        for z in range(1, numUnpaired):
            compareRow = unpairedRows[z]
            compareWins = compareRow[1:2]
            compareWins = compareWins[0]       # converts list value to integer
            comparePlayer = compareRow[0:1]
            comparePlayer = comparePlayer[0]   # converts list value to integer

            # test for correct number of wins and do not allow rematch
            if ((compareWins + offset) == targetWins) and \
               (isRematch(targetPlayer, comparePlayer) == False):
                # player Match Found
                playersPaired.append((getPlName(targetPlayer) + getPlName(comparePlayer)))  # noqa
                # remove this pair from the unpaired player list
                unpairedRows.remove(targetRow)
                unpairedRows.remove(compareRow)
                # reset offset
                offset = -1
                numUnpaired = len(unpairedRows)
                break

    # return a list of tuples each of which contains (id1, name1, id2, name2)
    return playersPaired

