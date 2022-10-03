#!/usr/bin/python3
from flask import Flask, abort, request, jsonify
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route('/v2/color', methods=['GET'])
def get_color():
  try:
    ret = {'color': 'green'}

    return jsonify(ret), 200
  except Exception as e:
    logging.error(e)
    abort(500)

@app.route('/health', methods=['GET'])
def get_health():
  try:
    ret = {'status': 'ok'}

    return jsonify(ret), 200
  except Exception as e:
    logging.error(e)
    abort(500)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)