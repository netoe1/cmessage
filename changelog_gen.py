import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

ARQUIVO_MD = "CHANGELOG.md"

CABECALHO = (
    "| Data | Commit | Tipo | Mensagem Git | Descrição Adicional | Autor | Versão |\n"
    "|------|--------|------|---------------|---------------------|-------|--------|\n"
)

historico = {}
commits_git = []

# ---------------- Git ---------------- #

def obter_git_log_completo():
    try:
        resultado = subprocess.check_output(
            [
                "git", "log",
                "--pretty=format:%h|%an|%ad|%s",
                "--date=short"
            ],
            stderr=subprocess.DEVNULL
        ).decode("utf-8")

        commits = []
        for linha in resultado.splitlines():
            hash_, autor, data, msg = linha.split("|", 3)
            commits.append({
                "hash": hash_,
                "autor": autor,
                "data": data,
                "msg": msg
            })
        return commits
    except Exception:
        return []

# ---------------- Arquivo ---------------- #

def carregar_changelog():
    if not os.path.exists(ARQUIVO_MD):
        return

    with open(ARQUIVO_MD, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("|") and "----" not in linha and "Data" not in linha:
                partes = linha.strip().split("|")
                commit_hash = partes[2].strip()
                historico[commit_hash] = linha.strip()

def salvar_changelog():
    with open(ARQUIVO_MD, "w", encoding="utf-8") as f:
        f.write(CABECALHO)
        for linha in historico.values():
            f.write(linha + "\n")

# ---------------- Lógica ---------------- #

def atualizar_lista_commits():
    listbox.delete(0, tk.END)
    for c in commits_git:
        if c["hash"] not in historico:
            listbox.insert(
                tk.END,
                f'{c["hash"]} | {c["data"]} | {c["msg"]}'
            )

def adicionar_commit():
    selecao = listbox.curselection()
    if not selecao:
        messagebox.showwarning("Seleção", "Selecione um commit.")
        return

    descricao = text_desc.get("1.0", tk.END).strip()
    versao = entry_versao.get()
    tipo = combo_tipo.get()

    if not descricao or not versao:
        messagebox.showwarning(
            "Campos obrigatórios",
            "Descrição adicional e versão são obrigatórias."
        )
        return

    index = selecao[0]
    commit = [
        c for c in commits_git
        if f'{c["hash"]} | {c["data"]} | {c["msg"]}' == listbox.get(index)
    ][0]

    linha = (
        f"| {commit['data']} | {commit['hash']} | {tipo} | "
        f"{commit['msg']} | {descricao} | {commit['autor']} | {versao} |"
    )

    historico[commit["hash"]] = linha

    salvar_changelog()
    atualizar_lista_commits()
    atualizar_preview()
    text_desc.delete("1.0", tk.END)

def atualizar_preview():
    text_hist.delete("1.0", tk.END)
    text_hist.insert(tk.END, CABECALHO)
    for linha in historico.values():
        text_hist.insert(tk.END, linha + "\n")

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Changelog Markdown (Git Log Completo)")
root.geometry("1100x700")

frame_top = ttk.Frame(root, padding=10)
frame_top.pack(fill="x")

ttk.Label(frame_top, text="Tipo").grid(row=0, column=0)
combo_tipo = ttk.Combobox(frame_top, values=[
    "feat", "fix", "refactor", "docs", "test", "chore"
])
combo_tipo.grid(row=1, column=0)
combo_tipo.set("feat")

ttk.Label(frame_top, text="Versão").grid(row=0, column=1)
entry_versao = ttk.Entry(frame_top)
entry_versao.grid(row=1, column=1)

# Lista de commits
frame_left = ttk.Frame(root, padding=10)
frame_left.pack(side="left", fill="both", expand=True)

ttk.Label(frame_left, text="Commits do Git (não adicionados)").pack(anchor="w")

listbox = tk.Listbox(frame_left)
listbox.pack(fill="both", expand=True)

# Descrição
frame_right = ttk.Frame(root, padding=10)
frame_right.pack(side="right", fill="both", expand=True)

ttk.Label(frame_right, text="Descrição adicional").pack(anchor="w")
text_desc = tk.Text(frame_right, height=6)
text_desc.pack(fill="x")

ttk.Button(
    frame_right,
    text="Adicionar commit ao CHANGELOG",
    command=adicionar_commit
).pack(pady=10)

ttk.Label(frame_right, text="Preview CHANGELOG.md").pack(anchor="w")

text_hist = tk.Text(frame_right, font=("Courier", 10))
text_hist.pack(fill="both", expand=True)

# ---------------- Inicialização ---------------- #

carregar_changelog()
commits_git = obter_git_log_completo()
atualizar_lista_commits()
atualizar_preview()

root.mainloop()
