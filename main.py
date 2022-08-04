import temperature
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
import calorie

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):

        calories_form = CaloriesForm()

        return render_template('calories_form_page.html', form=calories_form)

    def post(self):

        form = CaloriesForm(request.form) #requests.form was to be used in the declaration when post
        weight = float(form.weight.data)
        height = float(form.height.data)
        age = float(form.age.data)
        country = form.country.data
        city = form.city.data
        temp = temperature.Temperature(country, city).get()
        calories = calorie.Calorie(weight, height, age, temp).calculate()
        return render_template('calories_form_page.html',
                               result=True,
                               form=form,
                               calories=calories)


class CaloriesForm(Form):
    weight = StringField('Weight: ')
    height = StringField('Height: ')
    age = StringField('Age: ')
    country = StringField('Country: ')
    city = StringField('City: ')
    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form_page', view_func=CaloriesFormPage.as_view('calories_page'))

app.run(debug=True)