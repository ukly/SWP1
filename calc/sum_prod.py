from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    error = "No Error"
    sum, prod = "a와 b를 입력하면 합이 출력됩니다", "a와 b를 입력하면 곱이 출력됩니다"
    try:
        if '' not in [a, b]:
            sum, prod = 0, 0
            a, b = int(a), int(b)
            sum = a + b
            prod = a * b
            sum, prod = str(sum), str(prod)
    except (TypeError, ValueError):
        error = "정수를 입력해 주세요"
    except TimeOutError:
        error = "계산 값이 너무 큽니다(런타임 에러)"
    except SyntaxError:
        error = "소스 코드 내 문법 오류가 발생했습니다."
    except NameError:
        error = "소스 코드 내 객체의 이름이 잘못 입력되어있습니다."
    except IndentationError:
        error = "소스 코드 내 들여쓰기가 잘못된 부분이 있습니다."
    except KeyError:
        error = "소스 코드 내 키 값이 잘못 지정되어 있습니다."
    response_body = html % {'sum':sum, 'prod':prod, 'error':error}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
