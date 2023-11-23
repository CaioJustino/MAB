# IMPORTS
from flask import render_template, request, url_for, redirect, flash, Blueprint
from utils.utils import db
from utils.models import User, Passageiro, Motorista, Veiculo, Viagem, Pagamento
from flask_login import login_required, current_user, logout_user
import hashlib

# CONFIGS
bp_adm = Blueprint("adm", __name__, template_folder="templates")

# PERFIL
@bp_adm.route('/perfil', methods=['GET'])
@login_required
def perfil():
  if current_user.adm == 1:
    users = User.query.filter_by(adm = 1).order_by(User.id.desc()).all()
    return render_template('adm/perfil.html', users=users)

  else:
    if Passageiro.query.filter_by(id = current_user.id).count() == 1: 
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

# CADASTRO - ADMINISTRADOR
@bp_adm.route('/cadastro', methods=['POST'])
def cadastro():
  nome = request.form.get('nome')
  email = request.form.get('email')
  data_nasc = request.form.get('data_nasc')
  tel = request.form.get('tel')
  senha = request.form.get('senha')
  csenha = request.form.get('csenha')

  if senha != "" and csenha != "" and senha != csenha:
    flash("Senhas diferentes!", "warning")
    return redirect(url_for('adm.perfil'))

  else:
    if ((User.query.filter_by(email = email)) or (User.query.filter_by(tel = tel))).count() == 1:
     flash("Esses dados já foram utilizados! Por favor, tente outros.", "danger")
     return redirect(url_for('adm.perfil'))

    else:
      senha = hashlib.md5(request.form.get('senha').encode()).hexdigest()
      u = User(nome, data_nasc, email, tel, senha, True, True)
      db.session.add(u)
      db.session.commit()

      flash("Cadastro concluído com sucesso!", "success")
      return redirect(url_for('adm.perfil'))

# EDITAR - ADMINISTRADOR
@bp_adm.route('/editar/<int:id>', methods=['POST'])
@login_required
def update_adm(id): 
  nome = request.form.get('nome')
  email = request.form.get('email')
  data_nasc = request.form.get('data_nasc')
  tel = request.form.get('tel')
  status = request.form.get('status')
  
  user = User.query.get(id)
  user.nome = nome
  user.data_nasc = data_nasc
  user.status = bool(status)

  if User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 1:
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar o e-mail e o telefone, tente outros.","success")
    return redirect(url_for('adm.perfil'))
            
  elif User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 0:
    user.tel = tel
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar o e-mail, tente outro." ,"success")
    return redirect(url_for('adm.perfil'))
  
  elif User.query.filter_by(email = email).count() == 0 and User.query.filter_by(tel = tel).count() == 1:
    user.email = email
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar o telefone, tente outro.","success")
    return redirect(url_for('adm.perfil'))

  else:
    user.email = email
    user.tel = tel
    db.session.commit()
    flash("Dados atualizados com sucesso!","success")
    return redirect(url_for('adm.perfil'))

# ALTERAR SENHA
@bp_adm.route('/alterar-senha/<int:id>', methods=['POST'])
@login_required
def update_senha(id):
  senha = request.form.get('senha')
  csenha = request.form.get('csenha')

  if senha != csenha:
    flash('Senhas diferentes!', 'warning')
    return redirect(url_for('adm.perfil'))

  else:
    user = User.query.get(id)
    user.senha = hashlib.md5(request.form.get('senha').encode()).hexdigest()
    db.session.commit()

    if user.id == current_user.id:
      logout_user()
      flash('Senha atualizada com sucesso!', 'success')
      return redirect('/login')

    else:
      flash('Senha atualizada com sucesso!', 'success')
      return redirect(url_for('adm.perfil'))

# LISTAGEM - PASSAGEIROS
@bp_adm.route('/passageiros', methods=['GET'])
@login_required
def recovery_passg():
  if current_user.adm == 1:
    users = User.query.all()
    passgs = Passageiro.query.all()
    return render_template('adm/recovery_passg.html', users=users, passgs=passgs)

  else:
    if Passageiro.query.filter_by(id = current_user.id).count() == 1: 
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')
  
# EDITAR - PASSAGEIROS
@bp_adm.route('/passageiros/editar/<int:id>', methods=['POST'])
@login_required
def update_passg(id): 
  nome = request.form.get('nome')
  email = request.form.get('email')
  data_nasc = request.form.get('data_nasc')
  tel = request.form.get('tel')
  status = request.form.get('status')
  deficiencia = request.form.get('deficiencia')
  
  user = User.query.get(id)
  passg = Passageiro.query.get(id)
  user.nome = nome
  user.data_nasc = data_nasc
  user.status = bool(status)
  passg.deficiencia = deficiencia

  if User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 1:
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar o e-mail e o telefone, tente outros.","success")
    return redirect(url_for('adm.recovery_passg'))
            
  elif User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 0:
    user.tel = tel
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar o e-mail, tente outro." ,"success")
    return redirect(url_for('adm.recovery_passg'))
  
  elif User.query.filter_by(email = email).count() == 0 and User.query.filter_by(tel = tel).count() == 1:
    user.email = email
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar o telefone, tente outro.","success")
    return redirect(url_for('adm.recovery_passg'))

  else:
    user.email = email
    user.tel = tel
    db.session.commit()
    flash("Dados atualizados com sucesso!","success")
    return redirect(url_for('adm.recovery_passg'))

# DELETAR - PASSAGEIROS
@bp_adm.route('/passageiros/desativar/<int:id>', methods=['POST'])
@login_required
def delete_passg(id): 
  user = User.query.get(id)
  user.status = 0
  db.session.commit()

  flash('Cadastro desativado com sucesso!', "success")
  return redirect('/administrador/passageiros')
      
# LISTAGEM - MOTORISTAS
@bp_adm.route('/motoristas', methods=['GET'])
@login_required
def recovery_moto():
  if current_user.adm == 1:
    users = User.query.all()
    moto = Motorista.query.all()
    return render_template('adm/recovery_moto.html', users=users, moto=moto)

  else:
    if Passageiro.query.filter_by(id = current_user.id).count() == 1: 
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

# EDITAR - MOTORISTAS
@bp_adm.route('/motoristas/editar/<int:id>', methods=['POST'])
@login_required
def update_moto(id): 
  nome = request.form.get('nome')
  email = request.form.get('email')
  data_nasc = request.form.get('data_nasc')
  tel = request.form.get('tel')
  status = request.form.get('status')
  cnh = request.form.get('cnh')
  
  user = User.query.get(id)
  moto = Motorista.query.get(id)
  user.nome = nome
  user.data_nasc = data_nasc
  user.status = bool(status)

  if User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 1 and Motorista.query.filter_by(cnh = cnh).count() == 1:
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar a cnh, o e-mail e o telefone, tente outros.","success")
    return redirect(url_for('adm.recovery_moto'))
          
  elif User.query.filter_by(email = email).count() == 0 and User.query.filter_by(tel = tel).count() == 1 and Motorista.query.filter_by(cnh = cnh).count() == 1:
    user.email = email
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o telefone, tente outros." ,"success")
    return redirect(url_for('adm.recovery_moto'))
      
  elif User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 0 and Motorista.query.filter_by(cnh = cnh).count() == 1:
    user.tel = tel
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o email, tente outros.","success")
    return redirect(url_for('adm.recovery_moto'))

  elif User.query.filter_by(email = email).count() == 1 and User.query.filter_by(tel = tel).count() == 1 and Motorista.query.filter_by(cnh = cnh).count() == 0:
    moto.cnh = cnh
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar o e-mail e o telefone, tente outros.","success")
    return redirect(url_for('adm.recovery_moto'))

  elif User.query.filter_by(email = email).count() == 1:
    moto.cnh = cnh
    user.tel = tel
    db.session.commit()    
    flash("Dados atualizados com sucesso! Se deseja alterar o e-mail, tente outro.","success")
    return redirect(url_for('adm.recovery_moto'))

  elif User.query.filter_by(tel = tel).count() == 1:
    user.email = email
    moto.cnh = cnh
    db.session.commit()    
    flash("Dados atualizados com sucesso! Se deseja alterar o telefone, tente outro.","success")
    return redirect(url_for('adm.recovery_moto'))

  elif Motorista.query.filter_by(cnh = cnh).count() == 1:
    user.email = email
    user.tel = tel
    db.session.commit()    
    flash("Dados atualizados com sucesso! Se deseja alterar a cnh, tente outra.","success")
    return redirect(url_for('adm.recovery_moto'))

  else:
    moto.cnh = cnh
    user.email = email
    user.tel = tel
    db.session.commit()    
    flash("Dados atualizados com sucesso!","success")
    return redirect(url_for('adm.recovery_moto'))

# DELETAR - MOTORISTAS
@bp_adm.route('/motoristas/desativar/<int:id>', methods=['POST'])
@login_required
def delete_moto(id): 
  user = User.query.get(id)
  user.status = 0
  db.session.commit()

  flash('Cadastro desativado com sucesso!', "success")
  return redirect('/administrador/motoristas')

# LISTAGEM - VEÍCULOS
@bp_adm.route('/veiculos', methods=['GET'])
@login_required
def recovery_ve():
  if current_user.adm == 1:
    ve = Veiculo.query.all()
    return render_template('adm/recovery_ve.html', ve=ve)

  else:
    if Passageiro.query.filter_by(id = current_user.id).count() == 1: 
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

# EDITAR - VEÍCULOS
@bp_adm.route('/veiculos/editar/<int:id>', methods=['POST'])
@login_required
def update_ve(id):
  placa = request.form.get('placa')
  renavam = request.form.get('renavam')
  modelo = request.form.get('modelo')  
  cor = request.form.get('cor')  
  marca = request.form.get('marca')
  ano = request.form.get('ano')
  
  ve = Veiculo.query.get(id)
  ve.modelo = modelo
  ve.cor = cor
  ve.marca = marca
  ve.ano = ano

  if Veiculo.query.filter_by(placa = placa).count() == 1 and Veiculo.query.filter_by(renavam = renavam).count() == 1:
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar a cnh, o e-mail e o telefone, tente outros.","success")
    return redirect(url_for('adm.recovery_ve'))
          
  elif Veiculo.query.filter_by(placa = placa).count() == 1 and Veiculo.query.filter_by(renavam = renavam).count() == 0:
    ve.renavam = renavam
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o telefone, tente outros." ,"success")
    return redirect(url_for('adm.recovery_ve'))
      
  elif Veiculo.query.filter_by(placa = placa).count() == 0 and Veiculo.query.filter_by(renavam = renavam).count() == 1:
    ve.placa = placa
    db.session.commit()
    flash("Dados atualizados com sucesso! Se deseja alterar a cnh e o email, tente outros.","success")
    return redirect(url_for('adm.recovery_ve'))

  else:
    ve.placa = placa
    ve.renavam = renavam 
    db.session.commit()    
    flash("Dados atualizados com sucesso!","success")
    return redirect(url_for('adm.recovery_ve'))

# LISTAGEM - VIAGENS
@bp_adm.route('/viagens', methods=['GET'])
@login_required
def recovery_vi():
  if current_user.adm == 1:
    vi = Viagem.query.all()
    return render_template('adm/recovery_vi.html', vi=vi)

  else:
    if Passageiro.query.filter_by(id = current_user.id).count() == 1: 
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')