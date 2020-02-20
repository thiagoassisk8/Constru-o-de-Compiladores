import tkinter as tk
'''frase = input('Digite a sua frase: \n')
espaços = 0
caractere = 0
frasesemespaco = ""

    
  for letra in range(0,len(frase)):

    if frase[letra] == " ":
        espaços += 1
    else:
        frasesemespaco += frase[letra]
        caractere += 1
    
print ("1. - Total de caracteres encontrados:  {}   \n2. - Total de espaços em branco encontrados: {}  \n3. – Boanoiteturmadecompiladores: {}".format(caractere,espaços,frasesemespaco))'''
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Compilador')
label1.config(font=('Impact', 20))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Digite sua frase:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def Analisador ():    
    frase = entry1.get()
    espaços = 0
    caractere = 0
    frasesemespaco = ""

    
    for letra in range(0,len(frase)):

        if frase[letra] == " ":
            espaços += 1
        else:
            frasesemespaco += frase[letra]
            caractere += 1
            
    #print(frase)
    
    label3 = tk.Label(root, text= 'A frase que você digitou é ' + frase,font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    #label4 = tk.Label(root, text= frase,font=('helvetica', 10, 'bold'))
    #canvas1.create_window(240, 230, window=label4)
    
    label5 = tk.Label(text= 'Total de caracteres encontrados:' + str(caractere),font=('helvetica', 10))
    canvas1.create_window(250, 240, window=label5)
    
    label6 = tk.Label(text= 'Total de espaços em branco encontrados:' + str(espaços),font=('helvetica', 10))
    canvas1.create_window(300, 260, window=label6)
    
    label7 = tk.Label(text= 'Frase sem nenhum espaço (concatenado) :' + str(frasesemespaco),font=('helvetica', 10))
    canvas1.create_window(380, 270, window=label7)
    
    
    
button1 = tk.Button(text='Analisar', command=Analisador, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(310, 135.8, window=button1)

root.mainloop()
