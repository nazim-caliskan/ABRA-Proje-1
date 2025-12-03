import json
import time

def main():

    giris_dosya_adi = input("JSON dosyasının adını yazın (örnek: veriler.json): ")


    with open(giris_dosya_adi, "r", encoding="utf-8") as f:
        veri = json.load(f)


    liste1 = veri.get("liste1", [])
    liste2 = veri.get("liste2", [])

    kume1 = set(liste1)
    kume2 = set(liste2)

    basla = time.perf_counter()
    birlesim = kume1.union(kume2)
    sure_birlesim = time.perf_counter() - basla

    basla = time.perf_counter()
    kesisim = kume1.intersection(kume2)
    sure_kesisim = time.perf_counter() - basla

    basla = time.perf_counter()
    fark_1_2 = kume1.difference(kume2)
    sure_fark_1_2 = time.perf_counter() - basla

    basla = time.perf_counter()
    fark_2_1 = kume2.difference(kume1)
    sure_fark_2_1 = time.perf_counter() - basla

    sonuc = {
        "birlesim": {
            "sonuc": list(birlesim),
            "sure_saniye": sure_birlesim
        },
        "kesisim": {
            "sonuc": list(kesisim),
            "sure_saniye": sure_kesisim
        },
        "fark_liste1_eksi_liste2": {
            "sonuc": list(fark_1_2),
            "sure_saniye": sure_fark_1_2
        },
        "fark_liste2_eksi_liste1": {
            "sonuc": list(fark_2_1),
            "sure_saniye": sure_fark_2_1
        }
    }

    cikis_dosya_adi = "sonuc.json"
    with open(cikis_dosya_adi, "w", encoding="utf-8") as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=4)

    print(f"İşlem tamamlandı! Sonuçlar '{cikis_dosya_adi}' dosyasına yazıldı.")

if __name__ == "__main__":
    main()
