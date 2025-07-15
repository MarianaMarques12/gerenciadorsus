from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class GrupoRisco(models.Model):
    nome = models.CharField(max_length=100)  # Ex: Idoso, Criança, Doença Crônica

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    grupo_risco = models.ForeignKey(GrupoRisco, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class UnidadeSaude(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Especialidade(models.Model):
    nome = models.CharField(max_length=150)  # Ex: Clínica Geral, Pediatria, Cardiologia

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=150)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    unidade_saude = models.ForeignKey(UnidadeSaude, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.crm})"

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('AG', 'Agendado'),
        ('CO', 'Confirmado'),
        ('CA', 'Cancelado'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AG')

    def __str__(self):
        return f"Agendamento: {self.paciente} com {self.medico} em {self.data_hora}"

class Triagem(models.Model):
    PRIORIDADE_CHOICES = [
        ('BA', 'Baixa'),
        ('ME', 'Média'),
        ('AL', 'Alta'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    sintomas = models.TextField()
    prioridade = models.CharField(max_length=2, choices=PRIORIDADE_CHOICES)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Triagem {self.paciente} em {self.data}"

class ExameProcedimento(models.Model):
    nome = models.CharField(max_length=150)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class AgendamentoExame(models.Model):
    STATUS_CHOICES = [
        ('AG', 'Agendado'),
        ('CO', 'Confirmado'),
        ('CA', 'Cancelado'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    exame_procedimento = models.ForeignKey(ExameProcedimento, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AG')

    def __str__(self):
        return f"Exame: {self.paciente} - {self.exame_procedimento} em {self.data_hora}"

class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    diagnostico = models.TextField()
    prescricao = models.TextField()

    def __str__(self):
        return f"Atendimento: {self.paciente} com {self.medico} em {self.data_hora}"

class OcorrenciaPaciente(models.Model):
    TIPO_CHOICES = [
        ('AT', 'Atraso'),
        ('FA', 'Faltou'),
        ('RE', 'Reclamou'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField()
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)

    def __str__(self):
        return f"Ocorrência {self.tipo} - {self.paciente} em {self.data}"

class Notificacao(models.Model):
    STATUS_LEITURA_CHOICES = [
        ('NL', 'Não Lida'),
        ('LI', 'Lida'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    status_leitura = models.CharField(max_length=2, choices=STATUS_LEITURA_CHOICES, default='NL')

    def __str__(self):
        return f"Notificação para {self.paciente} em {self.data_envio}"
