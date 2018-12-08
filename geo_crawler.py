from flask import Flask, render_template, request

import requests
import json 

app = Flask(__name__)


def lenSort(e):
    """Gets length of array for sorting"""
    return len(e)


@app.route('/', methods=['POST', 'GET'])
def locations():
    """Route which returns the geo location json data"""

    api_endpoint = 'https://app.wordstream.com/services/v1/wordstream/interview_data';

    json_data_dict = requests.get(api_endpoint).json()

    region_hitlist = []
    city_hitlist = []
    country_hitlist = []
    zip_hitlist = []
    geo_markets_hitlist = []

    for dataset in json_data_dict['data']:
        try:
            for loc in dataset['targeting']['geo_locations']:
                if loc == "regions":
                    region_hitlist.append({"regions": dataset['targeting']['geo_locations'][loc]})
                if loc == "countries":
                    country_hitlist.append({"countries": dataset['targeting']['geo_locations'][loc]})
                if loc == "cities":
                    city_hitlist.append({"cities": dataset['targeting']['geo_locations'][loc]})
                if loc == "zips":
                    zip_hitlist.append({"zips": dataset['targeting']['geo_locations'][loc]})
                if loc == "geo_markets":
                    geo_markets_hitlist.append({"geo_markets": dataset['targeting']['geo_locations'][loc]})
        except:
            print('no geo_locations key');

    # Store all lists in list for sorting then sort.
    all_hitlists = [
        region_hitlist,
        city_hitlist,
        country_hitlist,
        zip_hitlist,
        geo_markets_hitlist
    ]

    all_hitlists.sort(reverse=True, key=lenSort)

    return json.dumps(all_hitlists)


if __name__ == '__main__':
    app.run(debug=True)