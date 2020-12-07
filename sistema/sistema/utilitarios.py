from django.contrib.auth.mixins import LoginRequiredMixin

class AutenticacaoObrigatoria(LoginRequiredMixin):
    """
    Mixin para limitar acesso (apenas usuários autenticados)
    """
    login_url = '/'