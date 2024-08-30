# import tkinter as tk
# #funcao para receber os valores inputados na interface
# def submit_data():
#     nome = entry1.get()
#     idade = entry2.get()
#     om = entry3.get()
#     patente = entry4.get()
#     nip = entry5.get()

#     print(f'Nome: {nome}')
#     print(f'idade: {idade}')
#     print(f'om: {om}')
#     print(f'patente: {patente}')
#     print(f'nip: {nip}')
    
# # interface em formato grid
 
# root = tk.Tk()
# root.title("formulário")

# label1 = tk.Label(root, text="nome:")
# label1.grid(row=0, column=0,padx=10,pady=5)

# entry1 = tk.Entry(root)
# entry1.grid(row=0, column=1)

# label2 = tk.Label(root, text="idade:")
# label2.grid(row=1, column=0,padx=10,pady=5)

# entry2 = tk.Entry(root)
# entry2.grid(row=1, column=1,padx=10,pady=5)

# label3= tk.Label(root, text="om:")
# label3.grid(row=2, column=0,padx=10,pady=5)

# entry3 = tk.Entry(root)
# entry3.grid(row=2, column=1,padx=10,pady=5)

# label4= tk.Label(root, text="patente:")
# label4.grid(row=3, column=0,padx=10,pady=5)

# entry4 = tk.Entry(root)
# entry4.grid(row=3, column=1,padx=10,pady=5)

# label5= tk.Label(root, text="nip:")
# label5.grid(row=4, column=0,padx=10,pady=5)

# entry5 = tk.Entry(root)
# entry5.grid(row=4, column=1,padx=10,pady=5)

# submit_button = tk.Button(root, text="Cadastrar", command=submit_data)
# submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# root.mainloop()

