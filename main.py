from extract import convert_data_to_objects
from extract import songs_to_list
# from search import get_all_artists, get_albums_songs, get_artist_album, get_top_10_artist_songs
from application import app
from user import User

# this convert the data into list of artists
convert_data_to_objects.convert_data_to_object(songs_to_list.all_songs_data(songs_to_list.all_songs_path()))
# get_all_artists()
# get_artist_album('2l6M7GaS9x3rZOX6nDX3CM')
# get_top_10_artist_songs('2l6M7GaS9x3rZOX6nDX3CM')
# get_albums_songs('78bpIziExqiI9qztvNFlQu')
# app.debug = True
# app.run(host="0.0.0.0", port="5000")
use = User("noa", "1", True)
use.get_all_artists()
