from flask import Flask
from threading import Thread
import random
import os
app = Flask('')


@app.route('/')
def home():
    return 'Server started'


def run():
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def server(status=None,name=None):
	if status == "f" or status == None:
		t = Thread(target=run)
		t.start()
	if status == "es":
		os.system(f"mkdir {name}")
		os.system(f"mkdir {name}/templates")
		os.system(f"touch {name}/templates/index.html")
		os.system(f"echo please check templates for the index.html file > {name}/templates/index.html")
		os.system(f"mkdir {name}/static")
		os.system(f"mkdir {name}/static/css")
		os.system(f"mkdir {name}/static/js")
		os.system(f"mkdir {name}/static/assets")
		os.system(f"touch {name}/startesserver.py")
		os.system(f"echo import er1s as es\nes.server() > {name}/startesserver.py")
		os.system(f"cd {name} && python startesserver.py")

def help():
	print("**Commands:**\nhelp - this command\n server - creates a flask server")