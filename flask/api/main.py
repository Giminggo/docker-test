from flask import Flask


app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE')

@app.route('/')
def hello():
  return 'Hello World!!!!!!!!!!!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)