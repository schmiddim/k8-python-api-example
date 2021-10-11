import requests


def get_time_from_web(url1, url2):
    try:
        a = requests.get(url1).json()
        return a
    except Exception as e:
        print(e)
        try:
            b = requests.get(url2).json()
            return b
        except Exception as e2:
            raise Exception("no valid responses")
