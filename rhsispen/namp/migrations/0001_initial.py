# Generated by Django 3.2 on 2021-04-17 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afastamento',
            fields=[
                ('id_afastamento', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='Código')),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name='Tipo de afastamento')),
                ('descricao', models.TextField(blank=True, max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Afastamento',
                'verbose_name_plural': 'Afastamentos',
                'ordering': ['tipificacao'],
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
                ('id_funcao', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Função',
                'verbose_name_plural': 'Funções',
                'ordering': ['nome'],
                'unique_together': {('id_funcao', 'nome')},
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
                'verbose_name': 'Status Funcional',
                'verbose_name_plural': 'Status Funcionais',
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
                ('cargo', models.CharField(choices=[('AEP', 'Agente de Execução Penal'), ('AAE', 'Agente Analista em Execução Penal'), ('AA', 'Assistente Administrativo'), ('AXA', 'Auxiliar Administrativo'), ('ASG', 'Auxiliar de Serviços Gerais'), ('ASS', 'Agente de Segurança Socioeducativo'), ('AES', 'Agente Especialista Socioeducativo')], max_length=50)),
                ('tipo_vinculo', models.CharField(choices=[('Contrato', 'Contrato'), ('Concursado', 'Concursado'), ('Estágio', 'Estágio'), ('Jovem Aprendiz', 'Jovem Aprendiz'), ('Terceirizado', 'Terceirizado')], max_length=25, verbose_name='Tipo de Vínculo')),
                ('regime_juridico', models.CharField(choices=[('C', 'CLT'), ('E', 'Estatutário')], max_length=25, verbose_name='Regime Jurídico')),
                ('situacao', models.BooleanField(default=False, verbose_name='Servidor Ativo')),
                ('fk_equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.equipe', verbose_name='Equipe')),
                ('fk_setor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
                'ordering': ['nome'],
                'unique_together': {('id_matricula', 'vinculo', 'cpf')},
            },
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id_jornada', models.AutoField(primary_key=True, serialize=False)),
                ('data_jornada', models.DateField()),
                ('assiduidade', models.BooleanField(default=False)),
                ('fk_equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.equipe', verbose_name='Equipe')),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
                ('fk_tipo_jornada', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.tipojornada', verbose_name='Tipo Jornada')),
            ],
            options={
                'verbose_name': 'Jornada',
                'verbose_name_plural': 'Jornadas',
                'ordering': ['data_jornada'],
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
                'verbose_name': 'Histórico de Status Funcional',
                'verbose_name_plural': 'Histórico de Status Funcionais',
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
                ('fk_setor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.setor', verbose_name='Sertor')),
            ],
            options={
                'verbose_name': 'Histórico de Lotação',
                'verbose_name_plural': 'Históricos de Lotações',
            },
        ),
        migrations.CreateModel(
            name='HistFuncao',
            fields=[
                ('id_hist_funcao', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('fk_funcao', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.funcao', verbose_name='Função')),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.servidor', verbose_name='Servidor')),
            ],
            options={
                'verbose_name': 'Histórico de Função',
                'verbose_name_plural': 'Históricos de Funcões',
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
                'verbose_name': 'Histório de Afastamento',
                'verbose_name_plural': 'Históricos de Afastamentos',
            },
        ),
        migrations.AddField(
            model_name='equipe',
            name='fk_setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.setor', verbose_name='Setor'),
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
        migrations.AlterUniqueTogether(
            name='equipe',
            unique_together={('nome', 'fk_setor')},
        ),
    ]
