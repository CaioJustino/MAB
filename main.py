# IMPORTS
from flask import Flask, render_template, url_for, session, redirect, flash
from flask_migrate import Migrate
from flask_oauthlib.client import OAuth
from flask_login import login_user, current_user

# UTILS
from utils.utils import db, lm
from utils.models import User, Passageiro, Motorista

# CONTROLLERS
from controllers.user import bp_user
from controllers.adm import bp_adm
from controllers.passageiro import bp_pass
from controllers.motorista import bp_moto
from controllers.viagem import bp_vi

# CONFIGS
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MAB./2023'
app.jinja_env.filters['zip'] = zip

# BLUEPRINTS
app.register_blueprint(bp_user)
app.register_blueprint(bp_adm, url_prefix='/administrador')
app.register_blueprint(bp_pass, url_prefix='/passageiro')
app.register_blueprint(bp_moto, url_prefix='/motorista')
app.register_blueprint(bp_vi, url_prefix='/viagem')

# DATABASE
conexao = "mysql+pymysql://root@localhost/mab"
# conexao = "sqlite:///mabdb.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# MIGRATE (DATABASE CONECTION)
migrate = Migrate(app, db)

# LOGIN MANAGER
lm.init_app(app)

# OAUTH
oauth = OAuth(app)

# GOOGLE
google = oauth.remote_app(
  "google",
  consumer_key="147115892445-j2ita5dpa1e0kg6framt8j7e2sksmppb.apps.googleusercontent.com",
  consumer_secret="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",
  request_token_params={
      "scope": ["profile", "email"]
  },
  base_url="https://www.googleapis.com/oauth2/v1/",
  request_token_url=None,
  access_token_method="POST",
  access_token_url="https://accounts.google.com/o/oauth2/token",
  authorize_url="https://accounts.google.com/o/oauth2/auth",
)

# LOGIN
@app.route("/login/google")
def login_google():
  return google.authorize(callback=url_for("auth_google", _external=True))

# AUTHORIZED
@app.route("/auth/google")
def auth_google():
  resp = google.authorized_response()
  session["google_token"] = (resp["access_token"], "")
  user_info = google.get("userinfo")
  
  if User.query.filter_by(email = user_info.data.get("email")).count() == 1:
    user =  User.query.filter_by(email = user_info.data.get("email")).first()

    if user.status == 0:
      flash("Usuário Inválido!", "danger")
      return redirect(url_for('user.login'))

    else:
      login_user(user) 
  
      if current_user.adm == 1:
        return redirect('/administrador/perfil')
      
      else:
        if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
          return redirect('/passageiro/perfil')
          
        elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
          return redirect('/motorista/perfil')

  else:
    flash("Dados incorretos!", "danger")
    return redirect(url_for('user.login'))

@google.tokengetter
def get_google_oauth_token():
  return session.get("google_token")

# ROTAS - LANDING PAGE E ERROR

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/suporte')
def suporte():
  return render_template('suporte.html')

@app.errorhandler(401)
def acesso_negado(e):
  c = 401
  de = "Seu acesso a esta página foi negado."
  return render_template('erro.html', c = c, de = de), 404

@app.errorhandler(404)
def page_n_encontrada(e):
  c = 404
  de = "Página não encontrada. Por favor, verifique a url."
  return render_template('erro.html', c = c, de = de ), 404

@app.errorhandler(500)
def page_internt_error(e):
  c = 500
  de = "Dificuldade de processamento do servidor a partir de uma incompatibilidade ou configuração incorreta."
  return render_template('erro.html', c = c, de = de ), 404  

app.run(host='0.0.0.0', port=81)