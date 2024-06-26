# Generated by Django 5.0.2 on 2024-04-03 01:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GdsSystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='criado_em',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='competicao',
            field=models.CharField(choices=[(None, ''), ('lideres', 'Líderes de placar ou tabelas de classificação'), ('desafios', 'Desafios cronometrados que testam a velocidade'), ('missoes', 'Missões ou tarefas especiais pontuam')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='detalhe',
            field=models.CharField(choices=[(None, ''), ('cibernetico', 'Possuem implantes cibernéticos avançados'), ('genetico', 'Possui um código genético exclusivo'), ('especies', 'Podem pertencer a diferentes raças ou espécies alienígenas')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='disciplina',
            field=models.CharField(choices=[(None, ''), ('fisica', 'Fisica'), ('quimica', 'Quimica'), ('matematica', 'Matematica')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='estilo',
            field=models.CharField(choices=[(None, ''), ('visual', 'Visual'), ('auditivo', 'Auditivo'), ('cinestesico', 'Cinestesico'), ('leitura_escrita', 'Leitura e Escrita')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='habilidade',
            field=models.CharField(choices=[(None, ''), ('criatividade', 'Criatividade'), ('lideranca', 'Liderança'), ('colaboracao', 'Colaboração'), ('resiliencia', 'Resiliência')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='historia',
            field=models.CharField(choices=[(None, ''), ('voluntarios', 'Voluntários em um programa de exploração'), ('recrutados', 'Recrutados para participar de uma resistência'), ('cientistas', 'Ciêntistas que foram enviados para estudar')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='interesse',
            field=models.CharField(choices=[(None, ''), ('tecnologia', 'Tecnologia'), ('arte_cultura', 'Arte E Cultura'), ('ciencia', 'Ciência'), ('esporte', 'Esporte e Atividades'), ('fisica', 'Fisica')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='limitacao',
            field=models.CharField(choices=[(None, ''), ('restricao', 'Restrição de tempo para implementar a gamificação durante as aulas'), ('limitacao', 'Limitações de acesso à internet ou dispositivos eletrônicos na sala de aula'), ('disponibilidade', 'Disponibilidade limitada de recursos financeiros')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='problema',
            field=models.CharField(choices=[(None, ''), ('virus', 'Vírus Tecnológico'), ('corporacoes', 'Corporações Dominam'), ('inteligencia', 'Inteligência Artificial'), ('autonoma', 'Autonoma'), ('escassez', 'Escassez de Recursos'), ('naturais', 'Naturais')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='recompensa',
            field=models.CharField(choices=[(None, ''), ('moedas_pontos', 'Moedas ou pontos'), ('avatares', 'Avatares personalizáveis'), ('niveis', 'Níveis ou rankings')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='recurso',
            field=models.CharField(choices=[(None, ''), ('quadro', 'Quadro'), ('laboratorio', 'Laboratório de informática'), ('biblioteca', 'Biblioteca'), ('quadra', 'Quadra poliesportiva')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='regra',
            field=models.CharField(choices=[(None, ''), ('viagem', 'Viagem no Tempo Proibida'), ('biotecnologia', 'Biotecnologia'), ('clones', 'Clones Humanos'), ('leis', 'Leis da robótica'), ('exploracao', 'Exploração de IA')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='serie',
            field=models.CharField(choices=[(None, ''), ('serie_1', '1º Série'), ('serie_2', '2º Série'), ('serie_3', '3º Série'), ('serie_4', '4º Série'), ('serie_5', '5º Série'), ('serie_6', '6º Série'), ('serie_7', '7º Série'), ('serie_8', '8º Série'), ('serie_9', '9º Série'), ('ano_1', '1º Ano'), ('ano_2', '2º Ano'), ('ano_3', '3º Ano')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tema',
            field=models.CharField(choices=[(None, ''), ('mediavel', 'Medieval'), ('floresta', 'Floresta Magica'), ('reino', 'Reino Encantado'), ('futurista', 'Futurista'), ('corrida', 'Corrida')], max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='vilao',
            field=models.CharField(choices=[(None, ''), ('militar', 'Ex-militar Ciberneticamente'), ('ia', 'Superinteligência Artificial'), ('magnata', 'Magnata Corporativo Corrupto')], max_length=255),
        ),
    ]
