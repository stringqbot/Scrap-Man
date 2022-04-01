class Translation(object):
    START_TEXT = """<b>QB SCRAP untuk membantu km mengambil APP ID dan API HASH!
━━━━━━━━━━━━━━━━━━━━━━━━
silahkan masukan nomor telepon telegram km dengan format kode negara,
contoh : +628xxxxxxx</b>
"""
    AFTER_RECVD_CODE_TEXT = """no HP diterima!
silahkan kirim kode yang km terima dari telegram!

kode ini hanya digunakan untuk tujuan mendapatkan ID APP dari my.telegram.org
jika km tida percaya bot ini, ambil manual aja tolol😁✌️
"""
    BEFORE_SUCC_LOGIN = "kode diterima, scarpping web page ..."
    ERRED_PAGE = """duh error, coba dengan cara manual

cara ambil APP ID dan API HASH secara manual
1. buka my.telegram.org/auth
2. login akun telegram km
3. klik menu API development
4. isi data seperti dibawah ini :
• app Title : tgbot
• short Name : tgbot
• URL : (kosongin)
• platform : desktop
5. selesai

bila berhasil ambil manual silahkan coba lagi di bot ini"""
    CANCELLED_MESG = "byee! silahkan /start kembali untuk mengulang"
    IN_VALID_CODE_PVDED = "kode OTP yang km masukan SALAH"
    IN_VALID_PHNO_PVDED = "no HP yang km masukan SALAH, silahkan masukan nomor telepon telegram dengan format kode negara.
,\ncontoh: +628xxxxxxx"
