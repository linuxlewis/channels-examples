from channels import route, route_class
from channels.generic.websockets import WebsocketDemultiplexer

from posts.bindings import LiveblogResource

class APIDemultiplexer(WebsocketDemultiplexer):

    mapping = {
        'liveblogs': 'liveblogs'
    }


# The channel routing defines what channels get handled by what consumers,
# including optional matching on message attributes. WebSocket messages of all
# types have a 'path' attribute, so we're using that to route the socket.
# While this is under stream/ compared to the HTML page, we could have it on the
# same URL if we wanted; Daphne separates by protocol as it negotiates with a browser.
channel_routing = [
    route_class(APIDemultiplexer),
    route("liveblogs", LiveblogResource.consumer)

    # A default "http.request" route is always inserted by Django at the end of the routing list
    # that routes all unmatched HTTP requests to the Django view system. If you want lower-level
    # HTTP handling - e.g. long-polling - you can do it here and route by path, and let the rest
    # fall through to normal views.
]
