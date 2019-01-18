#from azureml.deploy import DeployClient

from flask import Flask
from flask import render_template
from flask import request

import sys
import tempDriver
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/testpage')
def test():
  return 'Hello from test route!'

#@app.route('/<string:page_name>/')
#def render_static(page_name):
#    return render_template('%s.html' % page_name)

@app.route('/helloworld')
@app.route('/helloworld/')
def render_static(pageName=None):

    loopCount = request.args.get('loopCount', default=10, type=int)
    tempDriver.Drive(loopCount)

    #decode client principal to pass to template and display in browser
    encodedClientPrincipal = request.headers['X-Ms-Client-Principal']
    decodedClientPrincipal = base64.b64decode(encodedClientPrincipal)

    #write to app service log via standard out
    #sys.stdout.write("user: " + str(request.headers['X-Ms-Client-Principal-Name']) + '\n')
    #sys.stdout.write("decoded client principal: " + str(decodedClientPrincipal) + '\n')

    return render_template('helloworld.html', name=pageName, headers=request.headers, clientPrincipal = decodedClientPrincipal)


if __name__ == '__main__':
      app.run()