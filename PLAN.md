# Plan učenja: AI engineer / backend developer

**Cilj:** graditi backend sustave u Pythonu koji koriste AI (LLM-ove, agente, RAG), uz razumijevanje arhitekture.
**Prioriteti:** backend i arhitektura + AI engineering > frontend > DevOps/MLOps (samo nužni minimum).
**Tempo:** oko 8–10 sati tjedno. Datumi su okvirni, nisu rokovi.

Svaka faza ima svoj folder (`02_...`, `03_...`) i završava malim projektom. Kvačice označavaju napredak.

---

## Ritam ponavljanja

Ponavljanje ide u tri razine:

1. **Tjedno (30 min, kraj tjedna):** bez gledanja u bilješke ponovno napisati jednu vježbu iz tog tjedna. Ako zapne, to je tema za sljedeći tjedan.
2. **Provjera znanja prije svakog PDF-a (1–2 h):** datoteka `*_check.py` sa zadacima koji kombiniraju sve iz tog bloka, kao `numpy_check.py`. Pišem je sama, bez kopiranja starog koda.
3. **Na početku svake nove faze (1–2 h):** riješiti mini kviz iz PDF-a prethodne faze i jednog starijeg PDF-a. Tako se gradivo vraća nakon 1 i nakon 2–3 mjeseca.

## PDF pregledi

Nakon svakog bloka od nekoliko lekcija (otprilike svaka 3–4 tjedna) nastaje PDF s pregledom naučenog, po uzoru na `numpy_python_pregled.pdf`. Svaki PDF sadrži:

- ključne pojmove s primjerima iz mog koda
- dijagrame za ono što je teško zamisliti iz teksta
- česte greške na koje sam naišla
- mini kviz s 5–10 pitanja (odgovori na kraju), koji služi za ponavljanje na početku sljedećih faza
- što slijedi

PDF se radi tek kad je provjera znanja (`*_check.py`) gotova, jer pregled opisuje ono što stvarno znam, a ne ono što sam samo pročitala. PDF-ovi se spremaju u korijen repozitorija kao `NN_tema_pregled.pdf`.

| PDF | Pokriva | Okvirno |
|---|---|---|
| 01 | Python osnove i NumPy | ✅ 1. 10. 2026. (`numpy_python_pregled.pdf`) |
| 02a | Klase, greške, type hints | sredina studenog 2026. |
| 02b | Paketi, okruženja, pytest, Git + projekt | kraj studenog 2026. |
| 03a | HTTP, REST, FastAPI osnove | kraj prosinca 2026. |
| 03b | SQL, PostgreSQL, SQLAlchemy, migracije | sredina siječnja 2027. |
| 03c | Autentifikacija, testiranje API-ja, async + projekt | kraj veljače 2027. |
| 04 | Osnove ML-a, embeddingi, kako rade LLM-ovi | kraj ožujka 2027. |
| 05a | LLM API-ji, prompting, strukturirani izlaz | sredina travnja 2027. |
| 05b | RAG i vektorske baze | početak svibnja 2027. |
| 05c | Alati, agenti, MCP, evaluacija + projekt | kraj svibnja 2027. |
| 06a | Čist kod i obrasci dizajna | kraj lipnja 2027. |
| 06b | Dizajn sustava, arhitektura AI sustava, Docker | kraj srpnja 2027. |
| 07 | Frontend osnove | ljeto 2027. |
| Završni | Cijeli put na jednom mjestu: šalabahter za razgovore za posao | nakon portfolio projekta |

---

## 01 Python osnove i NumPy (kolovoz – listopad 2026) ✅ većinom gotovo

- [x] Varijable, petlje, funkcije, liste, rječnici
- [x] List/dict comprehension, `map`, `lambda`
- [x] Rad s JSON datotekama (`students.json`)
- [x] NumPy: nizovi, `shape`/`ndim`/`dtype`, agregacije po `axis`
- [x] Broadcasting
- [x] Boolean maske, `any`, `argmax`, udjeli
- [x] Provjera znanja: `numpy_check.py`
- [x] **PDF 01:** `numpy_python_pregled.pdf`
- [x] Ponoviti broadcasting: zašto `scores - scores.mean(axis=1)` ne radi i kako to popraviti (`keepdims=True` ili `[:, None]`)

NumPy je dovoljan za sada. Pandas preskačemo i vraćamo mu se samo ako zatreba u projektu.

---

## 02 Python kao programer (listopad – studeni 2026)

Cilj: pisati kod koji je organiziran, testiran i spreman za veće projekte.

- [ ] **Ponavljanje na početku:** kviz iz PDF-a 01 + ispraviti broadcasting iz faze 01

**Blok A**
- [ ] Klase i objekti: `__init__`, metode, `@dataclass`
- [ ] Greške: `try`/`except`, vlastite iznimke, `raise`
- [ ] Type hints (`def average(grades: list[int]) -> float:`)
- [ ] Provjera znanja: `classes_check.py`
- [ ] **PDF 02a:** klase, greške, type hints

**Blok B**
- [ ] Moduli i paketi, `if __name__ == "__main__":`
- [ ] Rad s datotekama i putanjama (`pathlib`)
- [ ] Virtualno okruženje i ovisnosti (`uv` ili `venv` + `requirements.txt`)
- [ ] Testiranje s `pytest`
- [ ] Git: grane, `.gitignore`, dobre commit poruke
- [ ] **Projekt:** refaktorirati studentsku analizu u mali paket s klasom `Student`, type hintovima, testovima i CLI-jem (`python -m students report students.json`)
- [ ] **PDF 02b:** paketi, okruženja, pytest, Git + što sam naučila iz projekta

---

## 03 Backend (prosinac 2026 – veljača 2027)

Cilj: napraviti pravi API s bazom i korisnicima.

- [ ] **Ponavljanje na početku:** kviz iz PDF-a 02a i 02b

**Blok A**
- [ ] Kako radi web: HTTP metode, statusni kodovi, JSON, REST
- [ ] `httpx` ili `requests`: pozivanje tuđih API-ja
- [ ] FastAPI: rute, parametri, Pydantic modeli, automatska dokumentacija
- [ ] Provjera znanja: `api_check.py` (mali API s 3–4 rute bez gledanja u tutorijal)
- [ ] **PDF 03a:** HTTP, REST, FastAPI osnove

**Blok B**
- [ ] SQL osnove: `SELECT`, `JOIN`, `GROUP BY`, indeksi
- [ ] PostgreSQL (ili SQLite za početak) + SQLAlchemy
- [ ] Migracije baze (Alembic)
- [ ] Provjera znanja: `sql_check.sql` + `db_check.py`
- [ ] **PDF 03b:** SQL, baze, SQLAlchemy, migracije

**Blok C**
- [ ] Autentifikacija: lozinke (hashiranje), JWT tokeni
- [ ] Testiranje API-ja (`pytest` + FastAPI `TestClient`)
- [ ] Async u Pythonu: `async`/`await`, zašto je važan za API-je
- [ ] **Projekt:** API za bilješke (korisnici, prijava, CRUD bilješki, pretraga) na FastAPI-ju i PostgreSQL-u
- [ ] **PDF 03c:** autentifikacija, testiranje, async + arhitektura projekta

---

## 04 Osnove ML-a za AI engineera (veljača – ožujak 2027)

Cilj: razumjeti što se događa "ispod haube", bez dubokog rada s podacima.

- [ ] **Ponavljanje na početku:** kviz iz PDF-a 03a–03c + kviz iz PDF-a 01 (NumPy treba za embeddinge)
- [ ] Što je model, treniranje, overfitting, train/test podjela
- [ ] scikit-learn: jedan klasifikacijski primjer od početka do kraja
- [ ] Neuronske mreže na razini koncepta (PyTorch tutorial "60 minute blitz")
- [ ] Embeddingi: tekst kao vektor, kosinusna sličnost (ovdje NumPy opet dolazi do izražaja)
- [ ] Kako rade LLM-ovi: tokeni, kontekstni prozor, temperatura
- [ ] **Mini projekt:** semantička pretraga bilješki pomoću embeddinga i kosinusne sličnosti u NumPyju
- [ ] **PDF 04:** osnove ML-a, embeddingi, LLM-ovi

---

## 05 AI engineering (ožujak – svibanj 2027)

Cilj: graditi aplikacije koje koriste LLM-ove.

- [ ] **Ponavljanje na početku:** kviz iz PDF-a 04 + kviz iz PDF-a 03a (API-ji)

**Blok A**
- [ ] Pozivanje LLM API-ja iz Pythona, streaming, upravljanje greškama i limitima
- [ ] Prompt engineering: sistemske poruke, primjeri, strukturirani izlaz (JSON)
- [ ] Provjera znanja: `llm_check.py`
- [ ] **PDF 05a:** LLM API-ji i prompting

**Blok B**
- [ ] RAG: dijeljenje dokumenata na dijelove, embeddingi, vektorska baza (pgvector ili Chroma)
- [ ] Provjera znanja: `rag_check.py` (RAG nad 3–4 vlastita dokumenta)
- [ ] **PDF 05b:** RAG i vektorske baze

**Blok C**
- [ ] Alati (tool use / function calling): model poziva vaše Python funkcije
- [ ] Agenti: petlja "razmisli, pozovi alat, pogledaj rezultat"
- [ ] MCP (Model Context Protocol): povezivanje modela s vanjskim alatima
- [ ] Evaluacija: skup testnih pitanja, mjerenje točnosti, LLM-as-judge
- [ ] Trošak i brzina: keširanje, odabir manjeg modela gdje je dovoljan
- [ ] **Projekt:** asistent za bilješke koji odgovara na pitanja iz vaših dokumenata (RAG) i može izvršavati akcije (alati), kao dio backenda iz faze 03
- [ ] **PDF 05c:** alati, agenti, MCP, evaluacija + arhitektura asistenta

---

## 06 Arhitektura (stalno, fokus lipanj – srpanj 2027)

- [ ] **Ponavljanje na početku:** kviz iz PDF-a 05a–05c + kviz iz PDF-a 02a (klase, temelj obrazaca dizajna)

**Blok A**
- [ ] Čist kod: SOLID, odvajanje slojeva (rute → servisi → repozitoriji)
- [ ] Obrasci dizajna koji se stvarno koriste: Repository, Strategy, Dependency Injection
- [ ] Provjera znanja: refaktorirati jedan dio API-ja iz faze 03 prema naučenim obrascima
- [ ] **PDF 06a:** čist kod i obrasci dizajna

**Blok B**
- [ ] Dizajn sustava: keširanje (Redis), redovi poruka i pozadinski zadaci, skaliranje
- [ ] Monolit ili mikroservisi: kada što
- [ ] Arhitektura AI sustava: fallback kad model ne odgovori, timeoutovi, praćenje (logging), sigurnost (prompt injection)
- [ ] Crtanje dijagrama (C4 model) i zapisivanje odluka (ADR)
- [ ] Docker osnove: `Dockerfile`, `docker compose` za aplikaciju + bazu (samo nužni minimum)
- [ ] **Projekt:** nadograditi asistenta: pozadinska obrada dokumenata, Redis keš, sve pokrenuto s `docker compose up`, s dijagramom arhitekture u README-u
- [ ] **PDF 06b:** dizajn sustava, arhitektura AI sustava, Docker

---

## 07 Malo frontenda (kad poželite, najkasnije ljeto 2027)

- [ ] **Ponavljanje na početku:** kviz iz PDF-a 03a (frontend razgovara s vašim API-jem)
- [ ] Brzi prototip u Pythonu: Streamlit ili Gradio
- [ ] HTML, CSS i JavaScript osnove
- [ ] TypeScript i React osnove
- [ ] **Projekt:** sučelje za asistenta (chat, upload dokumenata)
- [ ] **PDF 07:** frontend osnove i kako se spaja s backendom

---

## Završni portfolio projekt

Jedna cjelovita aplikacija na GitHubu: backend (FastAPI + PostgreSQL), AI dio (RAG + alati + evaluacija), Docker, testovi, jednostavno sučelje i README s dijagramom arhitekture.

- [ ] **Veliko ponavljanje:** riješiti kvizove iz svih PDF-ova redom
- [ ] **Završni PDF:** cijeli put na jednom mjestu, kao šalabahter za razgovore za posao

## Literatura

- *Designing Data-Intensive Applications*, Martin Kleppmann (faza 06)
- *AI Engineering*, Chip Huyen (faze 04–05)
- Službena FastAPI dokumentacija (faza 03)
- *Fluent Python*, Luciano Ramalho (faza 02, za produbljivanje)
