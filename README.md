
# Swiss_Tournament

This is a project that implements a Swiss Rules Tournament using a PostgreSQL database.  
Essentially, this is just a learning project that uses python code to interact with the Postgres database.

Udacity FullStack Web Developer NanoDegree - Project #2.
Written by: Marvin Fuller
Date: October 12, 2015 - Completed November 8, 2015.


# Quick Start (How to run the application):
To run the python application and manage a swiss sytle tournament:

**Prerequisites:**
It is assumed that you have access to a computer running postgreSQL v9.4 or later.  
Whether connecting to this computer locally or remotely, you will need to 
connect as a superuser (such as 'postgres') and create a database called
'tournament'.
    
The tournament database must have the following roles provisioned:
   Database Owner: Group role: web
   Database User: Login role: sid  
   (**most queries will be run as login role 'sid', so python application 
        will not work if these roles are not provisioned correctly.**)
    
1. Download the following files to your computer and store them all in the same directory on your computer.
     (tournament.py, tournament_test.py, tournament.sql)

   (tournament_data_fill.sql is **Optional**, for those who want to excercise 
   additional testing on the application)

2. Create the database schema by importing the tournament.sql file.
    This can be accomplished in a number of ways:
    For example:
    A. Use command line on local machine.
```
$ psql tournament [username]
(depending on permissions, psql will ask for user's password)
> \i [fullpath to file]\tournament.sql
(this will import the SQL file and setup database tables and Views)
```
B. The user may find it easier to use a database administration tool 
   such as 'pgadmin3'.  This application is available for multiple OS
   platforms such as Windows, Linux, and Mac  OS.  In the administration 
   tool, the user can connect to the database and then open a SQL command
   window to use the SQL code found in the tournament.sql file.

3. On a Mac, open a terminal window and change the working directory 
   to the directory where the files above are stored.

4. To confirm this, you can type 'pwd' at the command line and the 
   path shown should match where you have the files stored.

5. Then, at the command line, type: 'python tournamant_test.py'
  
6. This will run the test application and output the results of the 
       system test for this application.

# Test Output

Upon executing 'tournament_test.py' you should see the following output on your screen...

```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Extra Credit: Rematch Prevention Demonstrated. 
   Players with matching scores were not paired since 
   this could have caused a rematch scenario.
Extra Credit: Support matches ending in Draws Demonstrated. 
   Players with Draws are correctly shown in standings table.

Success!  All tests pass!
```



#Documentation

###Function Definitions in tournament.py
**connect()**: Connect to the PostgreSQL database.  Returns a database connection.

**countPlayers()**: Returns the number of players currently registered in the tournament.

**deleteMatches()**: Remove all the match records from the database.

**deletePlayers()**: Remove all the player records from the database.

**registerPlayer(name)**: Adds a player to the tournament database. The database 
assigns a unique serial id number for the player.
   Args:
   name: the player's full name (need not be unique).

**reportDraw(pl_x, pl_y)**: Records a 'Draw' as the outcome of a single match between two players.
   Args:
   pl_x:  the id number of one of the players
   pl_y:  the id number of another player

**reportMatch(winner, loser)**: Records the outcome of a single match between two players.
   Args:
   winner:  the id number of the player who won
   loser:  the id number of the player who lost
            
**playerStandings()**: Returns a list of the players and their win records, sorted by wins. The first entry in the list is the player in first place, or a player tied for first place if there is currently a tie.
   Returns:
   A list of tuples, each of which contains (id, name, wins, matches):
   id: the player's unique id (assigned by the database)
   name: the player's full name (as registered)
   wins: the number of matches the player has won
   matches: the number of matches the player has played
              
**getPlName(plyr)**: Performs a query on the given player ID and returns the ID and the player's name from the players table
        of the database.
          Args:
            plyr: id number of the player for which the name is needed
          Return:
            Return a list containing the player ID and their name.

**isRematch(pl_x, pl_y)**: Checks the matches table to determine if this player combination is a rematch of the players provided.
   Args:
   pl_x: id number of 1st player to be checked for previous pairing
   pl_y: id number of 2nd player to be checked for previous pairing
   Return:
   Return a boolean True if the pair is a rematch otherwise False.

**swissPairings()**: Returns a list of pairs of players for the next round of a match. Assuming that there are an even number of     players registered, each player appears exactly once in the pairings.  Each player is paired with another
   player with an equal or nearly-equal win record, that is, a player adjacent to him or her in the standings.
   Returns:
   A list of tuples, each of which contains (id1, name1, id2, name2)
   id1: the first player's unique id
   name1: the first player's name
   id2: the second player's unique id
   name2: the second player's name


#Extra Credit features:

###Three features were implemented to qualify for extra credit for this project.

1. Program Enhancement for Extra Credit: Rematch Prevention.  While creating 
next round pairings, pairs of players were examined rematch condition.  If a 
rematch was detected , another player was chosen for the pair to prevent a 
rematch.  This function is demonstrated in the version of the tournament_test.py provided.

2. Program Enhancement for Extra Credit: Support for matches ending in a Draw.
A function called reportDraw() was created to allow the tournament administrator 
the ability to record matches that end in a 'draw'.  In this function, a Null 
value is left in the winner column and a True state is stored in the Draw 
column of the players table.  This function is demonstrated in the version 
of the tournament_test.py provided.

3. Program Enhancement for Extra Credit: Views were created in database and 
used in application to enhance queries.
