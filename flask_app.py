import utils
import random
import simple_models
# from scripts import print_songs

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	song = simple_models.simple_song('bruno mars')
	return '''<!DOCTYPE html>
<html>
<body>

{}

</body>
</html>'''.format(song.get_html())

@app.route("/hi/<int:post_id>")
def hi(post_id):
	# print(datasetmetrics.get_average_tokens('songs/artists/Adele.json'))
	return '''<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>
<h2> you found my secret page! </h2>
{}

</body>
</html>'''.format(post_id + 2)

if __name__ == "__main__":
	app.run('0.0.0.0')
