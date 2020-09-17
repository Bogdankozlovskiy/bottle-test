from bottle import Bottle


app = Bottle()


@app.get("/")
def hello():
	return "<h1><i>hello world!!!</i></h1>"


@app.get("/movies")
def movies():
	return "<h1><i>a lot movies</i></h1>"
