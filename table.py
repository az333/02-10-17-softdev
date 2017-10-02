from flask import Flask, render_template


my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('form.html', title = "Form") 


if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
