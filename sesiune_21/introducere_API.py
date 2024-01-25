'''
API-urile sau interfete de programare a aplicatiilor (Aplication Programming Interface)
permit aplicatiilor software sa comunice intre ele.
Actioneaza ca un mediator intre doua aplicatii, permitand uneia sa solicite
date sau servicii de la cealalta si sa primeasca raspunsuri in schimb.
API-urile fac posibil ca aplicatiile sa acceseze functii sau date ale altor platforme
deschizand posibilitati infinite de integrare si inovare.
'''

'''
REST (REpresentational State Transfer) este un stil arhitectural pt furnizarea
de standarde intre sisteme computerizate de pe web, facilitand comunicarea intre ele.
Sistemele compatibile REST, numite si RESTFUL, se caracterizeaza prin modul
in care sunt independente si separa preocuparile clientului si ale serverului.
Pentru ca un API sa fie considerat RESTFUL trebuie sa respecte urmatoarele
constrangeri:

1-> arhitectura client - server: clientul si serverul sunt separate si actioneaza
independent permitand utilizarea a diferite tehnologii pentru fiecare.

2-> stateless(fara stare): serverul nu stocheaza niciun context pentru client intre
cereri, astfel incat fiecare cerere contine toate informatiile necesare pentru
a o finaliza.

3-> capacitate de cache: clientii pot stoca in cache datele de raspuns reducand
nr de solicitari catre server, astfel imbunatatind performanta.

4-> utilizarea metodelor HTTP

5-> utilizarea codurilor de stare HTTP: API-urile RESTFUL folosesc aceste coduri pt
a indica starea rezultatului unei solicitari, cum ar fi succes(200), esec(400),
negasit(404) https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
'''