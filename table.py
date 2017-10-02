from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/', methods = ["POST", "GET"])
def root():
    print request
    print request.headers
    print request.method
    print request.range
    print "args"
    print request.args
    print request.args['input']
    return render_template('form.html', title = "Form") 


if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
