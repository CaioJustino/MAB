# IMPORTS
from flask import render_template, request, url_for, redirect, flash, Blueprint
from utils.utils import db
from utils.models import User, Motorista, Passageiro, Viagem, Veiculo
from flask_login import login_required, logout_user, current_user
import hashlib

# CONFIGS
bp_moto = Blueprint("moto", __name__, template_folder="templates")

# CADASTRO
@bp_moto.route('/cadastro', methods=['GET', 'POST'])
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
      return render_template('moto/cadastro.html')

  elif request.method == 'POST':  
    nome = request.form.get('nome')
    email = request.form.get('email')
    data_nasc = request.form.get('data_nasc')
    tel = request.form.get('tel')
    senha = request.form.get('senha')
    csenha = request.form.get('csenha')
    cnh = request.form.get('cnh')
    placa = request.form.get('placa')
    renavam = request.form.get('renavam')
    modelo = request.form.get('modelo')    
    marca = request.form.get('marca')
    cor = request.form.get('cor')
    ano = request.form.get('ano')

    if senha != "" and csenha != "" and senha != csenha:
      flash("Senhas diferentes!", "warning")
      return redirect('/cadastro')

    else:
      if ((User.query.filter_by(email = email)) or (User.query.filter_by(tel = tel)) or (Motorista.query.filter_by(cnh = cnh))).count() == 1:
       flash("Esses dados já foram utilizados! Por favor, tente outros.", "danger")
       return redirect('/motorista/cadastro')

      else:
        senha = hashlib.md5(request.form.get('senha').encode()).hexdigest()
        u = User(nome, data_nasc, email, tel, senha, False, True)
        db.session.add(u)
        db.session.commit()
        moto = Motorista(u.id, cnh)
        db.session.add(moto)
        db.session.commit()
        ve = Veiculo(u.id, placa, renavam, modelo, cor, marca, ano)
        db.session.add(ve)
        db.session.commit()
        flash("Cadastro concluído com sucesso!", "success")
        return redirect(url_for('user.login'))

# PERFIL
@bp_moto.route('/perfil', methods=['GET'])  
@login_required
def perfil():
  if current_user.adm == 1:
    return redirect('/administrador/perfil')
  
  else:
    if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/passageiro/perfil')
      
    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      moto = Motorista.query.filter_by(id = current_user.id).first()
      viagem = Viagem.query.filter_by(id_moto = current_user.id).filter_by(status = 0).order_by(Viagem.id.desc()).limit(1).all()
      vi_count = Viagem.query.filter_by(id_moto = current_user.id).count()
      return render_template('moto/perfil.html', moto=moto, viagem=viagem, vi_count=vi_count)

# HISTÓRICO DE VIAGENS
@bp_moto.route('/historico', methods=['GET'])  
@login_required
def historico():
  if current_user.adm == 1:
    return redirect('/administrador/perfil')

  else:
    if (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      moto = Motorista.query.filter_by(id = current_user.id).first()
      viagem = Viagem.query.filter_by(id_moto = current_user.id).filter_by(status = 0).order_by(Viagem.id.desc()).all()
      vi_count = Viagem.query.filter_by(id_moto = current_user.id).count()
      return render_template('moto/historico.html', moto = moto, viagem = viagem, vi_count = vi_count)

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

# EDITAR
@bp_moto.route('/perfil/editar', methods=['GET','POST'])
@login_required
def update():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect(url_for('/administrador/perfil'))

    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/passageiro/perfil')
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        moto = Motorista.query.get(current_user.id)
        return render_template('moto/update.html', moto=moto)

  elif request.method == 'POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    data_nasc = request.form.get('data_nasc')
    tel = request.form.get('tel')
    cnh = request.form.get('cnh')
    
    user = User.query.filter_by(id = current_user.id).first()
    moto = Motorista.query.filter_by(id = current_user.id).first()
    user.nome = nome
    user.data_nasc = data_nasc

    if User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 1 and Motorista.query.filter_by(cnh = cnh).count() == 1:
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar a cnh, o e-mail e o telefone, tente outros.","success")
      return redirect(url_for('moto.update'))
            
    elif User.query.filter_by(email = email).count() == 0 and User.query.filter_by(tel = tel).count() == 1 and Motorista.query.filter_by(cnh = cnh).count() == 1:
      user.email = email
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o telefone, tente outros." ,"success")
      return redirect(url_for('moto.update'))
        
    elif User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 0 and Motorista.query.filter_by(cnh = cnh).count() == 1:
      user.tel = tel
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o email, tente outros.","success")
      return redirect(url_for('moto.update'))
  
    elif User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 1 and Motorista.query.filter_by(cnh = cnh).count() == 0:
      moto.cnh = cnh
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar o e-mail e o telefone, tente outros.","success")
      return redirect(url_for('moto.update'))

    elif User.query.filter_by(email = email).count() == 1:
      moto.cnh = cnh
      user.tel = tel
      db.session.commit()    
      flash("Dados atualizados com sucesso! Se deseja alterar o e-mail, tente outro.","success")
      return redirect(url_for('moto.update'))

    elif User.query.filter_by(tel = tel).count() == 1:
      user.email = email
      moto.cnh = cnh
      db.session.commit()    
      flash("Dados atualizados com sucesso! Se deseja alterar o telefone, tente outro.","success")
      return redirect(url_for('moto.update'))

    elif Motorista.query.filter_by(cnh = cnh).count() == 1:
      user.email = email
      user.tel = tel
      db.session.commit()    
      flash("Dados atualizados com sucesso! Se deseja alterar a cnh, tente outra.","success")
      return redirect(url_for('moto.update'))

    else:
      moto.cnh = cnh
      user.email = email
      user.tel = tel
      db.session.commit()    
      flash("Dados atualizados com sucesso!","success")
      return redirect(url_for('moto.update'))

# EDITAR - VEÍCULO
@bp_moto.route('/perfil/editar-veiculo', methods=['GET','POST'])
@login_required
def update_ve():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect(url_for('/administrador/perfil'))

    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/passageiro/perfil')
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1: 
        ve = Veiculo.query.filter_by(id_moto = current_user.id).first()
        return render_template('moto/update_ve.html', ve=ve)

  elif request.method == 'POST':
    placa = request.form.get('placa')
    renavam = request.form.get('renavam')
    modelo = request.form.get('modelo')  
    cor = request.form.get('cor')  
    marca = request.form.get('marca')
    ano = request.form.get('ano')
    
    ve = Veiculo.query.filter_by(id_moto = current_user.id).first()
    ve.modelo = modelo
    ve.cor = cor
    ve.marca = marca
    ve.ano = ano

    if Veiculo.query.filter_by(placa = placa).count() == 1 and Veiculo.query.filter_by(renavam = renavam).count() == 1:
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar a cnh, o e-mail e o telefone, tente outros.","success")
      return redirect(url_for('moto.update_ve'))
            
    elif Veiculo.query.filter_by(placa = placa).count() == 1 and Veiculo.query.filter_by(renavam = renavam).count() == 0:
      ve.renavam = renavam
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o telefone, tente outros." ,"success")
      return redirect(url_for('moto.update_ve'))
        
    elif Veiculo.query.filter_by(placa = placa).count() == 0 and Veiculo.query.filter_by(renavam = renavam).count() == 1:
      ve.placa = placa
      db.session.commit()
      flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o email, tente outros.","success")
      return redirect(url_for('moto.update_ve'))

    else:
      ve.placa = placa
      ve.renavam = renavam 
      db.session.commit()    
      flash("Dados atualizados com sucesso!","success")
      return redirect(url_for('moto.update_ve'))

# ALTERAR SENHA
@bp_moto.route('/perfil/alterar-senha', methods=['GET','POST'])
@login_required
def update_senha():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect('/administrador/perfil')
      
    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/passageiro/perfil')
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        return render_template('moto/update_senha.html')

  elif request.method == 'POST':
    senha = request.form.get('senha')
    csenha = request.form.get('csenha')
    
    if senha != csenha:
      flash('Senhas diferentes!', 'warning')
      return redirect('/motorista/perfil/alterar-senha')
  
    else:
      user = User.query.filter_by(id = current_user.id).first()
      user.senha = hashlib.md5(request.form.get('senha').encode()).hexdigest()
      db.session.commit()
      logout_user()
      flash('Senha atualizada com sucesso!', 'success')
      return redirect('/login')

# DELETAR
@bp_moto.route('/perfil/desativar', methods=['GET','POST'])
@login_required
def delete():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect('/administrador/perfil')
      
    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/passageiro/perfil')
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        return render_template('moto/delete.html')

  elif request.method == 'POST':
    user = User.query.filter_by(id = current_user.id).first()
    user.status = 0
    db.session.commit()
    
    logout_user()
    flash('Desativamos o seu cadastro. Esperamos revê-lo em breve!', "success")
    return redirect('/')