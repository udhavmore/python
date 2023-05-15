import flask


app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def main():
    return "<h1>Sample Page</h1>" \
           "<br>" \
           "<p>This is a simple Flask example</p>"


if __name__ == '__main__':
    app.run()

