import requests, logging
from FSGate import dump_in_file, swallow_file, swd, append_to_file
from os.path import join

last_log = []

def get(url):
    "Simple GET request."
    response = requests.get(url)
    last_log.clear()
    last_log.append(response.text)
    return response

def xml_post(url, payload=None, target_app='text'):
    "XML post request with text/xml as standard content type."
    headers = {'Content-Type': target_app + '/xml; charset=UTF-8'}
    response = requests.post(url, payload, headers=headers)
    log(payload, response)
    return response

def xml_post_file(url, payload_file, target_app='text'):
    "XML post request from file."
    headers = {'Content-Type': target_app + '/xml; charset=UTF-8'}
    content = str(swallow_file(payload_file)).rstrip()
    files = {'upload_file': content}
    response = requests.post(url, files=files, headers=headers)
    log(response.headers, response)
    return response

def post(url, payload=None, json=None, **arguments):
    "Simple POST request."
    response = requests.post(url, payload, json, **arguments)
    log(payload, response)
    return response

def log(request, response):
    "Logs the given request and its response."
    last_log.clear()
    last_log.append(request)
    last_log.append(response.text)
    dump_in_file("log", last_log[0])
    append_to_file("log", last_log[1])
    return last_log
