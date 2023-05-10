from flask import Flask, render_template, request
from random import randint

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")
l = ['screen1.jpg', 'screen2.jpg', 'screen3.jpg', 'screen4.jpg', 'screen5.jpg', 'screen6.jpg', 'screen7.jpg',
     'screen8.jpg', 'screen9.jpg', 'screen10.jpg']
Name = 'Друг'


@app.route('/')
def home():
    x = randint(0, 9)
    return render_template('home.html', Name=Name, screen=l[x])


@app.route('/contact')
def contact():
    return render_template('contact.html', Name=Name)


@app.route('/what_is_name', methods=['GET', 'POST'])
def what_is_name():
    global Name

    if request.method == 'POST':
        name_param = request.form.get('Name')
        Name = name_param
        return render_template(
            'home.html',
            Name=Name, screen=l[randint(0, 10)]
        )
    elif request.method == 'GET':
        name_param = Name

        return render_template(
            'what_is_name.html',
            Name=name_param,
            method=request.method
        )


if __name__ == '__main__':
    app.run()
