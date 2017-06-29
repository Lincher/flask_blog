"""
This script runs the FlaskWebProject1 application using a development server.
"""

import ptvsd
import socket

from os import environ
from FlaskWebProject1 import app


if __name__ == '__main__':
    # try:
    #     address = ('127.0.0.1', 12345)
    #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     s.bind(address)
    # except socket.error:
    #     ptvsd.enable_attach(None, address=('0.0.0.0', 3000))
        # ptvsd.wait_for_attach()
    ptvsd.settrace(None, address=('0.0.0.0', 3000))

    HOST = environ.get('SERVER_HOST', 'localhost')
    # import pdb; pdb.set_trace()
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    # app.run(HOST, PORT, debug=True)
    app.run(HOST, PORT)
    
