from channels_api.bindings import ResourceBinding

from .models import Liveblog
from .serializers import LiveblogSerializer

class LiveblogResource(ResourceBinding):

    model = Liveblog
    stream = "liveblogs"
    queryset = Liveblog.objects.all()
    serializer_class = LiveblogSerializer
