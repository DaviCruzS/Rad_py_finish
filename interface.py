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

        self.textoFiltrar = tk.Label(self.frame_esquerda_baixo, text='Pesquisar por ID',bg="#4169E1")
        self.textoFiltrar.grid(row=4,column=0,pady=5)
        self.id_missao = tk.Entry(self.frame_esquerda_baixo,)
        self.id_missao.grid(row=5,column=0)
        self.botaoFiltrar = tk.Button(self.frame_esquerda_baixo, text="Pesquisar", command=self.AbrirFiltro)
        self.botaoFiltrar.grid(row=6, column=0)

    def ExibirTela(self):
        try:
            self.treeMissoes.delete(*self.treeMissoes.get_children()) 
            viagens = self.objBD.select_missoes()
            for viagem in viagens:
                self.treeMissoes.insert("", tk.END, values=viagem)
        except Exception as erro:
            print(erro)

    def ExibirTelaFiltro(self,id_missao):
        try:
            self.treeMissoes.delete(*self.treeMissoes.get_children()) 
            viagens = self.objBD.select_missoes_filtradas(id_missao)
            for viagem in viagens:
                self.treeMissoes.insert("", tk.END, values=viagem)
        except Exception as erro:
            print(erro)

    def AbrirFormulario(self):
        self.lista_estados = ["Ativa","Concluída","Abortada"]
        try: 
            formulario = tk.Toplevel()
            formulario.title("Adicionar missao")
            formulario.geometry("950x250")
        
            self.nome = tk.Label(formulario, text="Nome da missão:")
            self.nome.grid(row=0 ,column=0,pady=10, sticky="w")
            self.entrynome = tk.Entry(formulario)
            self.entrynome.grid(row= 0,column=1,pady=10,padx=5, sticky="w")

            self.lancamento = tk.Label(formulario, text="Data de lançamento: ")
            self.lancamento.grid(row=0 ,column=2,pady=10,padx=5,sticky="w")
            self.entrylancamento = DateEntry(formulario,date_pattern="yyyy/mm/dd")
            self.entrylancamento.grid(row= 0,column=3,pady=10, sticky="w")

            self.destino = tk.Label(formulario, text="Destino: ")
            self.destino.grid(row= 1,column=0,pady=10, sticky="w")
            self.entrydestino = tk.Entry(formulario)
            self.entrydestino.grid(row=1 ,column=1,pady=10,padx=5, sticky="w")

            self.estado = tk.Label(formulario, text="Estado da missão: ")
            self.estado.grid(row= 1,column=2,pady=10,padx=5, sticky="w")
            self.entryestado = ttk.Combobox(formulario, values= self.lista_estados)
            self.entryestado.set("Selecionar")
            self.entryestado.grid(row=1,column=3, pady = 5, sticky="w")

            self.tripulacao = tk.Label(formulario, text="Tripulação: ")
            self.tripulacao.grid(row= 2,column=0,pady=10, sticky="w")
            self.entrytripulacao = tk.Entry(formulario)
            self.entrytripulacao.grid(row= 2,column=1,pady=10,padx=5, sticky="w")

            self.carga = tk.Label(formulario, text="Carga: ")
            self.carga.grid(row= 2,column=2,pady=10,padx=5, sticky="w")
            self.entrycarga = tk.Entry(formulario)
            self.entrycarga.grid(row= 2,column=3,pady=10, sticky="w")

            self.duracao = tk.Label(formulario, text="Duração da missão: ")
            self.duracao.grid(row= 3,column=0,pady=10, sticky="w")
            self.entryduracao = tk.Entry(formulario)
            self.entryduracao.grid(row= 3,column=1,pady=10,padx=5, sticky="w")

            self.custo = tk.Label(formulario, text="Custo:")
            self.custo.grid(row= 3,column=2,pady=10,padx=5, sticky="w")
            self.entrycusto = tk.Entry(formulario)
            self.entrycusto.grid(row= 3,column=3,pady=10, sticky="w")

            self.status = tk.Label(formulario, text="Status da missão: ")
            self.status.grid(row= 4,column=0,pady=10, sticky="w")
            self.entrystatus = tk.Entry(formulario)
            self.entrystatus.grid(row= 4,column=1,pady=10,padx=5, sticky="w")

            self.botaoAdicionar = tk.Button(formulario, text="Adicionar missão", command= self.AdicionarMissao)
            self.botaoAdicionar.grid(row= 4,column=3)

        except Exception as erro:
            print(erro)

    def AbrirEdicao(self):
        edicao = tk.Toplevel() 
        edicao.title("Edição de missões")
        edicao.geometry("950x550")

        self.treeMissoes = ttk.Treeview(edicao, columns=("id","nomemissao","lancamento","destino","estado","tripulacao","carga","duracao","custo","status"), show="headings")
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
        self.ExibirTela()
        self.lista_estados = ["Ativa","Concluída","Abortada"]
        
        try: 
            self.nome = tk.Label(edicao, text="Nome da missão:")
            self.nome.grid(row=1 ,column=0,pady=10, sticky="e")
            self.entrynome = tk.Entry(edicao)
            self.entrynome.grid(row= 1,column=1,pady=10,padx=5, sticky="w")

            self.lancamento = tk.Label(edicao, text="Data de lançamento: ")
            self.lancamento.grid(row=1 ,column=2,pady=10,padx=5,sticky="e")
            self.entrylancamento = DateEntry(edicao,date_pattern="yyyy/mm/dd")
            self.entrylancamento.grid(row= 1,column=3,pady=10, sticky="w")

            self.destino = tk.Label(edicao, text="Destino: ")
            self.destino.grid(row= 2,column=0,pady=10, sticky="e")
            self.entrydestino = tk.Entry(edicao)
            self.entrydestino.grid(row=2 ,column=1,pady=10,padx=5, sticky="w")

            self.estado = tk.Label(edicao, text="Estado da missão: ")
            self.estado.grid(row= 2,column=2,pady=10,padx=5, sticky="e")
            self.entryestado = ttk.Combobox(edicao, values= self.lista_estados)
            self.entryestado.set("Selecionar")
            self.entryestado.grid(row=2,column=3, pady = 5, sticky="w")

            self.tripulacao = tk.Label(edicao, text="Tripulação: ")
            self.tripulacao.grid(row= 3,column=0,pady=10, sticky="e")
            self.entrytripulacao = tk.Entry(edicao)
            self.entrytripulacao.grid(row= 3,column=1,pady=10,padx=5, sticky="w")

            self.carga = tk.Label(edicao, text="Carga: ")
            self.carga.grid(row= 3,column=2,pady=10,padx=5, sticky="e")
            self.entrycarga = tk.Entry(edicao)
            self.entrycarga.grid(row= 3,column=3,pady=10, sticky="w")

            self.duracao = tk.Label(edicao, text="Duração da missão: ")
            self.duracao.grid(row= 4,column=0,pady=10, sticky="e")
            self.entryduracao = tk.Entry(edicao)
            self.entryduracao.grid(row= 4,column=1,pady=10,padx=5, sticky="w")

            self.custo = tk.Label(edicao, text="Custo:")
            self.custo.grid(row= 4,column=2,pady=10,padx=5, sticky="e")
            self.entrycusto = tk.Entry(edicao)
            self.entrycusto.grid(row= 4,column=3,pady=10, sticky="w")

            self.status = tk.Label(edicao, text="Status da missão: ")
            self.status.grid(row= 5,column=0,pady=10, sticky="e")
            self.entrystatus = tk.Entry(edicao)
            self.entrystatus.grid(row= 5,column=1,pady=10,padx=5, sticky="w")

            self.botaoEditar = tk.Button(edicao, text="Editar missão", command= self.AtualizarMissao)
            self.botaoEditar.grid(row= 5,column=2,padx=10,sticky="e")
            self.botaoexcluir = tk.Button(edicao, text="Excluir missão", command= self.ExcluirMissao)
            self.botaoexcluir.grid(row= 5,column=3,padx=10,sticky="w")

        except Exception as erro:
            print(erro)

    def AbrirFiltro(self):
        janela_filtro = tk.Toplevel() 
        janela_filtro.title("Detalhes da missão: ")
        janela_filtro.geometry("950x550")

        self.ExibirTelaFiltro(self.id_missao)
        
        self.treeMissoes = ttk.Treeview(janela_filtro, columns=("id","nomemissao","lancamento","destino","estado","tripulacao","carga","duracao","custo","status"), show="headings")
        
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

            self.ExibirTela()
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
            print("A missão foi excluida!")
        except Exception as erro:
            print(erro)

        except Exception as erro:
            print(erro)

        except Exception as erro:
            print(erro)
    
janela = tk.Tk()
app_missao = PrincipalBD(janela)
janela.title("Aplicação Missão")
janela.geometry("950x250")
janela.mainloop()