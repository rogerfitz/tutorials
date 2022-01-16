import json
import ntpath

import requests

from secret_services import service_region, tts_subscription_key


def get_headers():
    headers = {
        'Ocp-Apim-Subscription-Key': tts_subscription_key
    }
    return headers


def get_voices():
    url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis/voices'.format(service_region)

    response = requests.get(url, headers=get_headers())
    return response.json()

def submit_synthesis(input_file_path, locale="en-US",headers=get_headers(), region="eastus", voice_name="en-US-GuyNeural"):
    url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis'.format(region)

    voice_identities = [
        {
            'voicename': voice_name
        }
    ]

    payload = {
        'displayname': 'long audio synthesis sample',
        'description': 'sample description',
        'locale': locale,
        'voices': json.dumps(voice_identities),
        'outputformat': 'riff-16khz-16bit-mono-pcm',
        'concatenateresult': True,
    }

    filename = ntpath.basename(input_file_path)
    files = {
        'script': (filename, open(input_file_path, 'rb'), 'text/plain')
    }

    response = requests.post(url, payload, headers=headers, files=files)
    return response