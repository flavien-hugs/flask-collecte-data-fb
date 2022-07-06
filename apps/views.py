from .utils import find_content
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def indexView():

    if 'img' in request.args:
        img = request.args.get('img')
        opg_url = url_for('indexView', img=img, _external=True)
        opg_image = url_for('static', filename=img, _external=True)
    else:
        opg_url = url_for('indexView', _external=True)
        opg_image = url_for('static', filename='tmp/smaple.jpg', _external=True)

    user_name = 'Flavien HUGS'
    page_title = 'Le test ultime'
    user_image = url_for('static', filename='img/profile.png')
    opg_description = "Découvre qui tu es vraiment en faisant le test ultime"
    description = """
        Toi, tu sais comment utiliser la console !
        Jamais à court d'idées pour réaliser ton objectif,
        tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs 
        volontiers que tu as du caractère et que tu ne te laisses
        pas marcher sur les pieds. Un peu hacker sur les bords,
        tu aimes trouver des solutions à tout problème.
        N'aurais-tu pas un petit problème d'autorité ? ;-)
    """

    return render_template(
        'index.html',
        blur=True,
        user_name=user_name,
        page_title=page_title,
        user_image=user_image,
        description=description,
        opg_url=opg_url,
        opg_image=opg_image,
        opg_description=opg_description
    )


@app.route('/result/')
def resultView():

    user_id = request.args.get('id')
    user_gender = request.args.get('gender')
    user_name = request.args.get('first_name')
    opg_image = url_for('static', filename='tmp/smaple.jpg')
    opg_url = url_for('index', img=img, _external=True)
    user_image = 'http://graph.facebook.com/' + user_id + '/picture?type=large'
    description = find_content(gender).description

    return render_template(
        'result.html',
        opg_url=opg_url,
        user_name=user_name,
        user_image=user_image,
        description=description
    )
