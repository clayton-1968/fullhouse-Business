import wget
import os
import sys
import win32com.client


link = 'https://srv-web-full-gestor.eastus2.cloudapp.azure.com/download'
diretorio = r'C:\FullBusiness'
file_path = os.path.join(diretorio, 'fullbusiness.exe')

# Verifica se o diretório existe e cria se não existir
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Faz o download
wget.download(link, file_path)

# Caminho do arquivo ou aplicativo que você deseja criar um atalho
target_path = r'C:\FullBusiness\fullbusiness.exe'  

# Localização da área de trabalho
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Nome do atalho
shortcut_name = 'FullBusiness.lnk'
shortcut_path = os.path.join(desktop, shortcut_name)

# Verifica se o atalho já existe e o remove, se necessário
if os.path.exists(shortcut_path):
    try:
        os.remove(shortcut_path)
        print(f'Atalho existente removido: {shortcut_path}')
    except Exception as e:
        print(f'Erro ao remover atalho existente: {e}')

# Criação do atalho
try:
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.IconLocation = target_path  # Defina um ícone, se desejar
    # shortcut.save()
    # print(f'Atalho criado na área de trabalho: {shortcut_path}')
except Exception as e:
    print(f'Erro ao criar atalho: {e}')