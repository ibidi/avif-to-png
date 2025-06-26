from PIL import Image
import os
import pillow_avif  # AVIF desteğini Pillow'a ekler


def avif_to_png(input_path, output_path=None):
    # Çıktı yolu belirtilmemişse, aynı isimle PNG uzantısı oluştur
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".png"

    # AVIF dosyasını aç
    with Image.open(input_path) as img:
        # PNG olarak kaydet
        img.save(output_path, "PNG")
        print(f"Dönüştürüldü: {output_path}")

# Örnek kullanım
avif_to_png("ibi1.avif")
avif_to_png("ibi2.avif")
avif_to_png("ibi3.avif")
avif_to_png("ibi4.avif")
avif_to_png("ibi5.avif")
