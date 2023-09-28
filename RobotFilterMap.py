import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def abrir_arquivo():
    global coordenadas
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.csv")])

    if arquivo:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()

        coordenadas = []
        contador = 1

        for linha in linhas:
            # Remove as aspas duplas e "P-" do início de cada linha
            linha = linha.strip('"P-')
            partes = linha.strip().split(',')
            if len(partes) == 4:
                coordenada = f"{partes[0]},{partes[1]},{contador}\n"
                coordenadas.append(coordenada)
                contador += 1

        if coordenadas:
            texto_caixa.delete(1.0, tk.END)
            texto_caixa.insert(tk.END, ''.join(coordenadas))

def salvar_arquivo():
    global coordenadas
    if coordenadas:
        arquivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivos de Texto", "*.csv")])

        if arquivo:
            with open(arquivo, 'w') as file:
                file.writelines(coordenadas)
                messagebox.showinfo(f"Sucesso", "As coordenadas foram filtradas com sucesso!")

janela = tk.Tk()
janela.title("quitoDev - QGIS Solix Map Filter V1.0.0.0")
janela.geometry("800x600")
janela.resizable(False, False)

q = tk.Label(janela, text="A quitoDev Development", width=40, height=0, font=('Times New Roman', 15, 'bold'))
d = tk.Label(janela, text="Grãos - P&D - Soluções Radical", width=40, height=0, font=('Times New Roman', 10))
largura, altura = 120, 120

q.pack()


d.pack()


botao_abrir = tk.Button(janela, text="Importar Mapa", command=abrir_arquivo)
botao_abrir.pack(pady=10)

botao_salvar = tk.Button(janela, text="Filtrar", command=salvar_arquivo)
botao_salvar.pack(pady=10)

texto_caixa = tk.Text(janela, wrap=tk.WORD, width=80, height=15)
texto_caixa.pack()

janela.mainloop()
