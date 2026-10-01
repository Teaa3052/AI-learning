# CLAUDE.md

Repozitorij za učenje programiranja. Cilj je postati **AI engineer / backend developer** u Pythonu. Plan s napretkom je u [PLAN.md](PLAN.md).

## O meni

- Učim Python od kolovoza 2026. Osnove i NumPy su gotovi, sljedeći korak je faza 02 iz plana.
- Najviše me zanima backend i arhitektura te AI engineering (LLM aplikacije, agenti, RAG), zatim frontend. DevOps/MLOps samo koliko je nužno.
- Analiza podataka mi nije zanimljiva. Kad biraš primjere, radije uzmi API-je, sustave i AI aplikacije nego grafove i statistiku.

## Kako mi pomagati

- Odgovaraj na hrvatskom.
- Ovo je repozitorij za učenje, ne za brzo dovršavanje zadataka. Kad pitam za vježbu, prvo objasni koncept i daj smjer ili hint. Cijelo rješenje napiši tek kad ga izričito tražim.
- Kad pregledavaš moj kod, reci što je dobro, što bi se napravilo drugačije i **zašto**. Nemoj sam ispravljati moje datoteke osim ako to tražim.
- Objašnjavaj kroz pitanja koja si postavljam u kodu: što funkcija prima, što vraća, što se zapravo ispisuje.
- Kad uvodiš nešto novo, poveži to s onim što već znam (npr. NumPy → embeddingi, funkcije → API rute).
- Ako primijetiš da preskačem nešto važno iz plana, reci mi.

## Struktura

- Svaka faza iz `PLAN.md` ima svoj folder: `01_python/`, `02_python_dev/`, `03_backend/`, `04_ml_basics/`, `05_ai_engineering/`, `06_architecture/`, `07_frontend/`.
- Jedna tema ili vježba po datoteci, s opisnim imenom (`broadcasting.py`, `numpy_check.py`).
- Generirane izlazne datoteke (npr. `students_updated.json`) ne idu u git, dodaju se u `.gitignore`.

## Konvencije koda

- Imena varijabli, funkcija i datoteka su na engleskom (`average_grade`, `student_analysis.py`).
- Komentari i ispisi smiju biti na hrvatskom.
- Od faze 02 nadalje: type hints, testovi u `tests/` s `pytest`, ovisnosti u virtualnom okruženju.

## Pokretanje

Skripte se pokreću iz foldera u kojem se nalaze, jer koriste relativne putanje:

```bash
cd 01_python
python main.py
```

## Git

- Commit nakon svake završene vježbe ili teme.
- Commit poruke na engleskom, u imperativu: `Add NumPy exercises: aggregation, masking`.

## Ponavljanje

Ritam ponavljanja opisan je u `PLAN.md`. Kad počinjem novu fazu, podsjeti me na kviz iz PDF-ova koje plan navodi za tu fazu i postavljaj mi pitanja jedno po jedno, bez da odmah otkriješ odgovor. Kad pišem provjeru znanja (`*_check.py`), daj mi zadatke, ali ne i rješenja.

## PDF pregledi

Nakon svakog bloka iz `PLAN.md`, kad je provjera znanja gotova, napravi PDF s pregledom naučenog. Uzor je `numpy_python_pregled.pdf`.

- Izvor je moj kod u tom bloku, git povijest i ono o čemu smo razgovarali, a ne općeniti tutorijal. Primjeri trebaju biti iz mojih datoteka.
- Struktura: kratki uvod, sadržaj, ključni pojmovi s primjerima, dijagrami za teže pojmove, česte greške koje sam radila, mini kviz s 5–10 pitanja (odgovori na zadnjoj stranici), što slijedi.
- Izrada: Python + ReportLab. Koristi TTF font koji podržava č, ć, đ, š, ž (npr. Arial iz `C:\Windows\Fonts`), a ne ugrađeni Helvetica.
- Ime datoteke: `NN_tema_pregled.pdf` u korijenu repozitorija (npr. `02a_klase_greske_pregled.pdf`). Skriptu za generiranje ne commitaj, osim ako to tražim.
- Nakon izrade označi kvačicu za taj PDF u `PLAN.md`.

## Napredak

Kad završim temu, označi kvačicu u `PLAN.md` i ažuriraj odjeljak "O meni" ako se promijenila faza.
