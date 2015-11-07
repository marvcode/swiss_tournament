# marvs_movies

Just a personal project that uses python code and the Bootstrap 3 framework to create a simple Favorite Movies Website.

Running this python application will generate an HTML file that represents the website.
Written by: Marvin Fuller
Date: Sept 7, 2015


#Quick Start (How to run the application):
To run the python application and generate the .HTML output file:
  1. Download the following files to your computer and store them all in the same directory on your computer.
        (fresh_tomatoes.py, media.py, mf_movies2.py)
  2. On a Mac, open a terminal window and change the working directory to the directory where the files above are stored.
  3. To confirm this, you can type 'pwd' at the command line and the path shown should match where you have the files stored.
  4. Then, at the command line, type: 'python mf_movies2.py'
  5. This will run the application and open a browser window to display the newly created HTML page called Marvin's Favorite Movies.

To see the final web page deployed in production:
  1. Go to this link www.marvsprojectsite.net, then click on the the link labeled "Marv's Favorite Movies Site".


#Documentation
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

