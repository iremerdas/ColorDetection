# Renk Tabanlı Nesne Tespiti

Bu proje, OpenCV kullanarak kırmızı, sarı ve yeşil renkli nesneleri tespit eden bir görüntü işleme sistemidir. Kamera görüntüsünü kullanarak belirli renk aralıklarında maskeleme yapar, konturları belirler ve nesnelerin konumlarını tespit eder.

## Özellikler
- Gerçek zamanlı görüntü işleme
- HSV renk aralığı kullanarak renk tespiti
- Gürültü azaltma (Gaussian Blur, Erosion, Dilation)
- Kontur analizi ve birleştirme
- Nesnelerin sol, sağ veya ortada olup olmadığını belirleme
- Açılı dikdörtgen ile nesne sınırlarını çizme

## Gereksinimler
Bu proje için aşağıdaki Python kütüphaneleri gereklidir:

```bash
pip install opencv-python numpy
```

## Kullanım
Projeyi çalıştırmak için aşağıdaki adımları takip edin:

1. Proje dosyanızı indirin veya kopyalayın.
2. Terminal veya komut satırında aşağıdaki komutu çalıştırın:

```bash
python color_detection.py
```

3. Kamera açılacak ve belirlenen renklerdeki nesneler ekranda işaretlenecektir.
4. Çıkmak için `q` tuşuna basabilirsiniz.

## Kod Açıklamaları

### 1. Renk Aralıkları
Kodda kırmızı, sarı ve yeşil renkleri tespit etmek için HSV renk uzayı kullanılmıştır:

```python
lower_red1 = np.array([1, 170, 100])
upper_red1 = np.array([5, 255, 255])
lower_red2 = np.array([170, 170, 100])
upper_red2 = np.array([179, 255, 255])
lower_yellow = np.array([25, 100, 100])
upper_yellow = np.array([30, 255, 255])
lower_green = np.array([40, 100, 100])
upper_green = np.array([70, 255, 255])
```

### 2. Görüntü İşleme
- GaussianBlur ile gürültü azaltma
- HSV formatına dönüştürme
- Renk maskeleri oluşturma ve morfolojik işlemler uygulama
- Kontur tespiti ve filtreleme
- Yakın konturların birleştirilmesi

### 3. Nesne Takibi
Tespit edilen nesnelerin pozisyonları hesaplanır ve ekranda nerede olduğu belirtilir:

```python
if x < frame.shape[1] / 3:
    print("Nesne sol tarafta.")
elif x > (2 * frame.shape[1]) / 3:
    print("Nesne sağ tarafta.")
else:
    print("Nesne ortada.")
```

## Geliştirme
Projeyi geliştirirken aşağıdaki ek özellikler eklenebilir:
- Farklı renkleri desteklemek için yeni aralıklar eklemek
- Nesne sınıflandırma ve takip algoritmaları eklemek
- Belirli bir mesafeden tespit edilen nesneleri ölçmek
