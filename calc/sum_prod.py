from cgi import parse_qs
from template import html

#for modify mistkae 
def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    sum, prod = 0, 0
    if '' not in [a, b]:
        a, b = int(a), int(b)
        sum1 = a + b
        product1 = a * b
    response_body = html % {'sum':sum, 'prod':prod}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
       ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
