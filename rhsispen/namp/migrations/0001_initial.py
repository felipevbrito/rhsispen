# Generated by Django 3.2 on 2021-05-28 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Afastamento',
            fields=[
                ('id_afastamento', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_afastamento', models.CharField(max_length=10, verbose_name='Código')),
                ('tipificacao', models.CharField(max_length=100, unique=True, verbose_name='Tipo de afastamento')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Afastamento',
                'verbose_name_plural': 'Tipos de Afastamento',
                'ordering': ['id_afastamento'],
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id_equipe', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False, verbose_name='Equipe Ativa')),
                ('hora_inicial', models.TimeField()),
                ('categoria', models.CharField(choices=[('Plantão', 'Plantão'), ('Expediente', 'Expediente')], max_length=10, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id_funcao', models.AutoField(primary_key=True, serialize=False)),
                ('simbolo', models.CharField(max_length=25, verbose_name='Símbolo')),
                ('nome', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Função',
                'verbose_name_plural': 'Tipos de Funções',
                'ordering': ['simbolo'],
                'unique_together': {('nome',)},
            },
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id_regiao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Região',
                'verbose_name_plural': 'Regiões',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='StatusFuncional',
            fields=[
                ('id_status_funcional', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Status Funcional',
                'verbose_name_plural': 'Tipos de Status Funcional',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='TipoJornada',
            fields=[
                ('id_tipo_jornada', models.AutoField(primary_key=True, serialize=False)),
                ('carga_horaria', models.PositiveIntegerField()),
                ('tipificacao', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Jornada',
                'verbose_name_plural': 'Tipos de Jornadas',
                'ordering': ['tipificacao'],
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id_setor', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Código')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=False, verbose_name='Setor Ativo')),
                ('setor_sede', models.BooleanField(default=False)),
                ('fk_regiao', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.regiao', verbose_name='Região')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
                'ordering': ['nome'],
                'unique_together': {('id_setor', 'nome', 'fk_regiao')},
            },
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id_matricula', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Matrícula')),
                ('vinculo', models.CharField(max_length=2, verbose_name='Vínculo')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('dt_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('cargo', models.CharField(choices=[('Agente de Execução Penal', 'Agente de Execução Penal'), ('Agente Analista em Execução Penal', 'Agente Analista em Execução Penal'), ('Assistente Administrativo', 'Assistente Administrativo'), ('Auxiliar Administrativo', 'Auxiliar Administrativo'), ('Auxiliar de Serviços Gerais', 'Auxiliar de Serviços Gerais'), ('Agente de Segurança Socioeducativo', 'Agente de Segurança Socioeducativo'), ('Agente Especialista Socioeducativo', 'Agente Especialista Socioeducativo')], max_length=50)),
                ('cf', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('Nenhum', 'Nenhum')], max_length=10, verbose_name='Curso de Formação')),
                ('tipo_vinculo', models.CharField(choices=[('Contrato', 'Contrato'), ('Concursado', 'Concursado'), ('Estágio', 'Estágio'), ('Jovem Aprendiz', 'Jovem Aprendiz'), ('Terceirizado', 'Terceirizado')], max_length=25, verbose_name='Tipo de Vínculo')),
                ('regime_juridico', models.CharField(choices=[('CLT', 'CLT'), ('Estatutário', 'Estatutário')], max_length=25, verbose_name='Regime Jurídico')),
                ('situacao', models.BooleanField(default=False, verbose_name='Servidor Ativo')),
                ('fk_equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.equipe', verbose_name='Equipe')),
                ('fk_setor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.setor', verbose_name='Setor')),
                ('fk_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
                'ordering': ['nome'],
                'unique_together': {('id_matricula', 'vinculo', 'cpf')},
            },
        ),
        migrations.CreateModel(
            name='HistStatusFuncional',
            fields=[
                ('id_hist_funcional', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
                ('fk_status_funcional', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.statusfuncional', verbose_name='Status Funcional')),
            ],
            options={
                'verbose_name': 'Status Funcional',
                'verbose_name_plural': 'Status Funcional',
            },
        ),
        migrations.CreateModel(
            name='HistLotacao',
            fields=[
                ('id_hist_lotacao', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField(blank=True, null=True)),
                ('fk_equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.equipe', verbose_name='Equipe')),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
                ('fk_setor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Lotação',
                'verbose_name_plural': 'Lotações',
            },
        ),
        migrations.CreateModel(
            name='HistFuncao',
            fields=[
                ('id_hist_funcao', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField(blank=True, null=True)),
                ('fk_funcao', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.funcao', verbose_name='Função')),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
            ],
            options={
                'verbose_name': 'Função',
                'verbose_name_plural': 'Funções',
            },
        ),
        migrations.CreateModel(
            name='HistAfastamento',
            fields=[
                ('id_hist_afastamento', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
                ('fk_afastamento', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.afastamento', verbose_name='Afastamento')),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
            ],
            options={
                'verbose_name': 'Afastamento',
                'verbose_name_plural': 'Afastamentos',
            },
        ),
        migrations.AddField(
            model_name='equipe',
            name='fk_setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.setor', verbose_name='Setor'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='fk_tipo_jornada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.tipojornada', verbose_name='Tipo de Jornada'),
        ),
        migrations.CreateModel(
            name='EnderecoSetor',
            fields=[
                ('id_endereco_setor', models.AutoField(primary_key=True, serialize=False)),
                ('uf', models.CharField(default='TO', max_length=2)),
                ('cep', models.CharField(blank=True, default='77000000', max_length=8)),
                ('municipio', models.CharField(default='Não registrado', max_length=100)),
                ('endereco', models.CharField(default='Não registrado', max_length=100)),
                ('numero', models.CharField(blank=True, max_length=10)),
                ('bairro', models.CharField(blank=True, max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('fk_setor', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='namp.setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Endereço do Setor',
                'verbose_name_plural': 'Enderecos dos Setores',
                'ordering': ['uf', 'municipio', 'endereco'],
            },
        ),
        migrations.CreateModel(
            name='EnderecoServ',
            fields=[
                ('id_endereco_serv', models.AutoField(primary_key=True, serialize=False)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('municipio', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('fk_servidor', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
            ],
            options={
                'verbose_name': 'Endereço do Servidor',
                'verbose_name_plural': 'Endereço do Servidor',
                'ordering': ['uf', 'municipio', 'endereco'],
            },
        ),
        migrations.CreateModel(
            name='ContatoServ',
            fields=[
                ('id_contato_serv', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_contato', models.CharField(choices=[('Telefone Celular', 'Telefone Celular'), ('Telefone Fixo', 'Telefone Fixo'), ('E-mail', 'E-mail')], max_length=100, verbose_name='Tipo de contato')),
                ('contato', models.CharField(max_length=100)),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
            ],
            options={
                'verbose_name': 'Contato do Servidor',
                'verbose_name_plural': 'Contatos de Servidor',
            },
        ),
        migrations.CreateModel(
            name='ContatoEquipe',
            fields=[
                ('id_contato_equipe', models.AutoField(primary_key=True, serialize=False)),
                ('tipificacao', models.CharField(choices=[('Telefone Celular', 'Telefone Celular'), ('Telefone Fixo', 'Telefone Fixo'), ('E-mail', 'E-mail')], max_length=50, verbose_name='Tipo de contato')),
                ('contato', models.CharField(max_length=50)),
                ('fk_equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.equipe', verbose_name='Equipe')),
            ],
            options={
                'verbose_name': 'Contato da Equipe',
                'verbose_name_plural': 'Contatos da Equipe',
            },
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id_jornada', models.AutoField(primary_key=True, serialize=False)),
                ('data_jornada', models.DateField()),
                ('assiduidade', models.BooleanField(default=False)),
                ('fk_afastamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='namp.afastamento', verbose_name='Motivo da Ausência')),
                ('fk_equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.equipe', verbose_name='Equipe')),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
                ('fk_tipo_jornada', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.tipojornada', verbose_name='Tipo Jornada')),
            ],
            options={
                'verbose_name': 'Jornada',
                'verbose_name_plural': 'Jornadas',
                'ordering': ['fk_equipe__fk_setor__nome', 'fk_equipe__nome', 'fk_servidor__nome', 'data_jornada'],
                'unique_together': {('fk_servidor', 'data_jornada')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='equipe',
            unique_together={('nome', 'fk_setor')},
        ),
    ]
