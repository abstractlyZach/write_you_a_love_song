# flask_app.py

import random
from models import random_models
from utils import get_data
# from scripts import print_songs

from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome_page():
	to_return = \
'''
<html>
<link rel= "stylesheet" type= "text/css" href= "static/style.css">
<body>
	<script language='javascript' type='text/javascript'>	
		
	</script>
	<h1 align="center">♫I'm Just Gonna Write You a Love Song♫</h1>
	<h2 align="center">
		Sarah Bareilles won't write you a love song, but I will. With artificial intelligence!
	</h2>
	<h3 align="center">
		A project by Zach
	</h3>
	<p align="center">
		Choose an artist and I'll try to write you two short songs in their style. Vote for the one that you like more; the more you vote the better the songs will get!
	</p>
	<div id="artist-pages">
		<ul>
			<li><a href="/vote/Adele">Adele</a></li>
			<li><a href="/vote/Bruno-Mars">Bruno Mars</a></li>
			<li><a href="/vote/Chance-The-Rapper">Chance The Rapper</a></li>
			<li><a href="/vote/Coldplay">Coldplay</a></li>
			<li><a href="/vote/Disney">Disney</a></li>
			<li><a href="/vote/Drake">Drake</a></li>
			<li><a href="/vote/Ed-Sheeran">Ed Sheeran</a></li>
			<li><a href="/vote/Eminem">Eminem</a></li>
			<li><a href="/vote/Imagine-Dragons">Imagine Dragons</a></li>
			<li><a href="/vote/Justin-Bieber">Justin Bieber</a></li>
			<li><a href="/vote/Katy-Perry">Katy Perry</a></li>
			<li><a href="/vote/Lady-GaGa">Lady GaGa</a></li>
			<li><a href="/vote/Major-Lazer">Major Lazer</a></li>
			<li><a href="/vote/Maroon-5">Maroon 5</a></li>
			<li><a href="/vote/Michael-Jackson">Michael Jackson</a></li>
			<li><a href="/vote/Prince">Prince</a></li>
			<li><a href="/vote/Rihanna">Rihanna</a></li>
			<li><a href="/vote/Taylor-Swift">Taylor Swift</a></li>
			<li><a href="/vote/The-Weeknd">The Weeknd</a></li>
		</ul>
	</div>

	<p>
		This project uses artifical intelligence and natural language processing techniques to build song lyrics. Click the button below to see how I do it!
	</p>
	<a class="button" href="https://github.com/exzacktlee/write_you_a_love_song">
		See the code
	</a>
</body>
</html>
'''
	return to_return


@app.route("/vote/<string:artist>")
def vote_page(artist):
	'Returns html for the voting page.'
	# i tried to use old and new python string formatting, but I need to
	#		go through and escape characters, or it won't work
	to_return = '''
<html>
<link rel= "stylesheet" type= "text/css" href= "../static/style.css">
<body>
	<script language='javascript' type='text/javascript'>	
		function getNewSongs() {
			clearSongs();
			var ajaxRequest;
				try{
					ajaxRequest = new XMLHttpRequest();
				} catch (e){
					try{
						ajaxRequest = new ActiveXObject('Msxml2.XMLHTTP');
					} catch (e) {
						try{
							ajaxRequest = new ActiveXObject('Microsoft.XMLHTTP');
						} catch (e){
							alert('Your browser broke!');
							return false;
						}
					}
				}
			ajaxRequest.onreadystatechange = function() {
				if(ajaxRequest.readyState == 4) {
					enableVoting();
					document.getElementById("algorithm1").value = ajaxRequest.responseText.split("|||")[0];
					document.getElementById("algorithm2").value = ajaxRequest.responseText.split("|||")[1];
					document.getElementById("song1").innerHTML = ajaxRequest.responseText.split("|||")[2];
					document.getElementById("song2").innerHTML = ajaxRequest.responseText.split("|||")[3];
				}
			}
			ajaxRequest.open('GET', "/get_songs/" + document.getElementById("artist").value,
							true);
			ajaxRequest.send(null);
		}

		function vote(winner) {
			var ajaxRequest;
				try{
					ajaxRequest = new XMLHttpRequest();
				} catch (e){
					try{
						ajaxRequest = new ActiveXObject('Msxml2.XMLHTTP');
					} catch (e) {
						try{
							ajaxRequest = new ActiveXObject('Microsoft.XMLHTTP');
						} catch (e){
							alert('Your browser broke!');
							return false;
						}
					}
				}
			ajaxRequest.onreadystatechange = function() {
				if(ajaxRequest.readyState == 4) {
					disableVoting();
				}
			}
			ajaxRequest.open('GET', 
							"/vote_for/"
								+ document.getElementById("algorithm1").value + "/"
								+ document.getElementById("algorithm2").value + "/"
								+ winner + "/"
								+ document.getElementById("artist").value,
							true);
			ajaxRequest.send(null);
		}

		function disableVoting() {
			var buttons = document.getElementsByClassName('vote-button');
			var i;
			for (i = 0; i < buttons.length; i++) {
				var button = buttons[i];
				button.disabled = true;
				button.innerHTML= "Thanks!";
			} 
		}

		function enableVoting() {
			var buttons = document.getElementsByClassName('vote-button');
			var i;
			for (i = 0; i < buttons.length; i++) {
				var button = buttons[i];
				button.disabled = false;
				button.innerHTML= "This One's Better";
			} 
		}

		function clearSongs() {
			document.getElementById("song1").innerHTML = "<h2>Thinking!</h2>"
			document.getElementById("song2").innerHTML = "<h2>Thinking!</h2>"
		}		

	</script>

	<div id="header">
	<h1 align="center">Welcome to </h1>
	<h1 align="center" style="color:#551A8B">THE ARENA</h1>
	<h2>Two verses. One victor. Who will win? You decide!</h2>
		<button id="load-new-verses-button" onclick="getNewSongs()">Load New Verses</button>
		<a class="button" href="/">Choose a new artist</a>
		<br><br>
	</div>
	<div id="main-container">
		<h3>Learning from ''' + artist.replace("-", " ") + '''</h3>
		<input type=hidden id="artist" value="''' + artist + '''">
		<input type=hidden id="algorithm1" value="">
		<input type=hidden id="algorithm2" value="">
		<div class="song-container">
			<button class="vote-button" type="button" onclick="vote(1)" disabled=true>This One's Better</button>
			<br><br>
			<div id="song1">
				<h2>Click the yellow button to load some verses!</h2>
			</div>
		</div>
		<div class="song-container">
			<button class="vote-button" type="button" onclick="vote(2)" disabled=true>This One's Better</button>
			<br><br>
			<div id="song2">
			</div>
		</div>
		<div id="spotify-player">
			<iframe src="https://embed.spotify.com/?uri=spotify%3Auser%3A1250251216%3Aplaylist%3A21v37QniMoKRzJ2OWGLAr4" height="380" frameborder="0" allowtransparency="true"></iframe>
		</div>
	</div>
</body>
</html>
'''
	return to_return


@app.route("/get_songs/<string:artist>")
def get_songs(artist):
	# convert back to regular artist string
	artist = ' '.join(artist.split('-'))
	model1_name, model2_name, model1, model2 = random_models.get_models(artist)
	song1 = model1.new_song(short=True)
	song2 = model2.new_song(short=True)
	return "|||".join([model1_name, model2_name, song1.get_html(), song2.get_html()])

@app.route("/vote_for/<string:algorithm1>/<string:algorithm2>/<int:winner>/<string:artist>")
def get_vote(algorithm1, algorithm2, winner, artist):
	'''Takes the users' votes and writes to a .txt file. 
	If winner is 1, algorithm1 got the vote. 2 for algorithm2.
	'''
	if winner == 1:
		winning_algorithm = algorithm1
		losing_algorithm = algorithm2
	elif winner == 2:
		winning_algorithm = algorithm2
		losing_algorithm = algorithm1
	else:
		with open('illegal_votes.txt', 'a', encoding='utf-8') as vote_file:
			vote_file.write('{},{},{},{}\n'.format(algorithm1, algorithm2, winner, artist))
		return ""
	with open('votes.txt', 'a', encoding='utf-8') as vote_file:
		vote_file.write('{},{},{}\n'.format(winning_algorithm, losing_algorithm, artist))
	return ""


if __name__ == "__main__":
	app.run('0.0.0.0')
