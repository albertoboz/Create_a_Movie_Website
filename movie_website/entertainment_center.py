import media
import fresh_tomatoes

#defining the details of each movie

the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "Director: Francis Ford Coppola",
                            "Stars: Marlon Brando, Al Pacino, James Caan",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://youtu.be/5DO-nDW43Ik")



the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                              "Director: Christopher Nolan",
                              "Stars: Christian Bale, Heath Ledger, Aaron Eckhart",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://youtu.be/5PSNL1qE6VY")



lotr = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                   "A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.",
                   "Director: Peter Jackson",
                   "Stars: Elijah Wood, Ian McKellen, Orlando Bloom",
                   "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
                   "https://youtu.be/aStYWD25fAQ")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a alter-ego devil-may-care soap maker, forming an underground fight club that evolves into something much, much more...",
                         "Director: David Fincher",
                         "Stars: Brad Pitt, Edward Norton, Meat Loaf",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_prestige = media.Movie("The Prestige",
                           "Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.",
                           "Director: Christopher Nolan",
                           "Stars: Christian Bale, Hugh Jackman, Scarlett Johansson",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                           "https://www.youtube.com/watch?v=o4gHCmTQDVI")

#create a list that contains all the movies as input for function open_movies_page() to create html file

movies = [the_godfather, the_dark_knight, lotr, fight_club, the_prestige]

#function to build the HTML file

fresh_tomatoes.open_movies_page(movies)
