# IMPORTS
from flask import render_template, request, url_for, redirect, flash, Blueprint
from sqlalchemy.orm import Session
from utils.utils import db
from utils.models import User, Passageiro, Viagem, Motorista, Pagamento
from flask_login import login_required, logout_user, current_user
import hashlib
from datetime import datetime

# CONFIGS
bp_pass = Blueprint("pass", __name__, template_folder="templates")

# CADASTRO
@bp_pass.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'GET':
    if current_user.is_authenticated:
      if current_user.adm == 1:
        return redirect('/administrador/perfil')
      
      else:
        if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
          return redirect('/passageiro/perfil')
          
        elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
          return redirect('/motorista/perfil')
    else:
      return render_template('pass/cadastro.html')

  elif request.method == 'POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    data_nasc = request.form.get('data_nasc')
    data_nasc_db = datetime.strptime(data_nasc, '%Y-%m-%d').date()
    tel = request.form.get('tel')
    senha = request.form.get('senha')
    csenha = request.form.get('csenha')
    deficiencia = request.form.get('deficiencia')

    if senha != "" and csenha != "" and senha != csenha:
      flash("Senhas diferentes!", "warning")
      return redirect(url_for('pass.cadastro'))

    else:
      if ((User.query.filter_by(email = email)) or (User.query.filter_by(tel = tel))).count() == 1:
       flash("Esses dados já foram utilizados! Por favor, tente outros.", "danger")
       return redirect(url_for('pass.cadastro'))

      else:
        senha = hashlib.md5(request.form.get('senha').encode()).hexdigest()
        u = User(nome, data_nasc_db, email, tel, senha, False, True)
        db.session.add(u)
        db.session.commit()
        passg = Passageiro(u.id, deficiencia)
        db.session.add(passg)
        db.session.commit()

        flash("Cadastro concluído com sucesso!", "success")
        return redirect(url_for('user.login'))

# PERFIL
@bp_pass.route('/perfil', methods=['GET'])  
@login_required
def perfil():
  if current_user.adm == 1:
    return redirect('/administrador/perfil')
    
  else:
    if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      passg = Passageiro.query.filter_by(id = current_user.id).first()
      viagem = Viagem.query.filter_by(id_pass = current_user.id).filter(Viagem.id_moto != 0).filter_by(status = 0).order_by(Viagem.id.desc()).limit(1).all()
      vi_count = Viagem.query.filter_by(id_pass = current_user.id).filter(Viagem.id_moto != 0).count()
      return render_template('pass/perfil.html', passg = passg, viagem = viagem, vi_count = vi_count)
      
    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

# HISTÓRICO DE VIAGENS
@bp_pass.route('/historico', methods=['GET','POST'])  
@login_required
def historico():
  if current_user.adm == 1:
    return redirect('/administrador/perfil')

  else:
    if Viagem.query.filter_by(id_pass = current_user.id).filter(Viagem.id_moto != 0).count() == 0:
      return redirect('/passageiro/perfil')

    elif Viagem.query.filter_by(id_pass = current_user.id).filter(Viagem.id_moto != 0).count() >= 1:
      if request.form.get('search') != None:
        filter = request.form.get('filter')
        search = request.form.get('search')

        if filter == "embarque":
          viagens = (db.session.query(Viagem, User, Pagamento).join(User, Viagem.id_moto == User.id).join(Passageiro, Viagem.id_pass == Passageiro.id).join(Pagamento, Viagem.id_pag == Pagamento.id).filter(Viagem.id_pass == current_user.id).filter(Viagem.embarque.like(f'%{search}%')).order_by(Viagem.id.desc()).all())
          return render_template('pass/historico.html', viagens = viagens, search = search, filter = filter)

        elif filter == "desembarque":
          viagens = (db.session.query(Viagem, User, Pagamento).join(User, Viagem.id_moto == User.id).join(Passageiro, Viagem.id_pass == Passageiro.id).join(Pagamento, Viagem.id_pag == Pagamento.id).filter(Viagem.id_pass == current_user.id).filter(Viagem.desembarque.like(f'%{search}%')).order_by(Viagem.id.desc()).all())
          return render_template('pass/historico.html', viagens = viagens, search = search, filter = filter)

        elif filter == "moto":
          viagens = (db.session.query(Viagem, User, Pagamento).join(User, Viagem.id_moto == User.id).join(Passageiro, Viagem.id_pass == Passageiro.id).join(Pagamento, Viagem.id_pag == Pagamento.id).filter(Viagem.id_pass == current_user.id).filter(User.nome.like(f'%{search}%')).order_by(Viagem.id.desc()).all())
          return render_template('pass/historico.html', viagens = viagens, search = search, filter = filter)

      else:
        viagens = (db.session.query(Viagem, User, Pagamento).join(User, Viagem.id_moto == User.id).join(Passageiro, Viagem.id_pass == Passageiro.id).join(Pagamento, Viagem.id_pag == Pagamento.id).filter(Viagem.id_pass == current_user.id).order_by(Viagem.id.desc()).all())
        return render_template('pass/historico.html', viagens = viagens)
      
    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')
      
# EDITAR
@bp_pass.route('/perfil/editar', methods=['GET','POST'])
@login_required
def update():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect('/administrador/perfil')
      
    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        passg = Passageiro.query.get(current_user.id)
        return render_template('pass/update.html', passg=passg)
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/motorista/perfil')

  elif request.method == 'POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    data_nasc = request.form.get('data_nasc')
    data_nasc_db = datetime.strptime(data_nasc, '%Y-%m-%d').date()
    tel = request.form.get('tel')
    deficiencia = request.form.get('deficiencia')
    
    user = User.query.filter_by(id = current_user.id).first()
    passg = Passageiro.query.filter_by(id = current_user.id).first()
    user.nome = nome
    user.data_nasc = data_nasc_db
    passg.deficiencia = deficiencia

    if User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 1:
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar o e-mail e o telefone, tente outros.","success")
      return redirect(url_for('pass.update'))
            
    elif User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 0:
      user.tel = tel
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar o e-mail, tente outro." ,"success")
      return redirect(url_for('pass.update'))
    
    elif User.query.filter_by(email = email).count() == 0 and User.query.filter_by(tel = tel).count() == 1:
      user.email = email
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar o telefone, tente outro.","success")
      return redirect(url_for('pass.update'))
  
    else:
      user.email = email
      user.tel = tel
      db.session.commit()
      flash("Dados atualizados com sucesso!","success")
      return redirect(url_for('pass.update'))

# ALTERAR SENHA
@bp_pass.route('/perfil/alterar-senha', methods=['GET','POST'])
@login_required
def update_senha():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect('/administrador/perfil')
      
    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        return render_template('pass/update_senha.html')
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/motorista/perfil')

  elif request.method == 'POST':
    senha = request.form.get('senha')
    csenha = request.form.get('csenha')
    
    if senha != csenha:
      flash('Senhas diferentes!', 'warning')
      return redirect('/passageiro/perfil/alterar-senha')
  
    else:
      user = User.query.filter_by(id = current_user.id).first()
      user.senha = hashlib.md5(request.form.get('senha').encode()).hexdigest()
      db.session.commit()
      logout_user()
      flash('Senha atualizada com sucesso!', 'success')
      return redirect('/login')

# DELETAR
@bp_pass.route('/perfil/desativar', methods=['GET','POST'])
@login_required
def delete():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect('/administrador/perfil')
      
    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        return render_template('pass/delete.html')
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/motorista/perfil')

  elif request.method == 'POST':
    user = User.query.filter_by(id = current_user.id).first()
    user.status = 0
    db.session.commit()
    
    logout_user()
    flash('Desativamos o seu cadastro. Esperamos revê-lo em breve!', "success")
    return redirect('/')