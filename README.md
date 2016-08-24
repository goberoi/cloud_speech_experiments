# Experimenting with Cloud Speech Vendors

This was a quick experiment to see how Google Cloud Speech's transcription output looks for long sound files. As input, I used a ~63 minute FLAC file of an episode from the podcast [Acquired](http://www.acquired.fm/episodes/2016/8/3/acquired-episode-17-waze) (thanks [Ben](https://twitter.com/gilbert)!).

The code is a modified example from Google to run an asynchronous speech processing request. I had to call asyncRecognize because this is the only option if the audio length is greater than 1 minute. Furthermore, the format of the file must be LINEAR16 signed-integer little-endian encoded raw... see the audio format section, and resources sections below for processing tips.

This script currently only supports Google Cloud Speech for long recordings (>1m), and with the stated limitations above. I may or may not modify it later to include other speech vendor examples. For a more comprehensive tool to do this, see [Speech Recognition](https://github.com/Uberi/speech_recognition).


## Learnings

1. The output was not at all what I expected, and fairly disappointing; take a glance below.
1. I've had much better results with a short bit of speech, say 20s on their test page here: https://cloud.google.com/speech/
1. One possible issue is that the post-processing on the podcast audio created artifacts that led to inaccuracy. There is some indication this could be true based on their [best practices](https://cloud.google.com/speech/docs/best-practices), e.g. "All noise reduction processing should be disabled.".
1. Another concern is that Google Cloud Speech will try to return up to 30 guesses... unclear how long each guess can be. In the output below they are short phrases, but in my tests with 20 second long phrases on their site, I see much longer sentences per guess.
  * See "maxAlternatives" deep down in their API docs here: https://cloud.google.com/speech/reference/rest/v1beta1/RecognitionConfig

## Sample Output

The result for this [5 minute section](https://storage.cloud.google.com/example-content/5m-ben-podcast-waze.raw?_ga=1.96114268.1595850234.1461692478) of the podcast was:
```
{
  "response": {
    "@type": "type.googleapis.com/google.cloud.speech.v1beta1.AsyncRecognizeResponse",
    "results": [
      {
        "alternatives": [
          {
            "confidence": 0.31786352,
            "transcript": "Mississauga"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.92226779,
            "transcript": "weather for Bakersfield College"
          }
        ]
      }
    ]
  },
  "done": true,
  "name": "4920998656671129691",
  "metadata": {
    "lastUpdateTime": "2016-08-24T18:38:09.049576Z",
    "@type": "type.googleapis.com/google.cloud.speech.v1beta1.AsyncRecognizeMetadata",
    "startTime": "2016-08-24T18:33:03.320765Z",
    "progressPercent": 100
  }
}
```

For the [entire hour long podcast](https://storage.cloud.google.com/example-content/ben-podcast-waze.raw?_ga=1.53665000.1595850234.1461692478) it was:
```
{
  "response": {
    "@type": "type.googleapis.com/google.cloud.speech.v1beta1.AsyncRecognizeResponse",
    "results": [
      {
        "alternatives": [
          {
            "confidence": 0.31786352,
            "transcript": "Mississauga"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.92226779,
            "transcript": "weather for Bakersfield College"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.578178,
            "transcript": "Bed Bath & Beyond"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.70186234,
            "transcript": "ESPN"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.2595036,
            "transcript": "Bakersfield High School"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.93311942,
            "transcript": "White Castle"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.81802225,
            "transcript": "Kelly Services in Columbia Maryland"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.51821041,
            "transcript": "weather Chicago"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.30766535,
            "transcript": "Yahoo"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.31368122,
            "transcript": "Mexican grocery store"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.90448982,
            "transcript": "Facebook"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.26522613,
            "transcript": "sexy"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.69060469,
            "transcript": "restaurants in Los Angeles"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.49876788,
            "transcript": "American toxicology"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.63318396,
            "transcript": "Dumb Ways to Die"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.59668612,
            "transcript": "facebook.com"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.95454544,
            "transcript": "661 Sheldon"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.95454544,
            "transcript": "weather"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.3689521,
            "transcript": "open Facebook"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.57749414,
            "transcript": "restaurants"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.4529644,
            "transcript": "dictionary.com"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.95454544,
            "transcript": "browser"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.83804256,
            "transcript": "transgender"
          }
        ]
      },
      {
        "alternatives": [
          {
            "confidence": 0.63055462,
            "transcript": "Dublin Toyota"
          }
        ]
      }
    ]
  },
  "done": true,
  "name": "6402258854541648563",
  "metadata": {
    "lastUpdateTime": "2016-08-24T06:47:00.016904Z",
    "@type": "type.googleapis.com/google.cloud.speech.v1beta1.AsyncRecognizeMetadata",
    "startTime": "2016-08-24T05:40:58.702306Z",
    "progressPercent": 100
  }
}
```



## Setup

### Get an API key from Google

1. [Visit the Google Developer Console](https://console.developers.google.com/apis/dashboard) and create a new project.
2. For that project, click "Enable API" and add "Google Cloud Speech API"
3. For that project, click "Credentials" and create an "API Key".
4. Copy the key, and set it as the env variable GOOGLE_API_KEY to run the script.

### Get audio into the right format

To process Audio greater than 

```
# Install SOX on OSX
brew install sox --with-lame --with-flac --with-libvorbis

# Convert FLAC file I got from Ben to PCM LINEAR16 format
sox input/ben-podcast-waze.flac --channels=1 --bits=16 --rate=44100 --encoding=signed-integer --endian=little input/ben-podcast-waze.raw

# Optional: trim it down to try a smaller sample.
sox --rate 44100 --bits 16 --encoding signed-integer input/ben-podcast-waze.raw input/5m-ben-podcast-waze.raw trim 0 05:00
```

### Upload Audio

1. Visit https://console.cloud.google.com/storage/browser
2. Upload files and make them public.
3. URL is of the format: gs://yourbucketname/yourfilename, e.g: gs://example-content/5m-ben-podcast-waze.raw

### Install dependencies for script

```
pip install --upgrade google-api-python-client
```

### Run script

```
# Call script for this URL
```



## Useful resources

Audio cleanup:
* http://apple.stackexchange.com/questions/137108/how-can-i-add-support-for-flac-files-in-sox
* http://stackoverflow.com/questions/38926114/flac-file-with-google-cloud-speech-api-fails
* http://stackoverflow.com/questions/9667081/how-do-you-trim-the-audio-files-end-using-sox

Google dev:
* https://console.developers.google.com
* https://console.cloud.google.com/storage/browser

Google speech:
* https://cloud.google.com/speech/
* https://cloud.google.com/speech/reference/rest/v1beta1/RecognitionAudio
* https://cloud.google.com/speech/limits
* https://cloud.google.com/speech/support

Example code:


## Related businesses

Podcast transcription:
* https://www.popuparchive.com/
* https://www.audiosear.ch/
* https://castingwords.com/

## License

Apache License, Version 2.0 (the "License"): http://www.apache.org/licenses/LICENSE-2.0
