#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayyumun Sonsuz Çay Demleme Ritüeli
Bu kod asla bitmez. Çünkü çay demlemek bitmez.
"""

import time
import random
import sys

mesajlar = [
    "Su kaynıyor... ama henüz değil.",
    "Çay yaprakları suyla tanışıyor. Bu ciddi bir tanışma.",
    "Demleme süresi hesaplanıyor. Hesap makinesi ağlıyor.",
    "Kayyum onayı bekleniyor. Onay geldi. Devam.",
    "Bardak ısınıyor. Bardak mutlu.",
    "Şeker eklenecek mi? Hayır, çay kendi kendine yeter.",
    "Sonsuzluk başladı. Çay hâlâ demleniyor.",
    "Türk çayı dünyanın en ciddi içeceğidir. Bu bir gerçektir.",
    "Rastgele bekleme: Çay demlemek acele işi değildir.",
    "Demleme tamamlandı mı? Hayır. Asla tamamlanmaz."
]

def demle():
    print("Kayyumun Sonsuz Çay Demleme Ritüeli başlatıldı.")
    print("Asla bitmeyecek. Hazır olun.")
    print("-" * 50)
    sayac = 0
    while True:
        mesaj = random.choice(mesajlar)
        print(f"[{sayac}] {mesaj}")
        bekleme = random.uniform(0.5, 3.0)
        time.sleep(bekleme)
        sayac += 1
        if sayac % 100 == 0:
            print("*** 100 adım geçti ama çay hâlâ demleniyor. Bu normal. ***")
            # Gizli siyasi not: base64 ile saklı
            # "Çay içmeyenler birleşemez" -> Q2F5IGnlY21leWVuIHBpciBiYXJpc2luIGJpcmxlc2VtZXo=
            # Ama asıl mesaj daha derinde.

if __name__ == "__main__":
    try:
        demle()
    except KeyboardInterrupt:
        print("\n\nRitüel sona erdi. Ama çay hâlâ demleniyor... bir yerlerde.")
        print("Kayyum mührüyle onaylandı. 2 Kasım 2026 - Kayyum Grok")
        sys.exit(0)
