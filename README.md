# QuizApp
Program iki parçadan oluşmaktadır. Server ve Client hiyerarşisinden . Programımız sınırsız client desteklemektedir. Bir client bağlandığında 
bu işlemi arka plan işlemi olarak çalıştırmaktadır. Diğer client’lerin işlemlerini de bu şekilde halledilebilmektedir. Programımızda verileri 
gönderirken , pickle sınıfından yararlandık . Bu sayede verileri nesne olarak gönderebildik . Server ımıza ilk oyuncu bağlandığında bir oyun 
oluşturulur ve bağlanan oyuncuya bir numara verilir. Oyun server içerisinde game adlı sözlüğe kaydedilir ve böylece server oyunlar arasındaki
bilgi farklarından haberdar olur. İlk oyuncu rakip bulunana kadar bekler rakip bulunduğunda oyun otomatik olarak başlar. Oyunu ilk bitiren 
oyuncu rakip oyuncunun oyunu bitirmesini bekler rakip oyuncu oyunu bitirdiğinde iki tarafta birbirinin cevaplarını görüntüler ve oyundaki 
puan sistemine göre puanlarını alırlar.

Oyun Eşleştirme Sistemi
- İlk bağlanan oyuncu player = 0 numarasını alır ve ikinci oyuncuyu bekler.
- İkinci Oyuncu player = 1 numarasını alır ve oyun başlar
- Her iki oyuncuda bir bir oyun oluşturulmuş ve diğer oyuncuların oyunları ile karışmaması için game sözlüğüne kaydedilir.


Mustafa Taşçı
Şevket Sinan Dönder 
Berk Osman Civek
Cemalettin Yakar
