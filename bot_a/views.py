from django.shortcuts import render
from django.http import HttpResponse
import bot
import subprocess
import os


def bot_a(request):
    current_directory = os.getcwd()
    desired_path = os.path.join(current_directory, 'venv', 'Scripts', 'python.exe')
    bot_path = os.path.join(current_directory, 'bot', 'bot_alive', 'bot_alive', 'bot.py')
    try:
        # Executa o script usando o comando 'python'
        resultado = subprocess.run([desired_path, bot_path ])
        

        # Decodifica a saída do subprocesso para uma string legível
        resultado_str = resultado

        return HttpResponse(f'Resultado: {resultado_str}')
    except Exception as e:
        return HttpResponse(f'Ocorreu um erro: {e}')


