from flask import Flask, render_template, request


my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('form.html')

@my_app.route('/submitted')
def submitted():
    return render_template('submitted.html', name = request.args["name"], method = request.method)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
