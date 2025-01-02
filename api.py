import json
import requests
import boto3


secrets = json.loads(
        boto3.client('secretsmanager').get_secret_value(
            SecretId='gulp-backend-automation/flipper'
        )['SecretString']
    )

ENDPOINT = secrets['DB_BASE_URL']
TYPE = "application/json"
HEADERS = {
        "Content-Type": TYPE,
        "x-api-key": secrets['DB_API_KEY']
    }

def process_response(response, data_key):
    if response is None:
        return None
    if data_key:
        return response.json()[data_key]
    return response.json()


def do_request(url, method='GET', params=None, data=None):
    if method == 'GET':
        return requests.get(url, headers=HEADERS, params=params, timeout=60)
    if method == 'POST':
        return requests.post(
            url,
            headers=HEADERS,
            data=json.dumps(data),
            params=params, timeout=60
        )
    return None


def fetch_with_pagination(url, method='GET', params=None, data=None, data_key=None, limit=5, offset=0):
    results = []

    while True:
        if params is None:
            params = {}
        params.update({'limit': limit, 'offset': offset})
        try:
            response = do_request(url, method, params, data)
            if response is not None:
                response.raise_for_status()

            new_results = process_response(response, data_key)
            if not new_results:
                break
            results.extend(new_results)
            offset += limit
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    return results


def get_all_valuations(limit=100, extra_attr:list=[]):
    url = f"{ENDPOINT}data-py/valuations"
    params = { 'gboost': 25000, 'attributesCount' : 8}
    if len(extra_attr) > 0:
        params.update({'extraAttr': ",".join(extra_attr)}) # type: ignore

    return fetch_with_pagination(
        url,params=params,
        data_key='valuations',
        limit=limit,
    )

def do_request(url, method='GET', params=None, data=None):
    if method == 'GET':
        return requests.get(url, headers=HEADERS, params=params, timeout=60)
    if method == 'POST':
        return requests.post(
            url,
            headers=HEADERS,
            data=json.dumps(data),
            params=params, timeout=60
        )
    return None