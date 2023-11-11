import requests

def get_access_token():

    client_id = '216'
    client_secret = '7f90c58a2cf9e812d73973508bd23b20'
    scope = 'system/*.*'

    form_params = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope
    }

    token_url = "https://app.azaleahealth.com/fhir/R4/142442/oauth/token"

    response = requests.post(token_url, data=form_params)
    response.raise_for_status()

    token_data = response.json()
    return token_data['access_token']


def get_all_patients():

    access_token = get_access_token()

    get_url = "https://app.azaleahealth.com/fhir/R4/142442/Patient"
    headers = { 'Authorization': f'Bearer {access_token}' }

    response = requests.get(get_url, headers=headers)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")

def get_patient(id):
    
    access_token = get_access_token()

    get_url = f"https://app.azaleahealth.com/fhir/R4/142442/Patient?_id={id}"
    headers = { 'Authorization': f'Bearer {access_token}' }

    response = requests.get(get_url, headers=headers)
    response.raise_for_status()

    response_json = response.json()

    patient_information = {
        'name': response_json['entry'][0]['resource']['name'][0]['text']
    }

    if response.status_code == 200:
        return patient_information['name']
    else:
        print(f"Error: {response.status_code}")