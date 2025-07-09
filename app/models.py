from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class GrupoRisco(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nasc = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    grupo_risco = models.ForeignKey(GrupoRisco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class UnidadeSaude(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    unidade_saude = models.ForeignKey(UnidadeSaude, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('Agendado', 'Agendado'),
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado')
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Triagem(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    sintomas = models.TextField()
    prioridade = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)

class ExameProcedimento(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class AgendamentoExame(models.Model):
    STATUS_CHOICES = [
        ('Agendado', 'Agendado'),
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado')
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    exame = models.ForeignKey(ExameProcedimento, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    diagnostico = models.TextField()
    prescricao = models.TextField()

class OcorrenciaPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField()
    tipo = models.CharField(max_length=100)

class Notificacao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField()
    status_leitura = models.BooleanField(default=False)
