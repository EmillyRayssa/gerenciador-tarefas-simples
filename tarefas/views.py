from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Tarefa


class TarefaLista(LoginRequiredMixin, ListView):
    template_name = 'tarefas/lista.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user).order_by('concluida', '-criada_em')


class TarefaCriar(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao']
    template_name = 'tarefas/form.html'
    success_url = reverse_lazy('lista')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class TarefaEditar(LoginRequiredMixin, UpdateView):
    fields = ['titulo', 'descricao', 'concluida']
    template_name = 'tarefas/form.html'
    success_url = reverse_lazy('lista')

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)


class TarefaExcluir(LoginRequiredMixin, DeleteView):
    template_name = 'tarefas/confirmar_exclusao.html'
    success_url = reverse_lazy('lista')

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)


class Cadastro(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/cadastro.html'
    success_url = reverse_lazy('login')