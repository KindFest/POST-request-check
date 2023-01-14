from tinydb import TinyDB
import type_validation as tv
from wsgiref.simple_server import make_server


def parse_input_data(data):
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env) -> bytes:
    content_length_data = env.get('CONTENT_LENGTH')
    content_length = int(content_length_data) if content_length_data else 0
    data = env['wsgi.input'].read(content_length) \
        if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        data_str = data.decode(encoding='utf-8')
        result = parse_input_data(data_str)
    return result


def get_post_query_view(data):
    templates_db = TinyDB('db.json')
    data_validated = {}
    for item in data:
        if tv.date_validation(data[item]):
            data_validated.update({item: 'date'})
            continue
        if tv.email_validation(data[item].upper()):
            data_validated.update({item: 'email'})
            continue
        if tv.phone_validation(data[item]):
            data_validated.update({item: 'phone'})
            continue
        if tv.text_validation(data[item]):
            data_validated.update({item: 'text'})
    template = ''
    field_dict_final = data_validated
    field_dict = {}
    template_db = {}
    for item in templates_db:
        template_db.update(item)
    for key, val in template_db.items():
        i = 0
        keys = val.keys()
        for item in data_validated:
            if item in keys and data_validated[item] == val[item]:
                i += 1
            else:
                field_dict.update({item: data_validated[item]})
        if i == 4:
            template = key
            break
        if i < 4:
            template = ''
            if len(field_dict) < len(field_dict_final):
                field_dict_final = field_dict
                field_dict = {}
    if template:
        print(template_db[template]['field_name'])  # - вывод результата в консоль
        return '200 OK', [b'Template name is ', template_db[template]['field_name'].encode()]
    else:
        print(field_dict_final)  # - вывод результата в консоль
        s = ''.join([f'"{k}": "{v}"\n' for k, v in sorted(field_dict_final.items())])
        return '200 OK', [s.encode()]


def not_found_404_view(data):
    return '404 WHAT', [b'404 PAGE Not Found or used not POST request']


routes = {
    '/get_form/': get_post_query_view,
}


class Application:

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            view = self.routes[path]
            data = get_wsgi_input_data(environ)
            data = parse_wsgi_input_data(data)
        else:
            view = not_found_404_view
            data = {}
        code, body = view(data)
        start_response(code, [('Content-Type', 'text/html')])
        return body


application = Application(routes)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
