import requests

URL = "https://yuya-okada.com/v1/movie/search?query="

def http(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    q = request.args.get("q")
    url = URL + (q if q else "")
    res = requests.get(url)

    return res.json()
