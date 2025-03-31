import requests
import subprocess

def download_file(url, local_filename):
    response = requests.get(url, stream=True)  # 'stream=True' para download em partes

    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f'Download concluído: {local_filename}')
    else:
        print(f'Falha no download. Status code: {response.status_code}')

# Processo de atualização
# Comando para encerrar o processo

process_name = "main.exe"
subprocess.run(["taskkill", "/F", "/IM", process_name])


url = 'https://srv-web-full-gestor.eastus2.cloudapp.azure.com/download/main.exe'  # Substitua pela sua URL
local_filename = r'C:\FullBusiness\main.exe'
download_file(url, local_filename)

caminho_exec = r"C:\FullBusiness\main.exe"  # Caminho para o executável
subprocess.Popen(caminho_exec)  # Inicia o executável

