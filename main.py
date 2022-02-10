import const
from extract_and_transform import load_to_the_relevant_objects
from extract_and_transform import extract
# from search import get_all_artists, get_albums_songs, get_artist_album, get_top_10_artist_songs
from application import app
from user import User
from log import debug_log, info_log, warning_log, error_log

# this convert the data into list of artists
load_to_the_relevant_objects.convert_data_to_object(extract.all_songs_data(extract.all_songs_path(const.SONGS_PATH)))
# get_all_artists()
# get_artist_album('2l6M7GaS9x3rZOX6nDX3CM')
# get_top_10_artist_songs('2l6M7GaS9x3rZOX6nDX3CM')
# get_albums_songs('78bpIziExqiI9qztvNFlQu')
# app.debug = True
# app.run(host="0.0.0.0", port="5000")
# use = User("noa", "1", True)
# use.get_all_artists()
# debug_log(class_name=__name__, message="hi")
