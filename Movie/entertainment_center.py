import fresh_tomatoes
import media

#movie instance Lion King
lion_king=media.Movie("Lion King",
                      "The story of Simba, a young lion who is to succeed his father, Mufasa, as king",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg/220px-The_Lion_King_poster.jpg",
                      "https://www.youtube.com/watch?v=jOIu472cCq0")

#movie instance Inception
inception=media.Movie("Inception",
                   "A professional thief who commits corporate espionage by infiltrating the subconscious of his targets.", 
                   "http://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg",
                   "https://www.youtube.com/watch?v=66TuSJo4dZM")

#movie instance Bridesmaids
bridesmaids=media.Movie("Bridesmaids",
                   "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.", 
                   "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/BridesmaidsPoster.jpg/220px-BridesmaidsPoster.jpg",
                   "https://www.youtube.com/watch?v=FNppLrmdyug")


#movie instance American Hustle
american_hustle=media.Movie("American Hustle",
                   "A con man, Irving Rosenfeld, along with his seductive partner Sydney Prosser, is forced to work for a wild FBI agent, Richie DiMaso, who pushes them into a world of Jersey powerbrokers and mafia.", 
                   "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/American_Hustle_2013_poster.jpg/220px-American_Hustle_2013_poster.jpg",
                   "https://www.youtube.com/watch?v=ST7a1aK_lG0")

#movie instance Food Inc
food_inc=media.Movie("Food Inc",
                   "The film examines corporate farming in the United States, concluding that agribusiness produces food that is unhealthy, in a way that is environmentally harmful and abusive of both animals and employees", 
                   "https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Food_inc.jpg/220px-Food_inc.jpg",
                   "https://www.youtube.com/watch?v=5eKYyD14d_0")

#movie instance The Silence of the Lambs
the_silence_of_the_lambs=media.Movie("The Silence of the Lambs",
                   "A young F.B.I. cadet must confide in an incarcerated and manipulative killer to receive his help on catching another serial killer who skins his victims.", 
                   "https://upload.wikimedia.org/wikipedia/en/thumb/8/86/The_Silence_of_the_Lambs_poster.jpg/220px-The_Silence_of_the_Lambs_poster.jpg",
                   "https://www.youtube.com/watch?v=V5dA92wqmME")

movies = [lion_king, inception, bridesmaids, american_hustle, food_inc, the_silence_of_the_lambs]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__module__)
