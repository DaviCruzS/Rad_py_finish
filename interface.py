import tkinter as tk
from tkinter import ttk 
from tkcalendar import Calendar, DateEntry
import main 
from datetime import datetime
class PrincipalBD():
    def __init__(self, win):
        self.objBD = main.Missao()
        self.janela = win
        self.frame_esquerda_cima = tk.Frame(self.janela, width=110,padx=5)
        self.frame_esquerda_cima.grid(row=0,column=0,pady=10,padx=5)
        self.frame_esquerda_baixo = tk.Frame(self.janela, width=110,padx=5)
        self.frame_esquerda_baixo.grid(row=1,column=0,)
        self.frame_direita = tk.Frame(self.janela, width=350,padx=5)
        self.frame_direita.grid(row=0,column=1,rowspan=2,pady=10,padx=5)

        self.treeMissoes = ttk.Treeview(self.frame_direita, columns=("id","nomemissao", "lancamento","destino"), show="headings")
        self.treeMissoes.heading("id", text="Localizador")
        self.treeMissoes.heading("nomemissao", text="Nome da Missão")
        self.treeMissoes.heading("lancamento",text= "Lançamento")
        self.treeMissoes.heading("destino",text= "Destino")
        self.treeMissoes.grid(row=0, column=0)

        self.ExibirTela()

        self.textoCadastro = tk.Label(self.frame_esquerda_cima, text='Cadastrar Viagem',bg="#4169E1",relief="flat", anchor="n")
        self.textoCadastro.grid(row=0,column=0,)
        self.botaoCadastrar = tk.Button(self.frame_esquerda_cima, text="Adicionar viagem", command=self.AbrirFormulario)
        self.botaoCadastrar.grid(row=1, column=0,pady=5)

        self.textoEditar = tk.Label(self.frame_esquerda_cima, text='Listar Viagens',bg="#4169E1")
        self.textoEditar.grid(row=2,column=0,pady=5)
        self.botaoEditar = tk.Button(self.frame_esquerda_cima, text="Listar", command=self.AbrirEdicao)
        self.botaoEditar.grid(row=3, column=0)

        self.textoFiltrar = tk.Label(self.frame_esquerda_baixo, text='Filtrar por',bg="#4169E1")
        self.textoFiltrar.grid(row=4,column=0,pady=5)
        self.botaoFiltrar = tk.Button(self.frame_esquerda_baixo, text="Filtrar", command=self.AbrirFiltro)
        self.botaoFiltrar.grid(row=6, column=0)

    def ExibirTela(self):
        try:
            self.treeMissoes.delete(*self.treeMissoes.get_children()) 
            viagens = self.objBD.select_missoes()
            for viagem in viagens:
                self.treeMissoes.insert("", tk.END, values=viagem)
        except Exception as erro:
            print(erro)

    def ExibirTelaFiltro(self):
        viagens=[]
        inicio = self.entrydata_inicio.get()
        fim = self.entrydata_fim.get()
        print(f"{inicio},{fim}")
        try:
            self.treeMissoes.delete(*self.treeMissoes.get_children()) 
            viagens = self.objBD.select_intervalo(inicio,fim)
            for viagem in viagens:
                self.treeMissoes.insert("", tk.END, values=viagem)
        except Exception as erro:
            print(erro)
    
    def ExibirFiltroId(self):
        viagens=[]
        filtro_id = self.entryFiltroId.get()
        try:
            self.treeMissoes.delete(*self.treeMissoes.get_children()) 
            viagens = self.objBD.select_filtro_id(filtro_id)
            for viagem in viagens:
                self.treeMissoes.insert("", tk.END, values=viagem)
        except Exception as erro:
            print(erro)

    def Exibicao(self, janela):
        self.treeMissoes = ttk.Treeview(janela, columns=("id","nomemissao","lancamento","destino","estado","tripulacao","carga","duracao","custo","status"), show="headings")
        self.treeMissoes.column('id',width=30)
        self.treeMissoes.column('nomemissao',width=120)
        self.treeMissoes.column('lancamento',width=90)
        self.treeMissoes.column('destino',width=70)
        self.treeMissoes.column('estado',width=70)
        self.treeMissoes.column('tripulacao',width=100)
        self.treeMissoes.column('carga',width=100)
        self.treeMissoes.column('duracao',width=70)
        self.treeMissoes.column('custo',width=70)
        self.treeMissoes.column('status',width=100)

        self.treeMissoes.heading("id", text="ID ")
        self.treeMissoes.heading("nomemissao", text="Nome da Missão")
        self.treeMissoes.heading("lancamento",text= "lançamento")
        self.treeMissoes.heading("destino",text= "Destino")
        self.treeMissoes.heading("estado",text= "Estado")
        self.treeMissoes.heading("tripulacao",text="Tripulação")
        self.treeMissoes.heading("carga",text="Carga")
        self.treeMissoes.heading("duracao",text="Duração")
        self.treeMissoes.heading("custo",text="Custo")
        self.treeMissoes.heading("status",text="Status")
        self.treeMissoes.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

    def Formulario(self, janela):
        self.janela = janela
        self.lista_estados = ["Ativa","Concluída","Abortada"]
        try: 
            self.nome = tk.Label(janela, text="Nome da missão:")
            self.nome.grid(row=1 ,column=0,pady=10, sticky="w")
            self.entrynome = tk.Entry(janela)
            self.entrynome.grid(row= 1,column=1,pady=10,padx=5, sticky="w")
            
            self.lancamento = tk.Label(janela, text="Data de lançamento: ")
            self.lancamento.grid(row=1 ,column=2,pady=10,padx=5,sticky="w")
            self.entrylancamento = DateEntry(janela,date_pattern="yyyy/mm/dd")
            self.entrylancamento.grid(row= 1,column=3,pady=10, sticky="w")
            
            self.destino = tk.Label(janela, text="Destino: ")
            self.destino.grid(row= 2,column=0,pady=10, sticky="w")
            self.entrydestino = tk.Entry(janela)
            self.entrydestino.grid(row=2 ,column=1,pady=10,padx=5, sticky="w")

            self.estado = tk.Label(janela, text="Estado da missão: ")
            self.estado.grid(row= 2,column=2,pady=10,padx=5, sticky="w")
            self.entryestado = ttk.Combobox(janela, values= self.lista_estados)
            self.entryestado.set("Selecionar")
            self.entryestado.grid(row=2,column=3, pady = 5, sticky="w")

            self.tripulacao = tk.Label(janela, text="Tripulação: ")
            self.tripulacao.grid(row= 3,column=0,pady=10, sticky="w")
            self.entrytripulacao = tk.Entry(janela)
            self.entrytripulacao.grid(row= 3,column=1,pady=10,padx=5, sticky="w")

            self.carga = tk.Label(janela, text="Carga: ")
            self.carga.grid(row= 3,column=2,pady=10,padx=5, sticky="w")
            self.entrycarga = tk.Entry(janela)
            self.entrycarga.grid(row= 3,column=3,pady=10, sticky="w")

            self.duracao = tk.Label(janela, text="Duração da missão: ")
            self.duracao.grid(row= 4,column=0,pady=10, sticky="w")
            self.entryduracao = tk.Entry(janela)
            self.entryduracao.grid(row= 4,column=1,pady=10,padx=5, sticky="w")

            self.custo = tk.Label(janela, text="Custo:")
            self.custo.grid(row= 4,column=2,pady=10,padx=5, sticky="w")
            self.entrycusto = tk.Entry(janela)
            self.entrycusto.grid(row= 4,column=3,pady=10, sticky="w")

            self.status = tk.Label(janela, text="Status da missão: ")
            self.status.grid(row= 5,column=0,pady=10, sticky="w")
            self.entrystatus = tk.Entry(janela)
            self.entrystatus.grid(row= 5,column=1,pady=10,padx=5, sticky="w")
        except Exception as erro:
                print(erro)

    def AbrirFormulario(self):
        try: 
            formulario = tk.Toplevel()
            formulario.title("Adicionar missao")
            formulario.geometry("950x250")
        
            self.Formulario(formulario)

            self.botaoAdicionar = tk.Button(formulario, text="Adicionar missão", command= self.AdicionarMissao)
            self.botaoAdicionar.grid(row= 5,column=3)

        except Exception as erro:
            print(erro)

    def AbrirEdicao(self):
        try: 
            edicao = tk.Toplevel() 
            edicao.title("Edição de missões")
            edicao.geometry("1100x550")
            
            self.Exibicao(edicao)
            self.ExibirTela()
            self.Formulario(edicao)

            self.botaoEditar = tk.Button(edicao, text="Atualizar missão", command= self.AtualizarMissao)
            self.botaoEditar.grid(row= 6,column=1)
            self.botaoExcluir = tk.Button(edicao, text="Excluir Missão", command= self.ExcluirMissao)
            self.botaoExcluir.grid(row= 6,column=2)

            self.textoTutorial1 = tk.Label(edicao, text="1 - Selecione a missão que deseja")
            self.textoTutorial1.grid(row=0, column= 6,sticky="w")
            self.textoTutorial2 = tk.Label(edicao, text ="2 - Preencha os campos")
            self.textoTutorial2.grid(row=3, column= 6,sticky='w')
            self.textoTutorial3 = tk.Label(edicao, text="3 - Clique em Atualizar ou Excluir missão")
            self.textoTutorial3.grid(row=6, column= 6,sticky="sw")

        except Exception as erro:
            print(erro)

    def AbrirFiltro(self):
        janela_filtro = tk.Toplevel() 
        janela_filtro.title("Detalhes da missão: ")
        janela_filtro.geometry("950x250")

        try:
            self.lancamento = tk.Label(janela_filtro, text="Data inicial: ")
            self.lancamento.grid(row=0 ,column=0,padx=5,pady=5)
            self.entrydata_inicio = DateEntry(janela_filtro,date_pattern="yyyy-mm-dd")
            self.entrydata_inicio.grid(row= 0,column=1,padx=5,pady=5)

            self.lancamento = tk.Label(janela_filtro, text="Data final: ")
            self.lancamento.grid(row=1 ,column=0,padx=5,pady=5)
            self.entrydata_fim = DateEntry(janela_filtro,date_pattern="yyyy-mm-dd")
            self.entrydata_fim.grid(row= 1,column=1,padx=5,pady=5)

            self.botaomostrarFiltro = tk.Button(janela_filtro,text="Filtrar por data",command=self.ExibirFiltro)
            self.botaomostrarFiltro.grid(row=0,column=3,rowspan=2,padx=5,pady=5)

            self.textoFiltroId = tk.Label(janela_filtro,text="Id da missão")
            self.textoFiltroId.grid(row=3 ,column=0,padx=5,pady=5)
            self.entryFiltroId = tk.Entry(janela_filtro)
            self.entryFiltroId.grid(row= 3,column=1,padx=5,pady=5,)
            
            self.botaoMostrarMissaoId = tk.Button(janela_filtro,text="Filtrar por ID",command=self.ExibirMissaoId)
            self.botaoMostrarMissaoId.grid(row=3,column=3,padx=5,pady=5)

        except Exception as erro:
            print( "erro",erro)

    def ExibirFiltro(self):
        mostrar_intervalo = tk.Toplevel() 
        mostrar_intervalo.title("Missão por data: ")
        mostrar_intervalo.geometry("950x250")

        try:
            self.Exibicao(mostrar_intervalo)
            self.ExibirTelaFiltro()
        
        except Exception as erro:
            print(erro)

    def ExibirMissaoId(self):
        janela_missao_id = tk.Toplevel() 
        janela_missao_id.title("Missão por Id: ")
        janela_missao_id.geometry("950x250")

        try:
            self.Exibicao(janela_missao_id)
            self.ExibirFiltroId()
            
        except Exception as erro:
            print(erro)

    def AdicionarMissao(self):
        try:
            nome = self.entrynome.get()
            lacamento = self.entrylancamento.get()
            destino = self.entrydestino.get()
            estado = self.entryestado.get()
            tripulacao = self.entrytripulacao.get()
            carga = self.entrycarga.get()
            duracao = self.entryduracao.get()
            custo = float(self.entrycusto.get())
            status = self.entrystatus.get()

            self.objBD.inserirDados(nome,lacamento,destino,estado,tripulacao,carga,duracao,custo,status)

            self.entrynome.delete(0, tk.END)
            self.entrylancamento.delete(0,tk.END)
            self.entrydestino.delete(0,tk.END)
            self.entryestado.delete(0,tk.END)
            self.entrytripulacao.delete(0,tk.END)
            self.entrycarga.delete(0,tk.END)
            self.entryduracao.delete(0,tk.END)
            self.entrycusto.delete(0, tk.END)
            self.entrystatus.delete(0,tk.END)

            print('Missão cadastrado com sucesso')
        except Exception as erro:
            print(erro)

    def AtualizarMissao(self):
        try:
            select_item = self.treeMissoes.selection()
            if not select_item:
                return
            item = self.treeMissoes.item(select_item)
            missao = item['values']
            missao_id = int(missao[0])
            nome_missao = self.entrynome.get()
            lancamento = self.entrylancamento.get()
            destino= self.entrydestino.get()
            estado_missao= self.entryestado.get()
            tripulacao= self.entrytripulacao.get()
            carga= self.entrycarga.get()
            duracao = self.entryduracao.get()
            custo = float(self.entrycusto.get())
            status = self.entrystatus.get()

            self.objBD.update_missoes(missao_id,nome_missao,lancamento,destino,estado_missao,tripulacao,carga,duracao,custo,status)
            self.ExibirTela()
 
            self.entrynome.delete(0, tk.END)
            self.entrylancamento.delete(0, tk.END)
            self.entrydestino.delete(0, tk.END)
            self.entryestado.delete(0, tk.END)
            self.entrytripulacao.delete(0, tk.END)
            self.entrycarga.delete(0, tk.END)
            self.entryduracao.delete(0, tk.END)
            self.entrycusto.delete(0, tk.END)
            self.entrystatus.delete(0, tk.END)
        except Exception as erro:
            print(erro)

    def ExcluirMissao(self):
        try:
            selected_item = self.treeMissoes.selection()
            if not selected_item:
                return
            item = self.treeMissoes.item(selected_item)
            missao = item['values']
            missao_id = missao[0]
            self.objBD.delete_missoes(missao_id)
            self.ExibirTela()
        except Exception as erro:
            print(erro)

    
janela = tk.Tk()
app_missao = PrincipalBD(janela)
janela.title("Aplicação Missão")
janela.geometry("950x250")
janela.mainloop()
