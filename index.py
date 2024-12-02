import tkinter as tk
import math

# Função para atualizar o visor
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Função para calcular o resultado
def calculate():
    try:
        result = eval(entry.get())  # Usa a função eval para calcular a expressão
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

# Função para limpar o visor
def clear():
    entry.delete(0, tk.END)

# Função para calcular o fatorial
def factorial():
    try:
        num = int(entry.get())
        if num < 0:
            entry.delete(0, tk.END)
            entry.insert(0, "Erro")
        else:
            result = math.factorial(num)
            entry.delete(0, tk.END)
            entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

# Função para calcular a raiz quadrada
def square_root():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

# Função para elevar um número a uma potência
def power():
    try:
        current = entry.get()
        base, exp = current.split('^')  # Espera a entrada no formato base^expoente
        result = float(base) ** float(exp)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

# Função para mostrar a função utilizada no visor (demonstrar a operação)
def show_function(func):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, func + "(" + current + ")")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora")

# Definindo o tamanho da janela
root.geometry("400x600")

# Alterando o fundo da janela
root.config(bg="#2E3B4E")

# Criando o visor (Entry)
entry = tk.Entry(root, width=16, font=("Arial", 30), borderwidth=2, relief="solid", justify="right", bg="#f1f1f1", fg="#333")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Estilo dos botões
button_style = {
    "width": 5,
    "height": 2,
    "font": ("Arial", 18),
    "borderwidth": 2,
    "relief": "solid"
}

# Função para criar botões com cores personalizadas
def create_button(root, text, row, col, command=None, bg="#DCDCDC", fg="#333", columnspan=1):
    button = tk.Button(root, text=text, **button_style, bg=bg, fg=fg, command=command)
    button.grid(row=row, column=col, padx=5, pady=5, columnspan=columnspan)
    return button

# Definindo os botões da calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('^', 5, 0), ('sqrt', 5, 1), ('!', 5, 2), ('demo', 5, 3)
]

# Adicionando os botões à janela com cores e comandos
for (text, row, col) in buttons:
    if text == "=":
        create_button(root, text, row, col, command=calculate, bg="#4CAF50", fg="white")
    elif text == "^":
        create_button(root, text, row, col, command=power, bg="#FF9800", fg="white")
    elif text == "sqrt":
        create_button(root, text, row, col, command=square_root, bg="#2196F3", fg="white")
    elif text == "!":
        create_button(root, text, row, col, command=factorial, bg="#FF5722", fg="white")
    elif text == "demo":
        create_button(root, text, row, col, command=lambda: show_function("f"), bg="#9C27B0", fg="white")
    else:
        create_button(root, text, row, col, command=lambda value=text: click_button(value))

# Botão de limpar
create_button(root, "C", 6, 0, command=clear, bg="#f44336", fg="white", columnspan=4)

# Iniciando o loop da interface gráfica
root.mainloop()
