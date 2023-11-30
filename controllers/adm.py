# IMPORTS
from flask import render_template, request, url_for, redirect, flash, Blueprint
from utils.utils import db
from utils.models import User, Passageiro, Motorista, Veiculo, Viagem, Pagamento
from flask_login import login_required, current_user, logout_user
import hashlib

# CONFIGS
bp_adm = Blueprint("adm", __name__, template_folder="templates")

# PERFIL
@bp_adm.route('/perfil', methods=['GET','POST'])
@login_required
def perfil():
  if current_user.adm == 1:
    if request.form.get('search') != None:
      filter = request.form.get('filter')
      search = request.form.get('search')

      if filter == "id":
        users = User.query.filter_by(adm = 1).filter(User.id.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/perfil.html', users = users, search = search, filter = filter)

      elif filter == "nome":
        users = User.query.filter_by(adm = 1).filter(User.nome.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/perfil.html', users = users, search = search, filter = filter)
      
      elif filter == "email":
        users = User.query.filter_by(adm = 1).filter(User.email.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/perfil.html', users = users, search = search, filter = filter)
      
      elif filter == "tel":
        users = User.query.filter_by(adm = 1).filter(User.tel.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/perfil.html', users = users, search = search, filter = filter)

    else:
      users = User.query.filter_by(adm = 1).order_by(User.nome).all()
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
def update(id): 
  nome = request.form.get('nome')
  email = request.form.get('email')
  data_nasc = request.form.get('data_nasc')
  tel = request.form.get('tel')
  status = request.form.get('status')
  
  user = User.query.get(id)
  user.nome = nome
  user.data_nasc = data_nasc

  if status == "True":
    user.status = 1
  
  else:
    user.status = 0

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
@bp_adm.route('/passageiros', methods=['GET','POST'])
@login_required
def recovery_passg():
  if current_user.adm == 1:
    if request.form.get('search') != None:
      filter = request.form.get('filter')
      search = request.form.get('search')

      if filter == "id":
        passgs = Passageiro.query.all()
        users = User.query.join(Passageiro).filter(User.id.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_passg.html', users = users, passgs = passgs, search = search, filter = filter)

      elif filter == "nome":
        passgs = Passageiro.query.all()
        users = User.query.join(Passageiro).filter(User.nome.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_passg.html', users = users, passgs = passgs, search = search, filter = filter)

      elif filter == "email":
        passgs = Passageiro.query.all()
        users = User.query.join(Passageiro).filter(User.email.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_passg.html', users = users, passgs = passgs, search = search, filter = filter)

      elif filter == "tel":
        passgs = Passageiro.query.all()
        users = User.query.join(Passageiro).filter(User.tel.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_passg.html', users = users, passgs = passgs, search = search, filter = filter)

    else:
      passgs = Passageiro.query.all()
      users = User.query.join(Passageiro).order_by(User.nome).all()
      return render_template('adm/recovery_passg.html', users = users, passgs = passgs)

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
  
  if status == "True":
    user.status = 1
  
  else:
    user.status = 0

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
      
# LISTAGEM - MOTORISTAS
@bp_adm.route('/motoristas', methods=['GET','POST'])
@login_required
def recovery_moto():
  if current_user.adm == 1:
    if request.form.get('search') != None:
      filter = request.form.get('filter')
      search = request.form.get('search')

      if filter == "id":
        motos = Motorista.query.all()
        users = User.query.join(Motorista).filter(User.id.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_moto.html', users = users, motos = motos, search = search, filter = filter)

      elif filter == "nome":
        motos = Motorista.query.all()
        users = User.query.join(Motorista).filter(User.nome.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_moto.html', users = users, motos = motos, search = search, filter = filter)
    
      elif filter == "email":
        motos = Motorista.query.all()
        users = User.query.join(Motorista).filter(User.email.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_moto.html', users = users, motos = motos, search = search, filter = filter)
    
      elif filter == "tel":
        motos = Motorista.query.all()
        users = User.query.join(Motorista).filter(User.tel.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_moto.html', users = users, motos = motos, search = search, filter = filter)
    
      elif filter == "cnh":
        motos = Motorista.query.all()
        users = User.query.join(Motorista).filter(User.cnh.like(f'%{search}%')).order_by(User.nome).all()
        return render_template('adm/recovery_moto.html', users = users, motos = motos, search = search, filter = filter)

    else:
      motos = Motorista.query.all()
      users = User.query.join(Motorista).order_by(User.nome).all()
      return render_template('adm/recovery_moto.html', users = users, motos = motos)

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
  
  if status == "True":
    user.status = 1
  
  else:
    user.status = 0

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

# LISTAGEM - VEÍCULOS
@bp_adm.route('/veiculos', methods=['GET','POST'])
@login_required
def recovery_ve():
  if current_user.adm == 1:
    if request.form.get('search') != None:
      if request.form.get('search') != None:
        filter = request.form.get('filter')
        search = request.form.get('search')

        if filter == "id":
          veiculos = Veiculo.query.filter(Veiculo.id.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)    
        
        elif filter == "id_moto":
          veiculos = Veiculo.query.filter(Veiculo.id_moto.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)

        elif filter == "placa":
          veiculos = Veiculo.query.filter(Veiculo.placa.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)
        
        elif filter == "renavam":
          veiculos = Veiculo.query.filter(Veiculo.renavam.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)
        
        elif filter == "modelo":
          veiculos = Veiculo.query.filter(Veiculo.modelo.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)
        
        elif filter == "marca":
          veiculos = Veiculo.query.filter(Veiculo.marca.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)
        
        elif filter == "ano":
          veiculos = Veiculo.query.filter(Veiculo.ano.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)
    
        elif filter == "cor":
          veiculos = Veiculo.query.filter(Veiculo.cor.like(f'%{search}%')).order_by(Veiculo.id.desc()).all()
          return render_template('adm/recovery_ve.html', veiculos = veiculos, search = search, filter = filter)
    
    else:
      veiculos = Veiculo.query.order_by(Veiculo.id.desc()).all()
      return render_template('adm/recovery_ve.html', veiculos = veiculos)

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

# LISTAGEM - PAGAMENTOS
@bp_adm.route('/pagamentos', methods=['GET','POST'])
@login_required
def recovery_pag():
  if current_user.adm == 1:
    if request.form.get('search') != None:
      if request.form.get('search') != None:
        filter = request.form.get('filter')
        search = request.form.get('search')
        
        if filter == "id":
          pagamentos = Pagamento.query.filter(Pagamento.id.like(f'%{search}%')).order_by(Pagamento.id.desc()).all()
          return render_template('adm/recovery_pag.html', pagamentos = pagamentos, search = search, filter = filter)    
        
        elif filter == "id_pass":
          pagamentos = Pagamento.query.filter(Pagamento.id_pass.like(f'%{search}%')).order_by(Pagamento.id.desc()).all()
          return render_template('adm/recovery_pag.html', pagamentos = pagamentos, search = search, filter = filter)    
        
        elif filter == "tipo":
          pagamentos = Pagamento.query.filter(Pagamento.tipo.like(f'%{search}%')).order_by(Pagamento.id.desc()).all()
          return render_template('adm/recovery_pag.html', pagamentos = pagamentos, search = search, filter = filter)    
        
        elif filter == "valor":
          pagamentos = Pagamento.query.filter(Pagamento.valor.like(f'%{search}%')).order_by(Pagamento.id.desc()).all()
          return render_template('adm/recovery_pag.html', pagamentos = pagamentos, search = search, filter = filter)    
        
    else:
      pagamentos = Pagamento.query.order_by(Pagamento.id.desc()).all()
      return render_template('adm/recovery_pag.html', pagamentos = pagamentos)

  else:
    if Passageiro.query.filter_by(id = current_user.id).count() == 1: 
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

# LISTAGEM - VIAGENS
@bp_adm.route('/viagens', methods=['GET','POST'])
@login_required
def recovery_vi():
  if current_user.adm == 1:
    if request.form.get('search') != None:
      filter = request.form.get('filter')
      search = request.form.get('search')

      if filter == "id":
        viagens = Viagem.query.filter(Viagem.id.like(f'%{search}%')).order_by(Viagem.data_hora).all()
        return render_template('adm/recovery_vi.html', viagens =  viagens, search = search, filter = filter)
      
      elif filter == "id_pass":
        viagens = Viagem.query.filter(Viagem.id_pass.like(f'%{search}%')).order_by(Viagem.data_hora).all()
        return render_template('adm/recovery_vi.html', viagens =  viagens, search = search, filter = filter)
    
      elif filter == "id_moto":
        viagens = Viagem.query.filter(Viagem.id_moto.like(f'%{search}%')).order_by(Viagem.data_hora).all()
        return render_template('adm/recovery_vi.html', viagens =  viagens, search = search, filter = filter)
      
      elif filter == "id_pag":
        viagens = Viagem.query.filter(Viagem.id_pag.like(f'%{search}%')).order_by(Viagem.data_hora).all()
        return render_template('adm/recovery_vi.html', viagens =  viagens, search = search, filter = filter)
      
      elif filter == "id_ve":
        viagens = Viagem.query.filter(Viagem.id_ve.like(f'%{search}%')).order_by(Viagem.data_hora).all()
        return render_template('adm/recovery_vi.html', viagens =  viagens, search = search, filter = filter)
      
      elif filter == "embarque":
        viagens = Viagem.query.filter(Viagem.embarque.like(f'%{search}%')).order_by(Viagem.data_hora).all()
        return render_template('adm/recovery_vi.html', viagens =  viagens, search = search, filter = filter)
      
      elif filter == "desembarque":
        viagens = Viagem.query.filter(Viagem.desembarque.like(f'%{search}%')).order_by(Viagem.data_hora).all()
        return render_template('adm/recovery_vi.html', viagens =  viagens, search = search, filter = filter)
    
    else:
      viagens = Viagem.query.order_by(Viagem.data_hora).all()
      return render_template('adm/recovery_vi.html', viagens = viagens)

  else:
    if Passageiro.query.filter_by(id = current_user.id).count() == 1: 
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')