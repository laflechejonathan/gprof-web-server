import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.insert(0, '/opt/python/current/app')

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flaskext.markdown import Markdown
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, RadioField
from gprof2dot import gprof_hack
from gprof2dot.gprof2dot import formats

class ExampleForm(Form):
    profiler_output = TextAreaField('Paste your profiler output here...')
    submit_button = SubmitField('Submit')

    radio_fields = [ (x,x) for x in formats.keys() if x not in ['sleepy']]
    profiler_type = RadioField('Profiler Format', choices = radio_fields)


application = Flask(__name__)
application.debug = True
AppConfig(application, None)
Bootstrap(application)
Markdown(application)

# in a real app, these should be configured through Flask-Appconfig
application.config['SECRET_KEY'] = 'devkey'
application.config['RECAPTCHA_PUBLIC_KEY'] = \
'6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

@application.route('/', methods=['GET', 'POST'])
def index():
    form = ExampleForm(request.form)
    if request.method == 'POST' and form.validate():
        form.validate_on_submit()
        graph = gprof_hack.convert_to_dot(form.profiler_output.data, form.profiler_type.data)
        return render_template('graph.html', dot_graph=graph)
    return render_template('index.html', form=form)

@application.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0')

