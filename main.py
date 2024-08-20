import tkinter as tk

root = tk.Tk()
root.title("Minha Interface")

label = tk.Label(root, text="Cadastro de MILITAR")

label1 = tk.Label(root, text="nome")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="senha:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root, show="*")
entry2.grid(row=1, column=1)

# com essa funçao eu formo um botão que retorna uma resposta

# def on_button_click():
#     print('Botão clicado!')
# root = tk.Tk()

# button = tk.Button(root, text='Clique Aqui', command=on_button_click)
# button.pack()
label.pack()
root.mainloop()


