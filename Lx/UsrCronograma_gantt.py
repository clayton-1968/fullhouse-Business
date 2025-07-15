import plotly.figure_factory as ff
import plotly.graph_objects  as go
import webbrowser

import http.server
import socketserver
import threading
import pandas       as pd

from datetime       import datetime, timedelta
from imports        import *
from plotly.offline import plot

# Função para criar dados de exemplo
def create_sample_data():
    sql_query = """
                    SELECT 
                        pc.projeto_empresa          AS projeto_empresa,
                        pa.projeto_ID               AS projeto_ID, 
                        pa.projeto_DS               AS projeto_DS, 
                        pa.tarefa_ID                AS tarefa_ID, 
                        pa.tarefa_DS                AS tarefa_DS, 
                        pa.parent_id                AS parent_id,
                        pa.responsavel_nome         AS responsavel_nome,
                        pa.tarefa_dependencia       AS tarefa_dependencia, 
                        pa.tempo_espera             AS tempo_espera, 
                        pa.tempo_previsto           AS tempo_previsto, 
                        pa.percentual_execucao      AS percentual_execucao,
                        pa.data_Inicial_Prevista    AS data_Inicial_Prevista, 
                        pa.data_Inicial_Realizada   AS data_Inicial_Realizada, 
                        pa.dias_diferenca_inicio    AS dias_diferenca_inicio,
                        pa.data_conclusao_prevista  AS data_conclusao_prevista, 
                        pa.data_conclusao_realizada AS data_conclusao_realizada, 
                        pa.prazo_fatal_dias         AS prazo_fatal_dias,
                        pa.dias_diferenca           AS dias_diferenca, 
                        pa.status                   AS status, 
                        pa.observacao               AS observacao
                    FROM programas_atividades pa
                    INNER JOIN projetos_cronograma pc ON pc.projeto_id=pa.projeto_id 
                    WHERE pa.projeto_ID = %s
                    ORDER BY tarefa_ID
                """

    list_tarefas = []
    list_tarefas = db.executar_consulta(sql_query, projeto_id)
    
    today = datetime.now().date()
    tasks = [
        dict(Task="Tarefa 1", Start=today, Finish=today + timedelta(days=5), Complete=100),
        dict(Task="Tarefa 2", Start=today + timedelta(days=3), Finish=today + timedelta(days=8), Complete=80),
        dict(Task="Tarefa 3", Start=today + timedelta(days=6), Finish=today + timedelta(days=12), Complete=50),
        dict(Task="Tarefa 4", Start=today + timedelta(days=9), Finish=today + timedelta(days=15), Complete=20),
        dict(Task="Tarefa 5", Start=today + timedelta(days=12), Finish=today + timedelta(days=18), Complete=0)
    ]
    return pd.DataFrame(tasks)

# Criar dados de exemplo
df = create_sample_data()

# Criar o gráfico de Gantt
fig = ff.create_gantt(df, index_col='Task', show_colorbar=True, group_tasks=True)

# Adicionar barras para o progresso realizado
for task in df.itertuples():
    if task.Complete > 0:
        start = task.Start
        duration = (task.Finish - task.Start).days
        completed_duration = duration * task.Complete / 100
        color = 'green' if task.Complete == 100 else 'red' if task.Complete < (datetime.now().date() - task.Start).days / duration * 100 else 'green'
        
        fig.add_trace(go.Bar(
            x=[start + timedelta(days=completed_duration)],
            y=[task.Task],
            orientation='h',
            marker=dict(color=color),
            width=0.5,
            base=start,
            hoverinfo='none',
            showlegend=False
        ))

# Atualizar o layout
fig.update_layout(
    title='Gráfico de Gantt-----',
    xaxis_title='Data',
    yaxis_title='Tarefas',
    height=400,
    margin=dict(l=150, r=50, t=50, b=50),
    xaxis=dict(
        tickformat='%d-%m-%Y',
        tickangle=45,
    )
)

# Atualizar as cores das barras
fig.data[0].marker.color = 'rgb(0, 0, 255)'  # Azul para previsto

# Adicionar legenda
fig.add_trace(go.Bar(x=[None], y=[None], name='Previsto', marker_color='blue'))
fig.add_trace(go.Bar(x=[None], y=[None], name='Realizado', marker_color='green'))
fig.add_trace(go.Bar(x=[None], y=[None], name='Atrasado', marker_color='red'))

# Mostrar o gráfico
# fig.show()
plot(fig, auto_open=True)

# Gerar o arquivo HTML
plot(fig, filename='gantt_chart.html', auto_open=False)

# Configurar e iniciar o servidor
PORT = 9000
Handler = http.server.SimpleHTTPRequestHandler

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

# Iniciar o servidor em uma thread separada
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Abrir o navegador
webbrowser.open(f'http://localhost:{PORT}/gantt_chart.html')

# Manter o script rodando
input("Pressione Enter para encerrar o servidor...")
