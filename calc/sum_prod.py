from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    error = "No Error"
    sum, prod = "a와 b를 입력하면 합이 출력됩니다", "a와 b를 입력하면 곱이 출력됩니다"
    if '' not in [a, b]:
        sum, prod = 0, 0
        a, b = int(a), int(b)
        sum = a + b
        prod = a * b
        sum, prod = str(sum), str(prod)
    response_body = html % {'sum':sum, 'prod':prod, 'error':error}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
