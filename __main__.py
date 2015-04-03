from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField
from gprof2dot import convert_to_dot
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class ExampleForm(Form):
    profiler_output = TextAreaField()
    submit_button = SubmitField('Submit')



def create_app(config_file=None):
    app = Flask(__name__)
    AppConfig(app, config_file)
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = ExampleForm(request.form)
        if request.method == 'POST' and form.validate():
	    form.validate_on_submit()
            graph = convert_to_dot(form.profiler_output)
            return render_template('graph.html', dot_graph=graph)
        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)

