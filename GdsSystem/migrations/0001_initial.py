# Generated by Django 5.0.2 on 2024-04-01 02:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('imagem', models.FileField(upload_to='')),
                ('conteudo', models.CharField(max_length=255)),
                ('grau', models.CharField(choices=[(None, ''), ('medio', 'Ensino Médio'), ('fundamental', 'Ensino Fundamental'), ('superior', 'Ensino Superior'), ('tecnico', 'Ensino Tecnico')], max_length=255)),
                ('serie', models.CharField(max_length=255)),
                ('disciplina', models.CharField(max_length=255)),
                ('estilo', models.CharField(max_length=255)),
                ('interesse', models.CharField(max_length=255)),
                ('habilidade', models.CharField(max_length=255)),
                ('recompensa', models.CharField(max_length=255)),
                ('competicao', models.CharField(max_length=255)),
                ('recurso', models.CharField(max_length=255)),
                ('limitacao', models.CharField(max_length=255)),
                ('tema', models.CharField(max_length=255)),
                ('problema', models.CharField(max_length=255)),
                ('regra', models.CharField(max_length=255)),
                ('detalhe', models.CharField(max_length=255)),
                ('historia', models.CharField(max_length=255)),
                ('vilao', models.CharField(max_length=255)),
                ('enredo', models.CharField(max_length=255)),
                ('emboscada', models.BooleanField()),
                ('feridos', models.BooleanField()),
                ('objetivo', models.CharField(max_length=255)),
                ('falha', models.CharField(max_length=255)),
                ('desafio', models.CharField(max_length=255)),
                ('desafio_para_casa', models.CharField(max_length=255)),
                ('exercicio_em_equipe', models.CharField(max_length=255)),
                ('distintivo', models.CharField(max_length=255)),
                ('insignias', models.CharField(max_length=255)),
                ('item_secreto', models.CharField(max_length=255)),
                ('mecanica', models.CharField(max_length=255)),
                ('periodos', models.CharField(max_length=255)),
                ('problema_final', models.CharField(max_length=255)),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projetos_salvos', models.ManyToManyField(to='GdsSystem.projeto')),
            ],
        ),
    ]
