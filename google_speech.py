"""Google Cloud Speech API sample application using the REST API for batch
processing."""

import argparse
import base64
import json
import sys

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')

API_KEY = "AIzaSyALQzz-AS-67fx3AUR45Q9ZmWI9F_L821o"

def get_speech_service():
#    credentials = GoogleCredentials.get_application_default().create_scoped(
#        ['https://www.googleapis.com/auth/cloud-platform'])
#    credentials.authorize(http)

    http = httplib2.Http()
    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL, developerKey=API_KEY)


def parse_file(speech_file):
    """Transcribe the given audio file.

    Args:
        speech_file: the name of the audio file.
    """

    print("START: open file and base64 decode")
    with open(speech_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())
    print("END: open file and base64 decode")        

    service = get_speech_service()

    print("START: setup request and decode content as UTF8")
    content = speech_content.decode('UTF-8')
    print("Size in bytes: ", sys.getsizeof(content))
    print("Size in megabytes: ", (sys.getsizeof(content) / 1000000.0))

    service_request = service.speech().asyncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRate': 16000,  # 16 khz
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': content
                }
            })
    print("END: setup request and decode content as UTF8")

    print("START: make the request")
    response = service_request.execute()
    print("END: make the request")

    print("START: dump response to JSON and print")
    print(json.dumps(response))
    print("END: dump response to JSON and print")

def parse_uri(speech_file):
    service = get_speech_service()
    service_request = service.speech().asyncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRate': 16000,  # 16 khz
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'uri' : speech_file
                }
            })

    print("START: make the request")
    response = service_request.execute()
    print("END: make the request")

    print("START: dump response to JSON and print")
    print(json.dumps(response))
    print("END: dump response to JSON and print")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
#    parse_file(args.speech_file)
    parse_uri(args.speech_file)
