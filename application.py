import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.insert(0, '/opt/python/current/app')


from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField
from gprof2dot import gprof_hack
import json


class ExampleForm(Form):
    profiler_output = TextAreaField()
    submit_button = SubmitField('Submit')

application = Flask(__name__)
application.debug = True
AppConfig(application, None)
Bootstrap(application)

# in a real app, these should be configured through Flask-Appconfig
application.config['SECRET_KEY'] = 'devkey'
application.config['RECAPTCHA_PUBLIC_KEY'] = \
'6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

@application.route('/', methods=['GET', 'POST'])
def index():

    form = ExampleForm(request.form)
    if request.method == 'POST' and form.validate():
        form.validate_on_submit()
        graph = gprof_hack.convert_to_dot(form.profiler_output.data)
        return render_template('graph.html', dot_graph=graph)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    application.run(host='0.0.0.0')

