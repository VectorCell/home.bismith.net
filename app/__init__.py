#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
import sys


app = Flask(__name__)


def read_status_file(filename):
	try:
		with open(filename) as file:
			return ''.join(line for line in file)
	except FileNotFoundError as fnfe:
		return filename + ' not found (is monitor.sh not running?)'
	except AttributeError as ae:
		return str(ae)
	except UnicodeDecodeError as ude:
		return str(ude)


@app.route('/')
@app.route('/index')
@app.route('/home')
def index_page():
	return render_template('index.html',
	                       zpool_status=read_status_file('/tmp/zpool.statusfile'),
	                       filesystem_status=read_status_file('/tmp/filesystem.statusfile'),
	                       block_status=read_status_file('/tmp/block.statusfile'),
	                       samba_status=read_status_file('/tmp/samba.statusfile'),
	                       smart_status=read_status_file('/tmp/smart.statusfile'))


@app.route('/<path:path>')
def static_proxy(path):
	if '.' not in path:
		path += '.html'
	return app.send_static_file(path)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8851)
