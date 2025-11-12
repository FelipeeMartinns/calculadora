from tkinter import*
from simpleeval import simple_eval


root=Tk()



class funcoes:
    def __init__(self):
        self.lista = []
        self.resultado=''

    def empilhar(self, valor):
        self.lista.append(valor)

    def resultadopainel(self):

         self.resultado = ''.join(self.lista)
         return self.resultado
    
    def limpar_tela(self):

        self.lista.clear()
        self.resultado = ''
        self.painel.config(text="")

    def acao_botao(self, valor):
        self.empilhar(valor)
        novo_texto = self.resultadopainel()
        self.painel.config(text=novo_texto)    

    def calcular(self):

        try:
            expressao = ''.join(self.lista)
            resultado = simple_eval(expressao)
            self.painel.config(text=str(resultado))
            self.lista = [str(resultado)]
        except:
            self.painel.config(text="Erro")
        


class Aplicattion(funcoes):

    def __init__(self):
        super().__init__()
        self.root=root
        self.tela()
        self.frame_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title('CALCULADORA')
        self.root.geometry('788x588')
        self.root.configure(background="#698FC7")
        self.root.resizable(True,True)
        self.root.maxsize(width=788 , height= 588)
        self.root.minsize( width=588, height= 388)

    def frame_da_tela(self):

       self.frame1= Frame(self.root, bd= 4 , bg= "#C2C2C2" , highlightthickness= 3 , highlightbackground= '#000000')
       self.frame1.place(relx= 0.25, rely= 0.02, relwidth= 0.5, relheight= 0.95)

    def widgets_frame1(self):

        self.painel= Label(self.frame1, bg="#A3A3A3", text=f'{self.resultado}')
        self.painel.place(relx= 0.02, rely= 0.05, relwidth= 0.97, relheight= 0.1)

        ### botões

        #7
        self.bot7 = Button(self.frame1, text='7', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('7') )
        self.bot7.place(relx= 0.02, rely= 0.2, relwidth= 0.14, relheight= 0.08)
        #8
        self.bot8 = Button(self.frame1, text='8', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('8'))
        self.bot8.place(relx= 0.22, rely= 0.2, relwidth= 0.14, relheight= 0.08)
        #9
        self.bot9 = Button(self.frame1, text='9', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('9'))
        self.bot9.place(relx= 0.42, rely= 0.2, relwidth= 0.14, relheight= 0.08)
        #4
        self.bot4 = Button(self.frame1, text='4', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('4'))
        self.bot4.place(relx= 0.02, rely= 0.35, relwidth= 0.14, relheight= 0.08)
        #5
        self.bot5 = Button(self.frame1, text='5', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('5'))
        self.bot5.place(relx= 0.22, rely= 0.35, relwidth= 0.14, relheight= 0.08)
        #6
        self.bot6 = Button(self.frame1, text='6', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('6'))
        self.bot6.place(relx= 0.42, rely= 0.35, relwidth= 0.14, relheight= 0.08)
        #1
        self.bot1 = Button(self.frame1, text='1', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('1'))
        self.bot1.place(relx= 0.02, rely= 0.50, relwidth= 0.14, relheight= 0.08)
        #2
        self.bot2 = Button(self.frame1, text='2', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('2'))
        self.bot2.place(relx= 0.22, rely= 0.50, relwidth= 0.14, relheight= 0.08)
        #3
        self.bot3 = Button(self.frame1, text='3', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('3'))
        self.bot3.place(relx= 0.42, rely= 0.5, relwidth= 0.14, relheight= 0.08)
        #0
        self.bot0 = Button(self.frame1, text='0', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('0'))
        self.bot0.place(relx= 0.02, rely= 0.65, relwidth= 0.14, relheight= 0.08)
        #,
        self.botvi = Button(self.frame1, text=',', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('.'))
        self.botvi.place(relx= 0.22, rely= 0.65, relwidth= 0.14, relheight= 0.08)
        #x
        self.botx = Button(self.frame1, text='X', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('*'))
        self.botx.place(relx= 0.8, rely= 0.2, relwidth= 0.14, relheight= 0.08)
        #-
        self.botmen = Button(self.frame1, text='-', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('-'))
        self.botmen.place(relx= 0.8, rely= 0.35, relwidth= 0.14, relheight= 0.08)
        #+
        self.botma = Button(self.frame1, text='+', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('+'))
        self.botma.place(relx= 0.8, rely= 0.50, relwidth= 0.14, relheight= 0.08)
        #/
        self.botdi = Button(self.frame1, text='/', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command=lambda: self.acao_botao('/'))
        self.botdi.place(relx= 0.8, rely= 0.65, relwidth= 0.14, relheight= 0.08)
        #=
        self.botigu = Button(self.frame1, text='=', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command= self.calcular)
        self.botigu.place(relx= 0.75, rely=0.8, relwidth= 0.2, relheight= 0.08)
        # c limpar tela
        self.limpar = Button(self.frame1, text='C', bd= 2 , bg= "#E9E9E9" , fg= "#000000" , font=('verdana',8,'bold'), command= self.limpar_tela)
        self.limpar.place(relx= 0.5, rely=0.8, relwidth= 0.2, relheight= 0.08)


Aplicattion()
