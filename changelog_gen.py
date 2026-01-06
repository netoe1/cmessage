import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

# Histórico em memória
historico = []

def gerar_markdown():
    data = entry_data.get()
    commit = entry_commit.get()
    tipo = combo_tipo.get()
    descricao = entry_desc.get()
    autor = entry_autor.get()
    versao = entry_versao.get()
    obs = entry_obs.get() or "—"

    if not (commit and descricao and versao):
        messagebox.showwarning("Campos obrigatórios",
                               "Commit, Descrição e Versão são obrigatórios.")
        return

    linha = f"| {data} | {commit} | {tipo} | {descricao} | {autor} | {versao} | {obs} |"
    historico.append(linha)

    atualizar_historico()
    limpar_campos()

def atualizar_historico():
    text_hist.delete("1.0", tk.END)

    cabecalho = (
        "| Data | Commit | Tipo | Descrição | Autor | Versão | Obs |\n"
        "|------|--------|------|-----------|-------|--------|-----|\n"
    )

    text_hist.insert(tk.END, cabecalho)
    for linha in historico:
        text_hist.insert(tk.END, linha + "\n")

def limpar_campos():
    entry_commit.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_obs.delete(0, tk.END)

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Gerador de Changelog Markdown")
root.geometry("900x600")

frame_form = ttk.Frame(root, padding=10)
frame_form.pack(fill="x")

# Linha 1
ttk.Label(frame_form, text="Data").grid(row=0, column=0)
entry_data = ttk.Entry(frame_form)
entry_data.grid(row=1, column=0)
entry_data.insert(0, date.today().isoformat())

ttk.Label(frame_form, text="Commit").grid(row=0, column=1)
entry_commit = ttk.Entry(frame_form)
entry_commit.grid(row=1, column=1)

ttk.Label(frame_form, text="Tipo").grid(row=0, column=2)
combo_tipo = ttk.Combobox(frame_form, values=[
    "feat", "fix", "refactor", "docs", "test", "chore"
])
combo_tipo.grid(row=1, column=2)
combo_tipo.set("feat")

ttk.Label(frame_form, text="Versão").grid(row=0, column=3)
entry_versao = ttk.Entry(frame_form)
entry_versao.grid(row=1, column=3)

# Linha 2
ttk.Label(frame_form, text="Descrição").grid(row=2, column=0, columnspan=2)
entry_desc = ttk.Entry(frame_form, width=50)
entry_desc.grid(row=3, column=0, columnspan=2)

ttk.Label(frame_form, text="Autor").grid(row=2, column=2)
entry_autor = ttk.Entry(frame_form)
entry_autor.grid(row=3, column=2)

ttk.Label(frame_form, text="Observações").grid(row=2, column=3)
entry_obs = ttk.Entry(frame_form)
entry_obs.grid(row=3, column=3)

# Botão
ttk.Button(frame_form, text="Adicionar ao histórico",
           command=gerar_markdown).grid(row=4, column=0, columnspan=4, pady=10)

# Histórico
frame_hist = ttk.Frame(root, padding=10)
frame_hist.pack(fill="both", expand=True)

ttk.Label(frame_hist, text="Histórico de Versões (Markdown)").pack(anchor="w")

text_hist = tk.Text(frame_hist, font=("Courier", 10))
text_hist.pack(fill="both", expand=True)

root.mainloop()
