# -*- coding: utf-8 -*-
# @Author  : ly

from flask import Flask , render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


@app.route('/profile/<uid>')
def profile(uid):
    return 'profile:' + uid


@app.route('/profile1/<int:uid>/', methods=['GET'])
def profile1(uid):
    # return 'profile1:' + str(uid)
    colors = ('red', 'green')
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, infos=infos, colors=colors)


@app.route('/newpath')
def newpath():
    return 'newpath'


@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)


if __name__ == '__main__':
    app.run(debug=True)