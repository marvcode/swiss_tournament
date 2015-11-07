
# Swiss_Tournament

This is a project that implements a Swiss Rules Tournament using a PostgreSQL database.  Essentially this is just a learning project that uses python code to interact with the Postgres database.

Udacity FullStack Web Developer NanoDegree - Project #2.
Written by: Marvin Fuller
Date: October 12, 2015 - Completed November 8, 2015.


# Quick Start (How to run the application):
To run the python application and manage a swiss sytle tournament:
  Prerequisites:
    It is assumed that you have access to a computer running postgreSQL v9.4 or later.  Whether connecting to this computer            locally or remotely, you will need to connect as a superuser (such as 'postgres') and create a database called                  'tournament'.
    The tournament database must have the following roles provisioned:
        Database Owner: Group role: web
        Database User: login role: sid  (most queries will be run as login role 'sid', so python application will not work if             these roles are not provisioned correctly.
    
  1. Download the following files to your computer and store them all in the same directory on your computer.
        (tournament.py, tournament_test.py, tournament.sql)
        (tournament_data_fill.sql is Optional, for those who want to excercise additional testing on the application)
  2. On a Mac, open a terminal window and change the working directory to the directory where the files above are stored.



  3. To confirm this, you can type 'pwd' at the command line and the path shown should match where you have the files stored.
  4. Then, at the command line, type: 'python mf_movies2.py'
  5. This will run the application and open a browser window to display the newly created HTML page called Marvin's Favorite Movies.

To see the final web page deployed in production:
  1. Go to this link www.marvsprojectsite.net, then click on the the link labeled "Marv's Favorite Movies Site".


#Documentation

Function Definitions in tournament.py
  connect(): Connect to the PostgreSQL database.  Returns a database connection.

  countPlayers(): Returns the number of players currently registered in the tournament.

  deleteMatches(): Remove all the match records from the database.

  deletePlayers(): Remove all the player records from the database.

  registerPlayer(name): Adds a player to the tournament database. The database assigns a unique serial id number for the             player.mber for the player.
          Args:
            name: the player's full name (need not be unique).

  reportDraw(pl_x, pl_y): Records a 'Draw' as the outcome of a single match between two players.
          Args:
            pl_x:  the id number of one of the players
            pl_y:  the id number of another player

  reportMatch(winner, loser): Records the outcome of a single match between two players.
          Args:
            winner:  the id number of the player who won
            loser:  the id number of the player who lost
            
  playerStandings(): Returns a list of the players and their win records, sorted by wins. The first entry in the list is the       player in first place, or a player tied for first place if there is currently a tie.
          Returns:
            A list of tuples, each of which contains (id, name, wins, matches):
              id: the player's unique id (assigned by the database)
              name: the player's full name (as registered)
              wins: the number of matches the player has won
              matches: the number of matches the player has played
              
  getPlName(plyr): Performs a query on the given player ID and returns the ID and the player's name from the players table
        of the database.
          Args:
            plyr: id number of the player for which the name is needed
          Return:
            Return a list containing the player ID and their name.

  isRematch(pl_x, pl_y): Checks the matches table to determine if this player combination is a rematch of the players provided.
          Args:
            pl_x: id number of 1st player to be checked for previous pairing
            pl_y: id number of 2nd player to be checked for previous pairing
          Return:
            Return a boolean True if the pair is a rematch otherwise False.

  swissPairings(): Returns a list of pairs of players for the next round of a match. Assuming that there are an even number of     players registered, each player appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent to him or her in the standings.
          Returns:
            A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name





Running the python app 'mf_movies2.py' will create instances of the Movie() class as defined in media.py.

for the Movie() class...

The required arguments for the class are:  
       movie_title - Movie Title as you want it to appear on the website  
       year - Year of the theatrical release  
       movie_storyline - Brief synopsis of the film  
       poster_image - A URL that points to a web based image file of the movie poster  
       trailer_youtube - A URL that points to the youtube trailer for each movie  

The Bootstrap framework will create an HTML output file in the same directory that the mf_movies2.py is located.  The HTML that will be creted will be named marvs_movies.html

#Using the HTML File
When your browser loads the HTML file, several elements of the Bootstrap framework as well as poster images are pulled from various web resources.  So internet connectivity is required to properly load this page.  

Once the page is loaded, the user can click on any movie poster to view the original theatrical trailer.

Enjoy

