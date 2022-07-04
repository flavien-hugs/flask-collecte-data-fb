from flask import Flask, render_template, url_for, request
from apps.utils import find_content

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def indexView():

    user_name = 'Flavien HUGS'
    user_image = url_for('static', filename='tmp/cover_111823112767411.jpg')
    user_description = """
    Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi.
    D'ailleurs, Koh Lanta est ton émission préférée !
    Bientôt tu partiras les cheveux au vent sur ton radeau.
    Tu es aussi un idéaliste chevronné. Quelle chance !
    """

    return render_template(
        'index.html',
        user_name=user_name,
        user_image=user_image,
        user_description=user_description,
        blur=True
    )


@app.route('/contents/<int:content_id>/')
def content(content_id):
    return content_id


@app.route('/result/')
def resultView():

    user_id = request.args.get('id')
    user_gender = request.args.get('gender')
    user_name = request.args.get('first_name')
    user_image = 'http://graph.facebook.com/' + user_id + '/picture?type=large'
    user_description = find_content(gender).description

    return render_template(
        'result.html',
        user_name=user_name,
        user_image=user_image,
        user_description=user_description
    )


if __name__ == "__main__":
    app.run()
