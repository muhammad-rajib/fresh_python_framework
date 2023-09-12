# app.py
from api import API
from middleware import Middleware


app = API()

# Exception handler
def custom_exception_handler(request, response, exception_cls):
    # response.text = "Oops! Something went wrong. Please, contact out customer support at +1-202-xxx"
    response.body = app.template(
        'exception.html', 
        context={'msg': "Oops! Something went wrong !!!"
        }).encode()

app.add_exception_handler(custom_exception_handler)


# Middleware
class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print('Processing request: ', req.url)

    def process_response(self, req, resp):
        print('Processing response', req.url)

app.add_middleware(middleware_cls=SimpleCustomMiddleware)



@app.route('/wow_exception')
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be user")


@app.route("/city")
class BooksHandler:
    def get(self, req, resp):
        resp.text = "Dhaka, Tokyo, Kolkatta"

    def post(self, req, res, name):
        resp.text = f"New city {name} added succesfully !"


@app.route("/home/{name}/")
def home(request, response, name):
    print(f'Step 5: Update response text by this name: {name}')
    response.text = f"Hello, {name}"


@app.route("/about")
def about(request, response):
    response.text = "Hello Sakalaka! from the ABOUT page"


def amazing(request, response):
    response.text = 'Amazing'
    print(response)

def amazing2(req, resp):
    resp.text = 'Absolutely Amazing'


def awesome_index(req, resp):
    resp.body = app.template('index.html', context={"title": "Just Awesome Framework !!!", "name": "Awesome Bee"}).encode()

# routes list
app.add_route('/wow', amazing)
app.add_route('/wow2', amazing2)
app.add_route('/index', awesome_index)
