class Mixer:
  kecepatan_sekarang = 0

  #fungsi construktor
  def __init__(self, nama_merk, jumlah_tungkai_pengaduk, kecepatan_mixer):
    self.nama_merk = nama_merk
    self.jumlah_tungkai_pengaduk = jumlah_tungkai_pengaduk
    self.kecepatan_mixer = kecepatan_mixer

#membuat fungsi dari mixer
  def nyalakanMixer(self):
    print('Mixer menyala ', self.nama_merk)

  def matikanMixer(self):
    print('Mixer dimatikan ', self.nama_merk)

  def menambahKecepatan(self):
    self.kecepatan_sekarang = self.kecepatan_sekarang + 2
    print('kecepatan_sekarang ', self.kecepatan_sekarang)

class Mixer2(Mixer):
    def __init__(self, nama_merk, jumlah_tungkai_pengaduk, kecepatan_mixer):
        super(Mixer2, self).__init__(nama_merk, jumlah_tungkai_pengaduk, kecepatan_mixer)
    def menambahKecepatan(self, kec):
        self.kecepatan_sekarang = self.kecepatan_sekarang + kec
        print('kecepatan_sekarang ', self.kecepatan_sekarang)

mixer_dapur = Mixer2("Phillips", "2", "0")
mixer_dapur.menambahKecepatan(3)
print(mixer_dapur.__dict__)