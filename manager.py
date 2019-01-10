# coding:utf8
'''
https://v4.bootcss.com/docs/4.0/components/carousel/
'''
#  import packages
from wtforms import StringField,SubmitField,TextAreaField
from flask import  render_template, jsonify, request, make_response, url_for,session,redirect
from flask_wtf import Form as FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,RadioField,SelectField
import json,os,pickle,os
from flask import Flask
#   forms
class cnwForm(FlaskForm):
    isp_info = TextAreaField('content', validators=[DataRequired()])
    sub = SubmitField('Submit')

# app start
app = Flask(__name__)
app.config['SECRET_KEY'] = 'lz'
@app.route('/')
def mainIndex():
    form = cnwForm()
    info =False
    if session.get('data'):
        info = session['data']
        session.clear()
    else:
        pass
    return render_template('cnw.html',form=form,data=info)

@app.route('/gettran', methods=['POST',])
def maingetCnw():
    form=cnwForm()
    dd = {}
    u = form.isp_info.data
    dd['en'] = 'this is engins'
    dd['cn'] = 'this is chinese'
    session['data'] = dd
    return redirect(url_for('mainIndex'))

# flask post api
@app.route('/postapi', methods=['POST',])
def return_api():
    res = {}
    if request.method == 'POST':
        sn = request.values['sn']
        res['model'] = search_redis(sn)
    return jsonify(res)

#    page 404 not found
'''
@app.errorhandler(Exception)
def all_exception_handler(e):
    #return 'Error', 500
    return render_template('404.html')
'''
if __name__ == '__main__':
    app.run(debug=True)