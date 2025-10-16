import requests
import json
import os


def search(params, url, headers,
           get_element="results"):
    response = requests.get(url, params=params, headers=headers)
    data = json.loads(response.text)
    print(data)
    return data.get(get_element)


def post(data, url, headers,
         get_element="results"):
    response = requests.post(url, data=data, headers=headers)
    result = json.loads(response.text)
    # print(result)
    return result.get(get_element)


def search_by_maps(query, api_key=os.environ['GOOGLEMAPS_API_KEY']):
    results = search({"query": query, "key": api_key, },
                     url=f"https://maps.googleapis.com/maps/api/place/textsearch/json", get_element="results")
    # print(results)
    return results


def search_by_places(query, api_key=os.environ['GOOGLEMAPS_API_KEY']):
    results = post(json.dumps({"textQuery": query}),
                   url=f"https://places.googleapis.com/v1/places:searchText",
                   headers={"accept": "application/json", "content-type": "application/json",
                            "X-Goog-FieldMask": "places.id,places.displayName.text,places.formattedAddress,places.priceLevel,places.currentOpeningHours.weekdayDescriptions,places.websiteUri,places.googleMapsUri,places.rating,places.userRatingCount",
                            "X-Goog-Api-Key": api_key},
                   get_element="places")
    # print(results)
    return results


def search_by_placeid(placeid, api_key=os.environ['GOOGLEMAPS_API_KEY']):
    result = search({"placeid": placeid, "key": api_key, },
                    url=f"https://maps.googleapis.com/maps/api/place/details/json", get_element="result")
    return result
