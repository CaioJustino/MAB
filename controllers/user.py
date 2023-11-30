# IMPORTS
from flask import render_template, request, url_for, redirect, flash, Blueprint, session
from utils.utils import db, lm
from utils.models import User, Passageiro, Motorista
from flask_login import login_user, logout_user, login_required, current_user
import hashlib

# CONFIGS
bp_user = Blueprint("user", __name__, template_folder="templates")

# LOAD 
@lm.user_loader
def load_user(id):
  u = User.query.filter_by(id=id).first()
  return u

# LOGIN
@bp_user.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'GET':
    if current_user.is_authenticated:
      if current_user.adm == 1:
        return redirect('/administrador/perfil')
        
      elif Passageiro.query.filter_by(id = current_user.id).count() == 1:
          return redirect('/passageiro/perfil')
          
      elif Motorista.query.filter_by(id = current_user.id).count() == 1:
          return redirect('/motorista/perfil')
            
    else:        
      return render_template('login.html')
  
  elif request.method == 'POST':
    email = request.form.get('email')
    senha = hashlib.md5(request.form.get('senha').encode()).hexdigest()
    user = User.query.filter_by(email = email).first()
   
    if (User.query.filter_by(email = email).count()) == 1:
      if senha == user.senha:
        if user.status == 0:
          return redirect(url_for('user.reativar_cadastro', id = user.id))
  
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
            
    else:
      flash("Dados incorretos!", "danger")
      return redirect(url_for('user.login'))

# LOGOUT
@bp_user.route('/logoff')
@login_required
def logoff():
  session.pop("google_token", None)
  logout_user()
  return redirect('/')

# REATIVAR
@bp_user.route('/reativar/conta/<int:id>', methods=['GET','POST'])
def reativar_cadastro(id):
  if request.method == 'GET':
    if current_user.is_authenticated:
      if current_user.adm == 1:
        return redirect('/administrador/perfil')
        
      elif Passageiro.query.filter_by(id = current_user.id).count() == 1:
        return redirect('/passageiro/perfil')
          
      elif Motorista.query.filter_by(id = current_user.id).count() == 1:
        return redirect('/motorista/perfil')
            
    else:
      return render_template('reativar_cadastro.html', id = id)
  
  elif request.method == 'POST':
    user = User.query.filter_by(id = id).first()
    user.status = 1
    db.session.commit()

    flash("Cadastro reativado!", "success")
    return redirect(url_for('user.login'))