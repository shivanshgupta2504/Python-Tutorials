# 🚀 FastAPI — From Zero to Production

> A structured, hands-on journey to mastering FastAPI — from Hello World to cloud deployment.

---

## 📖 About This Project

This is my personal FastAPI learning project. I'm studying FastAPI systematically, one phase at a time, using a combination of:
- **Claude AI** as my personal mentor (via this Claude Project)
- **YouTube playlists** from CampusX and Corey Schafer
- **Hands-on coding** with real challenges after every topic
- **A running Blog API** that grows with every new concept I learn

---

## 🗺️ Learning Path

| Phase | Focus | Topics |
|-------|-------|--------|
| **Phase 1** | Foundation | Setup, Routing, Parameters, Pydantic Basics |
| **Phase 2** | Pydantic In Depth | Validators, Nested Models, Response Models |
| **Phase 3** | Data Layer | SQLAlchemy, CRUD, Templates, Migrations |
| **Phase 4** | Architecture | Async, Dependency Injection, APIRouter, Middleware |
| **Phase 5** | Security | JWT Auth, Route Protection, Background Tasks |
| **Phase 6** | Advanced | File Uploads, S3, WebSockets, Testing, ML Models |
| **Phase 7** | Deployment | Docker, VPS (Nginx/SSL), AWS |

📋 Full tracker with YouTube links: [`progress-tracker.md`](./progress-tracker.md)

---

## 📁 Folder Structure

```
fastapi-learning/
│
├── 📄 README.md                    ← You are here
├── 📄 progress-tracker.md          ← Tick off topics as you complete them
│
├── 📁 notes/                       ← Summary notes from each phase
│   ├── phase-1-foundation.md
│   ├── phase-2-pydantic.md
│   ├── phase-3-database.md
│   ├── phase-4-architecture.md
│   ├── phase-5-security.md
│   ├── phase-6-advanced.md
│   └── phase-7-deployment.md
│
├── 📁 code/                        ← Individual concept practice files
│   ├── phase-1/
│   │   ├── hello_world.py
│   │   ├── routing.py
│   │   └── parameters.py
│   ├── phase-2/
│   │   └── pydantic_deep.py
│   ├── phase-3/
│   │   ├── database.py
│   │   └── crud.py
│   └── ...
│
├── 📁 challenges/                  ← My solutions to practice challenges
│   ├── phase-1-challenge-1.py
│   ├── phase-1-challenge-2.py
│   └── ...
│
└── 📁 blog-api/                    ← The running project built throughout
    ├── main.py
    ├── database.py
    ├── requirements.txt
    ├── .env.example
    ├── 📁 routers/
    │   ├── posts.py
    │   ├── users.py
    │   └── auth.py
    ├── 📁 models/
    │   └── models.py
    ├── 📁 schemas/
    │   └── schemas.py
    └── 📁 tests/
        └── test_posts.py
```

---

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.10+
- pip or uv (package manager)

### Install dependencies
```bash
# For learning code (minimal)
pip install fastapi uvicorn pydantic

# For the Blog API project (full)
cd blog-api
pip install -r requirements.txt
```

### Run the Blog API locally
```bash
cd blog-api
uvicorn main:app --reload
```

Then open:
- **Swagger UI (interactive docs):** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## 📺 Video Resources

### CampusX — FastAPI for Machine Learning
🔗 Playlist: https://www.youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ
Focus: ML model deployment, Docker, AWS — very practical ML-oriented series.

### Corey Schafer — Python FastAPI Tutorials
🔗 Playlist: https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI
Focus: Full-featured web app + REST API, 18-part complete series. Excellent for web development side.

---

## 🧠 How I Study (My System)

1. **Watch** the relevant YouTube video(s) for the topic first
2. **Study with Claude** — ask Claude (in this Project) to teach the topic deeply
3. **Solve challenges** given by Claude, then submit for code review
4. **Build** the same concept into the Blog API project
5. **Write notes** in the `notes/` folder for future revision
6. **Tick off** the topic in `progress-tracker.md`

---

## 📌 Claude Project Setup

This learning project uses a dedicated **Claude Project** with:
- A **Project-level system prompt** that defines Claude as my FastAPI mentor
- A **per-chat message** I paste at the start of each session to set phase + pacing rules
- The `progress-tracker.md` uploaded to Project files so Claude always has context

---

## 🏗️ The Running Project — Blog API

Throughout the course, I'm building a **Blog API** that includes:
- [ ] User registration & login
- [ ] Create, read, update, delete blog posts
- [ ] JWT authentication & route protection
- [ ] Image uploads (post thumbnails)
- [ ] Email notifications (background tasks)
- [ ] Full test suite
- [ ] Dockerized & deployed to cloud

---

## 📈 Progress

Started: _[fill in your start date]_
Target completion: _[fill in your target]_

See [`progress-tracker.md`](./progress-tracker.md) for detailed topic-by-topic progress.

---

*Learning in public. Building in practice. One phase at a time.* 🔥
