import tkinter as tk
from tkinter import messagebox, ttk
from database import Database
from mahasiswa import Mahasiswa

db = Database()
mhs = Mahasiswa(db)
selected_id = None

def refresh_data():
    for row in tree.get_children():
        tree.delete(row)

    for data in mhs.tampilkan():
        tree.insert("", tk.END, values=data)

def reset_form():
    entry_nim.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_prodi.delete(0, tk.END)
    entry_angkatan.delete(0, tk.END)

def reset_selection():
    global selected_id
    selected_id = None
    tree.selection_remove(tree.selection())

def reset_all():
    reset_form()
    reset_selection()

def tambah_data():
    if not entry_nim.get() or not entry_nama.get() or not entry_prodi.get() or not entry_angkatan.get():
        messagebox.showwarning("Validasi", "Semua field wajib diisi!")
        return

    mhs.tambah(
        entry_nim.get(),
        entry_nama.get(),
        entry_prodi.get(),
        entry_angkatan.get()
    )
    refresh_data()
    reset_all()

def pilih_data(event):
    global selected_id

    selected = tree.selection()
    if not selected:
        return

    item = tree.item(selected[0])
    data = item["values"]

    selected_id = data[0]

    reset_form()
    entry_nim.insert(0, data[1])
    entry_nama.insert(0, data[2])
    entry_prodi.insert(0, data[3])
    entry_angkatan.insert(0, data[4])

def update_data():
    if selected_id is None:
        messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu")
        return

    mhs.update(
        selected_id,
        entry_nim.get(),
        entry_nama.get(),
        entry_prodi.get(),
        entry_angkatan.get()
    )
    refresh_data()
    reset_all()

def hapus_data():
    if selected_id is None:
        messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu")
        return

    if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data?"):
        mhs.hapus(selected_id)
        refresh_data()
        reset_all()

root = tk.Tk()
root.title("Sistem Manajemen Mahasiswa")
root.geometry("960x540")
root.configure(bg="#f4f6f8")

header = tk.Frame(root, bg="#111827", height=60)
header.pack(fill="x")

tk.Label(
    header,
    text="SISTEM CRUD MAHASISWA",
    bg="#111827",
    fg="white",
    font=("Segoe UI", 16, "bold")
).pack(pady=15)

main = tk.Frame(root, bg="#f4f6f8")
main.pack(fill="both", expand=True, padx=20, pady=20)

form_card = tk.Frame(main, bg="white", width=300)
form_card.pack(side="left", fill="y", padx=(0, 15))

tk.Label(
    form_card,
    text="Form Mahasiswa",
    bg="white",
    font=("Segoe UI", 13, "bold")
).pack(pady=15)

def input_field(label):
    tk.Label(form_card, text=label, bg="white", anchor="w").pack(fill="x", padx=20)
    e = tk.Entry(form_card)
    e.pack(fill="x", padx=20, pady=5)
    return e

entry_nim = input_field("NIM")
entry_nama = input_field("Nama")
entry_prodi = input_field("Program Studi")
entry_angkatan = input_field("Angkatan")

btn_frame = tk.Frame(form_card, bg="white")
btn_frame.pack(pady=15)

def action_btn(text, color, cmd):
    return tk.Button(
        btn_frame,
        text=text,
        bg=color,
        fg="white",
        relief="flat",
        width=12,
        command=cmd
    )

action_btn("Tambah", "#2563eb", tambah_data).grid(row=0, column=0, padx=5, pady=5)
action_btn("Update", "#16a34a", update_data).grid(row=0, column=1, padx=5)
action_btn("Hapus", "#dc2626", hapus_data).grid(row=1, column=0, padx=5, pady=5)
action_btn("Reset", "#6b7280", reset_all).grid(row=1, column=1, padx=5)

data_card = tk.Frame(main, bg="white")
data_card.pack(side="right", fill="both", expand=True)

tk.Label(
    data_card,
    text="Data Mahasiswa",
    bg="white",
    font=("Segoe UI", 13, "bold")
).pack(pady=15)

columns = ("id", "nim", "nama", "prodi", "angkatan")

tree = ttk.Treeview(
    data_card,
    columns=columns,
    show="headings"
)

tree.heading("id", text="ID")
tree.heading("nim", text="NIM")
tree.heading("nama", text="Nama")
tree.heading("prodi", text="Prodi")
tree.heading("angkatan", text="Angkatan")

tree.column("id", width=50, anchor="center")
tree.column("nim", width=100)
tree.column("nama", width=220)
tree.column("prodi", width=160)
tree.column("angkatan", width=90, anchor="center")

tree.pack(fill="both", expand=True, padx=15, pady=10)
tree.bind("<<TreeviewSelect>>", pilih_data)

refresh_data()
root.mainloop()
