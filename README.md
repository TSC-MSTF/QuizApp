# QuizApp
QuizApp ağ üzerinde server ile etkileşimli bir şekilde bir quiz oyunu oynanması için kodlanmıştır. Program Python dilinde yazılmış olup nesne tabanlı programlamadan yararlanılmıştır.


Uygulama iki bölümden oluşmaktadır. Server ve Client hiyerarşisi yapısı olarak , programımız sınırsız client desteklemektedir. Bir client bağlandığında 
bu işlemi arka plan işlemi olarak çalıştırmaktadır. Diğer client’lerin işlemlerini de bu şekilde yürütebilmektedir. Programımızda verileri 
gönderirken , pickle sınıfından yararlandık . Bu sayede verileri nesne olarak gönderebildik . Server ımıza ilk oyuncu bağlandığında bir oyun 
oluşturulur ve bağlanan oyuncuya bir numara verilir. Oyun server içerisinde game adlı sözlüğe kaydedilir ve böylece server oyunlar arasındaki
bilgi farklarından haberdar olur. İlk oyuncu rakip bulunana kadar bekler rakip bulunduğunda oyun otomatik olarak başlar. Oyunu ilk bitiren 
oyuncu rakip oyuncunun oyunu bitirmesini bekler rakip oyuncu oyunu bitirdiğinde iki tarafta birbirinin cevaplarını görüntüler ve oyundaki 
puan sistemine göre puanlarını alırlar.

## Oyun Eşleştirme Sistemi
- İlk bağlanan oyuncu player = 0 numarasını alır ve ikinci oyuncuyu bekler.
- İkinci Oyuncu player = 1 numarasını alır ve oyun başlar
- Her iki oyuncuda bir bir oyun oluşturulmuş ve diğer oyuncuların oyunları ile karışmaması için game sözlüğüne kaydedilir.


## Server Sınıfı:

Server çalışma mantığı: Server sonsuz döngü ile çalışır. Her bağlantı alındığında işlemi, bir arka plan işlemine devreder ve bağlantı 
kabul etmeye devam eder.

threaded_client(conn, player, game_id) :
Client yönetimi için yazılan fonksiyondur. her clientı bir arka plan işlemi olarak çalıştırır.Bu sayede diğer client' ler işlem yapmak için beklemez.

## Client Sınıfı:

**send(reply):**

**reply:** Client ten server a giden yanıttır ve server bu yanıta göre oyun içerisinde oyun nesnesini server üzerinde değiştirip yollar. 

- send bu game nesnesini return eder.reply = "reset" ise oyunun resetlenmiş hali döner.
- reply = "get" ise bir oyun nesnesi döner.
- reply = answer ise server game.play(answer) fonksiyonunu çalıştırıp game nesnesini return eder.

## game.py:

Game.py içerisinde iki sınıf bulunmaktadır. 

**Questiostion Sınıfı**

Her soru bir nesne olarak tasarlanmıştır. Bir Question nesnesi oluşturulduğunda  soru, şıklar listeis ve doğru yanıt argümanlarını almaktadır.

**Game Sınıfı:**

Her oyun bir nesne olarak tasarlanmıştır. Bir Game nesnesi oluşturulduğunda id, question_list (soru listesi) argümanlarını almaktadır.

-------------------------------------------------------------------------------------------------------------------
- Mustafa Taşçı
- Şevket Sinan Dönder 
- Berk Osman Civek
- Cemalettin Yakar
