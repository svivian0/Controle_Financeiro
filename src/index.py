from tkinter import *
import customtkinter
import pymysql

class finanças:
    def __init__(self): ## var que iniciam com o code
        self.TelaInicial= customtkinter.CTk()    
        self.fonte="Montserrat"
        self.bold="bold"
        self.seta=PhotoImage(file="img/seta.png")
        self.qualtela=None



    def ConfgTela(self): ## configurações padrao de tela
        self.TelaInicial.geometry("1280x720")
        self.TelaInicial.configure(bg="#363636")
        self.TelaInicial.title("CONTROLE FINANCEIRO")

    def Voltar(self):
        try:
            self.TelaMetas.withdraw()
        except:
            pass
        try:
            self.TelaInicial.deiconify()
        except:
            pass
        try:
            self.TelaCarteira.withdraw()
        except:
            pass
        try:
            self.TelaGastos.withdraw()
        except:
            pass

    def BotaoVoltar(self):
        voltar=Button(self.qualtela, image=self.seta, command=self.Voltar,bg="#363636", borderwidth=0)
        voltar.place(x=0, y=0)


    def JanelaMetas(self):
        self.TelaMetas=Toplevel(self.TelaInicial)
        self.TelaInicial.withdraw()
        self.TelaMetas.geometry("1280x720")
        self.TelaMetas.configure(bg="#363636")
        self.TelaMetas.title("METAS")

        self.qualtela=self.TelaMetas
        self.BotaoVoltar()


    def JanelaCarteira(self):
        self.TelaCarteira=Toplevel(self.TelaInicial)
        self.TelaInicial.withdraw()
        self.TelaCarteira.geometry("1280x720")
        self.TelaCarteira.configure(bg="#363636")
        self.TelaCarteira.title("CARTEIRA")

        self.qualtela=self.TelaCarteira
        self.BotaoVoltar()

    def JanelaGastos(self):
        self.TelaGastos=Toplevel(self.TelaInicial)
        self.TelaInicial.withdraw()
        self.TelaGastos.geometry("1280x720")
        self.TelaGastos.configure(bg="#363636")
        self.TelaGastos.title("GASTOS")

        self.qualtela=self.TelaGastos
        self.BotaoVoltar()

    def JanelaInicial(self):
        print("ligou")
        self.ConfgTela()

        ##BLOCO SUPERIROR
        FormaSup = Frame(self.TelaInicial, bg="#D9D9D9", width=1280, height=106)
        FormaSup.place(x=0, y=0)

        NomeTelaIni= Label(self.TelaInicial, text="CONTROLE DE FINANÇAS", fg="#363636", bg="#d9d9d9", font=("Montserrat",50, "bold"))
        NomeTelaIni.place(x=209, y=-5)
        ## FIM BLOCO SUPERIOR

        BotaoMetas=customtkinter.CTkButton(self.TelaInicial,
                          fg_color="#d9d9d9",
                          text_color="#363636",
                          font=(self.fonte, 30, self.bold),
                          corner_radius=60, 
                          width=183,
                          height=62,
                          command=self.JanelaMetas,
                          text="Metas")
        BotaoMetas.place(x=37, y=241)

        BotaoCarteira=customtkinter.CTkButton(self.TelaInicial,
                          fg_color="#d9d9d9",
                          text_color="#363636",
                          font=(self.fonte, 30, self.bold),
                          corner_radius=60, 
                          width=183,
                          height=62,
                          command=self.JanelaCarteira,
                          text="Carteira")
        BotaoCarteira.place(x=37, y=363)

        BotaoCarteira=customtkinter.CTkButton(self.TelaInicial,
                          fg_color="#d9d9d9",
                          text_color="#363636",
                          font=(self.fonte, 30, self.bold),
                          corner_radius=60, 
                          width=183,
                          height=62,
                          command=self.JanelaGastos,
                          text="Gastos")
        


        BotaoCarteira.place(x=37, y=495)






    def Iniciar(self):
        self.TelaInicial.mainloop()

if __name__ == "__main__":
    app=finanças()
    app.JanelaInicial()
    app.Iniciar()