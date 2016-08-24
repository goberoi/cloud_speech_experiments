# Script to call Google Cloud Speech API asynchronously for sound files > 1m long.
#
# To run this script: python google_speech.py -h
#
# Originally inspired from: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/speech/api/speech_async_rest.py
# Licensed under the Apache License, Version 2.0 (the "License"): http://www.apache.org/licenses/LICENSE-2.0


import argparse
import base64
import json
import time
import os
from datetime import datetime

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


# Global internal vars
_SPEECH_SERVICE = None


# Set an API KEY to the environment variable GOOGLE_API_KEY
def get_speech_service():
    global _SPEECH_SERVICE
    if not _SPEECH_SERVICE:
        _SPEECH_SERVICE =  discovery.build(
            'speech',
            'v1beta1',
            http=httplib2.Http(),
            developerKey=os.environ['GOOGLE_API_KEY'])
    return _SPEECH_SERVICE


def process_speech_uri(speech_uri):
    """Transcribe the given audio file uri asynchronously.
    Args:
        speech_uri: the audio file uri.
    """

    service = get_speech_service()
    service_request = service.speech().asyncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',
                'sampleRate': 44100, 
                'languageCode': 'en-US',
            },
            'audio': {
                'uri' : speech_uri
                }
            })
    response = service_request.execute()

    print(json.dumps(response))

    fetch_job_result(response['name'])

    
def fetch_job_result(name):
    service = get_speech_service()
    service_request = service.operations().get(name=name)

    while True:
        # Get the long running operation with response.
        response = service_request.execute()

        if 'done' in response and response['done']:
            break
        else:
            # Give the server a few seconds to process.
            print('%s, waiting for results from job, %s' % (datetime.now().replace(second=0, microsecond=0), name))
            time.sleep(60)

    print(json.dumps(response))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--uri', required=False, help='URI of audio file. Must be hosted on Google, e.g.: gs://example-content/ben-podcast-waze.flac')
    parser.add_argument('-n','--name', required=False, help='Name of a job that is in progress.')
    args = parser.parse_args()
    if args.uri:
        process_speech_uri(args.uri)
    elif args.name:
        fetch_job_result(args.name)
    else:
        parser.print_help()
