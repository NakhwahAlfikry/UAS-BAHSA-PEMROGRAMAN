import math

def segi_empat(sisi):
    """Menghitung luas dan keliling segi empat"""
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def persegi_panjang(panjang, lebar):
    """Menghitung luas dan keliling persegi panjang"""
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def segitiga(alas, tinggi, sisi1, sisi2, sisi3):
    """Menghitung luas dan keliling segitiga"""
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    return luas, keliling

def lingkaran(jari_jari):
    """Menghitung luas dan keliling lingkaran"""
    luas = math.pi * jari_jari * jari_jari
    keliling = 2 * math.pi * jari_jari
    return luas, keliling
