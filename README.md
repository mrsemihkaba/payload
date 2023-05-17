Bu proje, Python programlama dilini kullanarak msfvenom adlı bir aracı otomatize etmek amacıyla tasarlanmış bir menü tabanlı bir araçtır. Msfvenom, saldırı testleri ve siber güvenlik alanında kullanılan bir araçtır ve çeşitli platformlar için zararlı yazılım (payload) oluşturma işlemlerini gerçekleştirir.

Bu projede, kullanıcıya bir menü sunulur ve kullanıcı, çeşitli payload seçenekleri arasından seçim yapabilir. Seçimine göre, msfvenom kullanılarak hedef IP adresi, port numarası ve payload türüne göre özel payload'lar oluşturulur. Kullanıcı ayrıca payload dosya adını da belirleyebilir.

Projede kullanıcıdan alınan girdiler, msfvenom komutunu oluşturmak için kullanılır ve oluşturulan komut, subprocess modülü kullanılarak sistem komutu olarak çalıştırılır. Bu sayede, msfvenom otomatik olarak çalıştırılır ve kullanıcının belirlediği hedefe yönelik payload dosyası oluşturulur.

Proje, hedef IP adresi, port numarası ve payload dosya adı gibi değerleri kullanıcıdan girmesini isteyerek esneklik sağlar. Aynı zamanda, menü tabanlı bir arayüzle kullanıcı dostu bir deneyim sunar.

Bu araç, siber güvenlik profesyonelleri ve etik hackerlar tarafından kullanılan test ve değerlendirme süreçlerinde yardımcı olabilir. Kullanıcıların hedefe özgü payload'lar oluşturması için kolaylık sağlar ve süreci otomatize ederek zaman tasarrufu sağlar.

Bu projeyi, hedef sisteme yönelik özel payload'lar oluşturmak veya msfvenom'u daha kullanıcı dostu bir şekilde kullanmak isteyen herkes kullanabilir. Bununla birlikte, msfvenom'un etik kullanım sınırları içinde ve yasal izinlerle kullanılması önemlidir.

Bu proje, Python programlama becerilerini geliştirmek, sistem çağrılarını yapmak ve menü tabanlı bir kullanıcı arayüzü tasarlamak için bir örnek olarak da kullanılabilir.
