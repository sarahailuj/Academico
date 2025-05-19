from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupacao")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"   
        verbose_name_plural = "Cidades"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(verbose_name="Pai")
    mae = models.CharField(verbose_name="Mãe")
    cpf = models.CharField(verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(verbose_name="Email")
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade")
    Ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE,verbose_name="Ocupacao")
    def __str__(self):
        return f"{self.nome}, {self.pai}, {self.mae}, {self.cpf}, {self.data_nasc}, {self.email}, {self.cidade}, {self.ocupacao}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituicao de Ensino")
    site = models.CharField(verbose_name="Site")
    telefone = models.CharField(verbose_name="Telefone")
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "InstituicaoEnsino"
        verbose_name_plural = "InstituicaoEnsinos"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "AreaSaber"
        verbose_name_plural = "AreaSaberes"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária")
    duracao_meses = models.IntegerField(verbose_name="Telefone")
    AreaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE,verbose_name="AreaSaber")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    AreaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE,verbose_name="AreaSaber")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    InstituicaoEnsino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE,verbose_name="InstituicaoEnsino")
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_previsao_termino = models.DateField(verbose_name="Previsao de termino")
    def __str__(self):
        return f"{self.Pessoa}, {self.Curso}"
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "AvaliacaoTipo"
        verbose_name_plural = "AvaliacaoTipos"

class Avaliacao(models.Model):
    descricao = models.CharField(verbose_name="Descricao")
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Dsciplina")
    AvaliacaoTipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE,verbose_name="AvaliacaoTipo")
    def __str__(self):
        return f"{self.descricao}"
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"

class Frequencia(models.Model):
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Dsciplina")
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Numero de Faltas")
    def __str__(self):
        return f"{self.numero_faltas}"
    class Meta:
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencias"

class Turnos(models.Model):
    nome = models.CharField(verbose_name="Nome do Turno")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class Ocorrencia(models.Model):
    descricao = models.CharField(verbose_name="Descricao")
    data = models.DateField(verbose_name="Data")
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Dsciplina")
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="Pessoa")
    def __str__(self):
        return f"{self.descricao}"
    class Meta:
        verbose_name = "Ocorrencia"
        verbose_name_plural = "Ocorrencias"

class CursoDisciplina(models.Model):
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Dsciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga Horaria")
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    # Periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE,verbose_name="Periodo")
    def __str__(self):
        return f"{self.Disciplina}"
    class Meta:
        verbose_name = "CursoDisciplina"
        verbose_name_plural = "CursoDisciplinas"



