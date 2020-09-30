# Laboratorul de Criptografie -- Preliminarii

**Observație importantă:** Acesta **NU** este un laborator de programre.
În consecință, **nu** se va pune accent pe optimizarea codului
sau pe uneltele folosite, cîtă vreme laboratorul se poate desfășura
conform specificațiilor.

Notițele și toate materialele, inclusiv bucățile de cod care îmi
aparțin vor fi scrise și testate folosind:
- Sistem de operare: GNU/Linux Manjaro i3;
- Editor text: GNU Emacs 27;
- Compilator C++: GCC 10;
- Python 3 (dacă este cazul).

Dacă folosiți oricare dintre uneltele de mai sus și aveți nevoie de
ajutor suplimentar, pot testa exact problema.

## Unelte recomandate
*Fără a fi obligatoriu*, puteți folosi oricare dintre următoarele, cu
observația că nivelul meu de cunoștințe, deci posibilitatea de ajutor variază:
- Sistem de operare: Windows 10, macOS (instalate direct sau în mașină
  virtuală, folosind Virtualbox);
- Editor text: Emacs, vim, Visual Studio Code, Sublime Text, Notepad++;
- IDE: Visual Studio, CLion, Code::Blocks, 
- Compilator C++: GCC, LLVM, MinGW;
- Python 3 (dacă este cazul);

Interacțiunea cu acest repository și cu ecosistemul GitHub în general 
se poate face:
- din orice browser cu posibilități (foarte) limitate de editare:
  + avantaj: nu trebuie instalat nimic;
  + dezavantaje: nu prea permite modificare sau încărcare de fișiere;
- folosind aplicația [GitHub Desktop](https://desktop.github.com/), disponibilă pentru Windows și macOS:
  + avantaje: este "self-contained", nu mai trebuie instalat nimic în afară de ea și are o interfață grafică, deci nu trebuie să dați comenzi de terminal;
  + dezavantaje: durează pînă vă familiarizați cu interfața, iar editarea fișierelor trebuie făcută separat;
- folosind terminalul și, eventual, [github cli](https://cli.github.com/);
  + avantaj: rulînd în terminal, mai ales dacă folosiți și un editor precum Vim sau Emacs, aveți toate uneltele la îndemînă pentru tot procesul;
  + dezavantaj: flexibilitatea și puterea de lucru vin cu un cost destul de mare de învățare; va fi greu la început.

## Foarte scurtă introducere în GitHub
GitHub este un serviciu construit pe baza programului de Linux `git`,
scris de Linus Torvalds, creatorul kernel-ului Linux, care se remarcă prin
faptul că permite /versionarea fișierelor/. În general, programul poate lucra
cu orice fel de fișiere, dar sînt preferate fișierele (plain) text.
De aceea, este un mediu perfect pentru cei care scriu cod. În plus față
de funcționalitățile `git`-ului simplu, GitHub permite și colaborarea,
adică mai mulți utilizatori să lucreze simultan la același proiect sau chiar
la aceleași fișiere. Avînd suficientă grijă pentru a evita conflictele
(modificări simultane ale acelorași fișiere /și în aceleași locuri/),
GitHub a permis colaborarea pentru proiecte foarte populare, chiar cu sute
sau mii de membri.

Pentru a lucra minimal cu GitHub, trebuie să vă familiarizați cu următoarele
noțiuni și cuvinte-cheie:
- **versionare**: sistem de evidență a fișierelor care păstrează versiunea
  inițială a unui fișier, apoi înregistrări (logs) despre modificările care
  i s-au adus. Astfel, se poate recupera orice versiune a fișierului,
  pornind de la versiunea inițială și făcînd numărul corespunzător de
  modificări. Prin aceasta, nu este necesară memorarea tuturor versiunilor
  fișierului, ci doar a celei inițiale, plus log-ul modificărilor, separat;
- **git**: programul care are toate aceste facilități (și multe altele). Totodată,
  este comanda care prefațează toate comenzile de terminal. Astfel, apelul
  la programul `git` se va face din terminal mereu cu sintaxa `git [comandă]`;
- **GitHub**: platformă online de stocare a fișierelor și colaborare, avînd
  integrat programul `git`;
- **repository**: proiect care se versionează. Odată creat un repository, fie că
  este stocat pe computerul personal sau pe serverele GitHub, pentru toate fișierele
  din interiorul acelui repository se ține evidența folosind `git` ca mai sus.
  (Anumite fișiere pot fi ignorate, cu o comandă specială, dar comportamentul
  implicit este să se țină evidența tuturor fișierelor. Această evidență este
  coordonată de un fișier ascuns cu numele `.git` în interiorul folderului
  părinte al repository-ului);
- **branch (ramură)**: se poate lucra la un proiect versionat fie într-o variantă
  "în linie dreaptă", fie ramificată. Astfel, fiecare colaborator își poate
  crea propria ramură, în care face modificări *care nu afectează ramura principală*,
  numită `master`;
- **merge (unește)**: atunci cînd un colaborator lucrează pe o ramură separată
  și vrea să contribuie la ramura principală, lansează operațiunea de unire a
  ramurii sale cu ramura `master`. Procesul de unire se numește *merge*;
- **pull**: sincronizează repository-ul local cu cel de pe server,
  *aducînd de acolo modificările*. Acest lucru presupune că versiunea de pe
  server are modificări mai noi decît cele locale!
- **push** (sau **fetch** în GitHub Desktop) : sincronizează repository-ul local cu cel de pe server,
  *trimițînd acolo modificări*. Acest lucru presupune că versiunea de pe server
  este în urmă cu modificările față de cea locală!
- **commit**: ca substantiv, înseamnă o modificare locală despre care vrem să
  îi spunem programului `git` să o înregistreze, ca versiune nouă. Ca verb,
  înseamnă că am făcut o astfel de modificare. Este preferabil ca atunci cînd facem
  o modificare să o înregistrăm împreună cu un mesaj de cîteva cuvinte care să
  spună ce s-a schimbat;
- **staging**: etapă intermediară între realizarea modificării și înregistrarea
  ei prin commit;
- **diff**: program de terminal care arată diferențele dintre două fișiere (text).
  Se pot vedea liniile în plus, în minus și cele modificate;
- **HEAD**: numele celei mai recente modificări înregistrate.

Cîteva comenzi de bază în terminal arată astfel:
```sh
  # marchează faptul că directorul curent vrei să fie versionat
  $ git init

  # adaugă manual un fișier pentru urmărirea versiunii
  $ git add {nume_fisier}

  # elimină manual un fișier sau director, ca să nu mai fie urmărit
  $ git rm [-r] {nume_fisier_sau_director}

  # vezi diferențele între două fișiere
  $ git diff {fisier_1} {fisier_2}

  # adu modificările de pe server
  $ git pull

  # înregistrează modificarea cu un mesaj
  $ git commit -m "rezolvat problema cu funcția cmmdc()"

  # trimite modificările pe server
  $ git push

  # vezi ultimele modificări, în varianta rezumată
  $ git log --oneline

  # arată ce e nou local față de ce este pe server
  $ git status

  # copiază ce este pe server într-un director indentic, local
  $ git clone https://github.com/adimanea/fsa-lab-cripto
```
  
În versiunea desktop, majoritatea comenzilor au butoane separate, precum se poate vedea [aici](https://desktop.github.com/images/github-desktop-screenshot-windows.png).

Un exemplu concret de sesiune de lucru poate fi aceasta:
```sh
  # 1. Copiez directorul laboratorului, să am un spațiu de lucru local
  $ git clone https://github.com/adimanea/fsa-lab-cripto

  # 2. Merg în directorul respectiv, unde am treabă
  $ cd fsa-lab-cripto/lab1/teme

  # 3. Scriu tema și o salvez în directorul respectiv
  # 4. Verific faptul că tema mea este înregistrată ca nouă
  $ git status
  # output:
  On branch master
  Your branch is ahead of 'origin/master' by 1 commit.
	(use "git push" to publish your local commits)

  Untracked files:
	(use "git add <file>..." to include in what will be committed)
		  tema_adrian.cpp

  nothing added to commit but untracked files present (use "git add" to track)

  # Deci fișierul ./tema_adrian.cpp este văzut ca nou.
  # Îl adaug la versionare:
  $ git add tema_adrian.cpp

  # 5. Îmi asum modificarea, cu un mesaj
  $ git commit -m "am adăugat tema"

  # 6. Trimit modificarea pe server
  $ git push
```

**ATENȚIE: Mereu cînd începeți să lucrați, prima comandă trebuie să fie Fetch sau =pull=!**
**Acest lucru asigură faptul că modificările pe care le mai fac alți colegi nu intră**
**în conflict cu modificările voastre!**

În caz de conflict, trebuie folosită comanda `merge`.

## Resurse suplimentare
### `git` și GitHub
- Site-ul oficial al programului `git` este [aici](https://git-scm.com/);
- Programe GUI pe care le puteți folosi, ca alternativă la GitHub Desktop, [aici](https://git-scm.com/downloads/guis);
- Un exemplu de tutorial video pe Youtube [aici](https://www.youtube.com/watch?v=SWYqp7iY_Tc);
- Un tutorial de doar 2 minute, [aici](https://www.youtube.com/watch?v=hwP7WQkmECE).
