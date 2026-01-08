import tkinter as tk
from tkinter import messagebox
from database import Database
from mahasiswa import Mahasiswa

db = Database()
mhs = Mahasiswa(db)

selected_id = None

def refresh_data():
    listbox.delete(0, tk.END)
    for data in mhs.tampilkan():
        listbox.insert(tk.END, data)

def reset_form():
    global selected_id
    selected_id = None
    entry_nim.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_prodi.delete(0, tk.END)
    entry_angkatan.delete(0, tk.END)

def tambah_data():
    nim = entry_nim.get()
    nama = entry_nama.get()
    prodi = entry_prodi.get()
    angkatan = entry_angkatan.get()

    if not nim or not nama or not prodi or not angkatan:
        messagebox.showwarning("Validasi", "Semua field wajib diisi!")
        return

    mhs.tambah(nim, nama, prodi, angkatan)
    refresh_data()
    reset_form()

def pilih_data(event):
    global selected_id
    try:
        index = listbox.curselection()[0]
        data = listbox.get(index)

        selected_id = data[0]

        entry_nim.delete(0, tk.END)
        entry_nama.delete(0, tk.END)
        entry_prodi.delete(0, tk.END)
        entry_angkatan.delete(0, tk.END)

        entry_nim.insert(0, data[1])
        entry_nama.insert(0, data[2])
        entry_prodi.insert(0, data[3])
        entry_angkatan.insert(0, data[4])
    except IndexError:
        pass

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
    reset_form()

def hapus_data():
    if selected_id is None:
        messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu")
        return

    if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data?"):
        mhs.hapus(selected_id)
        refresh_data()
        reset_form()

# ================= GUI =================
root = tk.Tk()
root.title("CRUD Mahasiswa - PBO")
root.geometry("500x450")

tk.Label(root, text="NIM").pack()
entry_nim = tk.Entry(root)
entry_nim.pack()

tk.Label(root, text="Nama").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

tk.Label(root, text="Prodi").pack()
entry_prodi = tk.Entry(root)
entry_prodi.pack()

tk.Label(root, text="Angkatan").pack()
entry_angkatan = tk.Entry(root)
entry_angkatan.pack()

tk.Button(root, text="Tambah", command=tambah_data).pack(pady=5)
tk.Button(root, text="Update", command=update_data).pack(pady=5)
tk.Button(root, text="Hapus", command=hapus_data).pack(pady=5)
tk.Button(root, text="Reset", command=reset_form).pack(pady=5)

listbox = tk.Listbox(root, width=70)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", pilih_data)

refresh_data()
root.mainloop()
