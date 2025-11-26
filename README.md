# User & Address Management API

Basit bir CRUD API projesi. Django ve Django REST Framework kullanılarak geliştirilmiştir. Amacı, kullanıcılar ve onların adreslerini yönetmek, eklemek, güncellemek, silmek ve görüntülemektir.

## Özellikler

- **User Tablosu**: Ad, soyad, okul, bölüm bilgilerini tutar
- **Address Tablosu**: Her adres bir kullanıcıya bağlıdır ve şehir, ülke bilgilerini içerir
- **CRUD İşlemleri**: Kullanıcı ve adresler için oluşturma, okuma, güncelleme ve silme işlemleri
- **PostgreSQL Veritabanı**: Verilerin güvenli şekilde depolanması
- **Django REST Framework**: Modern API endpoint'leri

## API Endpoints

### User Endpoints

| Method | URL | Açıklama |
|--------|-----|----------|
| GET | `/api/users/` | Tüm kullanıcıları listele |
| GET | `/api/users/<id>/` | Tek kullanıcıyı görüntüle |
| POST | `/api/users/create/` | Yeni kullanıcı oluştur |
| PUT | `/api/users/<id>/update/` | Kullanıcıyı güncelle |
| DELETE | `/api/users/<id>/delete/` | Kullanıcıyı sil |

### Address Endpoints

| Method | URL | Açıklama |
|--------|-----|----------|
| GET | `/api/addresses/` | Tüm adresleri listele |
| GET | `/api/addresses/<id>/` | Tek adresi görüntüle |
| POST | `/api/addresses/create/` | Yeni adres oluştur |
| PUT | `/api/addresses/<id>/update/` | Adresi güncelle |
| DELETE | `/api/addresses/<id>/delete/` | Adresi sil |

## İşlem Özeti

### CRUD Operasyonları

- **GET** → Listeleme / Görüntüleme
- **POST** → Oluşturma
- **PUT** → Güncelleme
- **DELETE** → Silme

### URL Yapısı

- **User CRUD**: `/api/users/...`
- **Address CRUD**: `/api/addresses/...`