def wsgi_application(environ, start_response):
    result = [(i + '\n').encode() for i in environ['QUERY_STRING'].split('&')]
    start_response('200 OK', [('Content-type', 'text/plain'), ])
    return result