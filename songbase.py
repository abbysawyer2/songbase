from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>hello world</h1>'
    return render_template('index.html')

@app.route('/mysong')
def get_mysong():
    return render_template('my-songs.html')

@app.route('/user/<string:name>/')
def get_user(name):
    #return 'hello %s your age is %d' % (name, 3)
    return render_template('user.html', user_name=name)

@app.route('/songs')
def get_all_songs():
    songs= [
    'song1',
    'song2',
    'song3'
    ]
    return render_template('songs.html', songs=songs)


@app.route('/users')
def show_all_users():
    return '<h2>this is the page for all users</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
