class Mahasiswa:
    def __init__(self, database):
        self.db = database

    def tambah(self, nim, nama, prodi, angkatan):
        query = """
        INSERT INTO mahasiswa (nim, nama, prodi, angkatan)
        VALUES (?, ?, ?, ?)
        """
        self.db.execute(query, (nim, nama, prodi, angkatan))

    def tampilkan(self):
        query = "SELECT * FROM mahasiswa"
        return self.db.fetch_all(query)

    def update(self, id_mhs, nim, nama, prodi, angkatan):
        query = """
        UPDATE mahasiswa
        SET nim=?, nama=?, prodi=?, angkatan=?
        WHERE id=?
        """
        self.db.execute(query, (nim, nama, prodi, angkatan, id_mhs))

    def hapus(self, id_mhs):
        query = "DELETE FROM mahasiswa WHERE id=?"
        self.db.execute(query, (id_mhs,))
