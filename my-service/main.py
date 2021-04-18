import json
import requests
from google.cloud import pubsub

URL = "https://yuya-okada.com/v1/movie/search?query="

CLIENT: pubsub.PublisherClient = None

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


def publish(event, context):

    # クライアントを初期化
    global CLIENT
    if not CLIENT:
        CLIENT = pubsub.PublisherClient()

    # メッセージとメタデータを作成
    attributes = {
        "bucket": event["attributes"]["bucketId"]
    }
    message = json.dumps(attributes).encode()

    # パブリッシュ
    topic = CLIENT.topic_path("ml-playground-306716", "sample-publish-topic")
    CLIENT.publish(topic=topic, data=message, **attributes)


def subscribe(event, context):
    print(event)
