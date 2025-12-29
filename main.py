import random
import string

def sifre_uret(uzunluk=12):
    # Harfler, sayılar ve sembolleri bir havuzda topla
    karakterler = string.ascii_letters + string.digits + string.punctuation
    
    # Rastgele seçim yap
    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

if __name__ == "__main__":
    print("--- Güvenlik Aracı v1.0 ---")
    kac_hane = int(input("Şifre kaç haneli olsun? (Örn: 10): "))
    yeni_sifre = sifre_uret(kac_hane)
    print(f"🔒 Oluşturulan Şifre: {yeni_sifre}")