from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from main.context_global import pic_global
from .models import UserProfile, HappyDay



User = get_user_model()

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None

            if user is not None and user.check_password(password):
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Logado com sucesso!')
                    return redirect('/')
                else:
                    messages.error(request, 'Sua conta está inativa. Entre em contato com o administrador.')
            else:
                messages.error(request, 'Nome de usuário ou senha incorretos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'login.html')



@login_required 
def logout_user(request):
    logout(request)
    messages.success(request, 'Operação realizada com sucesso!')
    return redirect( '/')



@login_required
def profile_user(request):
    if request.method == 'GET':
        return render(request, 'profile.html', pic_global(request))
    else:
        form_type = request.POST.get('form_type')
        if form_type == 'update_email':
            user = request.user
            new_email = request.POST.get('new_email')
            confirm_email = request.POST.get('confirm_email')
            if new_email == confirm_email:
                user.email = new_email
                user.save()
                messages.success(request, 'E-mail atualizado com sucesso!')
            else:
                messages.error(request, 'Os e-mails não correspondem.')

        elif form_type == 'update_password':
            user = request.user
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password:
                if check_password(current_password, user.password):
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Senha atualizada com sucesso!')
                else:
                    messages.error(request, 'Senha atual incorreta.')
            else:
                messages.error(request, 'Erro de dados: as senhas não correspondem.')

        elif form_type == 'update_photo':
            user_profile = UserProfile.objects.get(user=request.user)
            photo = request.FILES.get('update_photo')  # Obtém o arquivo enviado pelo campo de entrada de arquivo
        
            if photo:  # Verifica se um arquivo foi enviado
                user_profile.profile_pic = photo
                user_profile.save()
                messages.success(request, 'Foto atualizado com sucesso!')
    return render(request, 'profile.html', pic_global(request))


def registration(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        if request.user.is_authenticated:
            messages.warning(request, 'Você já está logado!')
            return redirect('/')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm-password')


        new_user = User.objects.filter(username=username)

        if new_user.exists():
            messages.info(request, 'Nome de usuário já existe!')
            return render(request, 'register.html')
        
        if password != confirmPassword:
            messages.info(request, 'As senhas não conferem!')
            return render(request, 'register.html')

        new_user = User.objects.create_user(username=username, email=email, password=password)

        username=username,
        new_user.save()

        # Criação do perfil de usuário
        user_profile = UserProfile(user=new_user)
        user_profile.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('/accounts/login/')


@login_required
def happy_day(request):
    # Verificar se o usuário possui um agendamento existente
    has_agendamento = HappyDay.objects.filter(cliente=request.user).exists()

    # Obter o primeiro agendamento do usuário (se existir)
    agendamento = HappyDay.objects.filter(cliente=request.user).first()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'new_happy':
            user = request.user
            current_password = request.POST.get('password')
            
            # Verificar a senha atual do usuário
            if check_password(current_password, user.password):
                data = request.POST.get('date')
                # Verificar se o agendamento já existe para o usuário
                existing_agendamento = HappyDay.objects.filter(cliente=user).exists()
                if existing_agendamento:
                    messages.error(request, 'Você já possui um agendamento.')
                else:
                    # Criar um novo objeto de agendamento
                    agendamento = HappyDay(cliente=user, data=data)
                    # Salvar o agendamento
                    agendamento.save()
                    messages.success(request, 'Agendamento cadastrado com sucesso!')
                return redirect('/happyday/') 

            else:
                messages.error(request, 'Senha incorreta.')

        elif form_type == 'del_happy':
            usuario = request.user
            agendamento = HappyDay.objects.filter(cliente=usuario).first()

            
            if agendamento:
                messages.success(request, 'Agendamento deletado com sucesso!')
                agendamento.delete()
                
            else:
                messages.error(request, 'Nenhum agendamento encontrado para deletar.')
            return redirect('/happyday/') 

    # Renderizar o template 'happyday.html' com as variáveis 'has_agendamento' e 'agendamento'
    return render(request, 'happyday.html', {'has_agendamento': has_agendamento, 'agendamento': agendamento})










