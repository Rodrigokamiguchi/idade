import tkinter as tk
from tkinter import messagebox

def calcular_idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento
def calcular_idade_em_dias(idade):
    return idade * 365

def ano_bissexto(ano):
    return (ano % 4 == 0 and ano% 100 != 0) or (ano % 400 == 0)

def calcular_dias_com_bissexto(ano_atual, ano_nascimento):
    idade = calcular_idade(ano_atual, ano_nascimento)
    anos_bissextos = sum(1 for ano in range(ano_nascimento, ano_atual + 1) if ano_bissexto(ano))
    dias = (idade * 365) + anos_bissextos
    return idade, dias
def calcular():
    try:
        ano_atual = int(entry_ano_atual.get())
        ano_nascimento = int(entry_ano_nascimento.get())

        if ano_nascimento > ano_atual:
            messagebox.showerror("Erro", "O ano de nascimento é maior que o ano atual")
            return
        idade = calcular_idade(ano_atual, ano_nascimento)
        dias_sem_bissexto = calcular_idade_em_dias(idade)
        idade_bissexto, dias_com_bissexto = calcular_dias_com_bissexto(ano_atual, ano_nascimento)

        output_display.delete(1.0, tk.END)
        output_display.insert(tk.END, f"Sua idade é: {idade} anos\n")
        output_display.insert(tk.END, f"Idade em dias (sem bissextos): {dias_sem_bissexto} dias\n")
        output_display.insert(tk.END, f"Idade em dias (com bissextos): {dias_com_bissexto} dias\n")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
root = tk.Tk()
root.title("Calculadora de idade")

label_ano_atual = tk.Label(root, text="Ano atual:")
label_ano_atual.grid(row=0, column=0, padx=10, pady=10)

entry_ano_atual = tk.Entry(root)
entry_ano_atual.grid(row=0, column=1, padx=10, pady=10)

label_ano_nascimento = tk.Label(root, text="Ano nascimento:")
label_ano_nascimento.grid(row=1, column=0, padx=10, pady=10)

entry_ano_nascimento = tk.Entry(root)
entry_ano_nascimento.grid(row=1, column=1, padx=10, pady=10)

btn_calcular = tk.Button(root, text="calcular", command=calcular)
btn_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

output_display = tk.Text(root, height=6, width=40)
output_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
