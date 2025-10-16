import requests
import json
import os


def post(data, url, headers):
    response = requests.post(url, data=data,
                             headers=headers or {"accept": "application/json", "content-type": "application/json"})
    result = json.loads(response.text)
    # print(result)
    return result


def validate_address(address, api_key=os.environ['GOOGLEMAPS_API_KEY']):
    results = post(json.dumps(address),
                   url=f"https://addressvalidation.googleapis.com/v1:validateAddress",
                   headers={"accept": "application/json", "content-type": "application/json",
                            "X-Goog-Api-Key": api_key})
    # print(results)
    return results


def main():
    result = validate_address({
        "address": {
            "regionCode": "US",
            "addressLines": ["9 bedford drive"]
        },
    })

    print(result)


if __name__ == "__main__":
    main()
