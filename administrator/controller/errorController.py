from django.shortcuts import (
    render_to_response
)

from django.conf import settings

from django.template import RequestContext

# HTTP Error 404
from django.template.context_processors import static


def page_not_found(request):

    response = render_to_response(
        '404.html',
        {"url": settings.MEDIA_URL},
        context_instance= RequestContext(request)
    )

    response.status_code = 404

    return response
