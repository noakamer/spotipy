from extract import convert_data_to_objects
from extract import songs_to_list
from application import app
#this convert the data into list of artists
#convert_data_to_objects.convert_data_to_object(songs_to_list.all_songs_data(songs_to_list.all_songs_path()))
app.debug = True
app.run(host="0.0.0.0", port="5000")