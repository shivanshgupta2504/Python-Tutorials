# 🚀 FastAPI — From Zero to Production
## Progress Tracker

> **How to use this tracker:**
> - Change `[ ]` to `[x]` when a topic is complete
> - Each topic links to the best YouTube video for that concept
> - 🎯 = Core topic | 📺 = Watch video first | 💻 = Code-heavy session

---

## Phase 1: The Foundation
> **Goal:** Understand what FastAPI is, get it running, and handle basic requests.

- [ ] 🎯 1. What is an API? + FastAPI Philosophy & Setup
  - 📺 **CampusX** → [What is an API? + Intro](https://www.youtube.com/watch?v=WJKsPchji0Q) · [FastAPI Philosophy & Setup](https://www.youtube.com/watch?v=lXx-_1r0Uss)
  - 📺 **Corey Schafer** → [Part 1: Getting Started](https://www.youtube.com/watch?v=7AMjmCTumuo)

- [ ] 🎯 2. Routing & HTTP Methods (GET, POST, PUT, DELETE)
  - 📺 **CampusX** → [HTTP Methods & Routing](https://www.youtube.com/watch?v=O8KrViWNhOM)
  - 📺 **Corey Schafer** → [Part 2: Jinja2 Templates & Routes](https://www.youtube.com/watch?v=G4NIB9Rx9Qs)

- [ ] 🎯 3. Path & Query Parameters
  - 📺 **CampusX** → [Path & Query Params](https://www.youtube.com/watch?v=VVVKEfhXCQ4)
  - 📺 **Corey Schafer** → [Part 3: Path Parameters](https://www.youtube.com/watch?v=WRjXIA5pMtk)

- [ ] 🎯 4. Request Body & Pydantic Basics
  - 📺 **CampusX** → [POST Request & Request Body](https://www.youtube.com/watch?v=sw8V7mLl3OI)
  - 📺 **Corey Schafer** → [Part 4: Pydantic Schemas](https://www.youtube.com/watch?v=9GHxnttXxrA)

---

## Phase 2: Pydantic In Depth ⚡ *(Critical — was missing from original tracker)*
> **Goal:** Master Pydantic v2 deeply. This is the backbone of all FastAPI data handling.

- [ ] 🎯 5. Field Validators & Custom Validators
  - 📺 **Corey Schafer** → [Part 4: Pydantic Schemas (revisit)](https://www.youtube.com/watch?v=9GHxnttXxrA)
  - 💡 *Topics: `@field_validator`, `@model_validator`, custom error messages*

- [ ] 🎯 6. Nested Models, Optional Fields & Default Values
  - 💡 *Topics: `Optional[T]`, nested Pydantic models, `List[Model]`, `model_config`*

- [ ] 🎯 7. Response Models & Output Shaping
  - 📺 **Corey Schafer** → [Part 4: Pydantic Schemas](https://www.youtube.com/watch?v=9GHxnttXxrA)
  - 💡 *Topics: `response_model=`, `response_model_exclude`, `model_dump()`*

- [ ] 🎯 8. Pydantic Best Practices & Common Mistakes
  - 💡 *Topics: `BaseSettings`, environment variables with Pydantic, type coercion gotchas*

---

## Phase 3: The Kitchen — Data Layer
> **Goal:** Store and retrieve real data from a database through your API.

- [ ] 🎯 9. SQLAlchemy Database Setup
  - 📺 **Corey Schafer** → [Part 5: Adding a Database](https://www.youtube.com/watch?v=NvOV3ig2tGY)
  - 💡 *Topics: SQLAlchemy ORM, models, sessions, SQLite setup*

- [ ] 🎯 10. Complete CRUD Operations
  - 📺 **Corey Schafer** → [Part 6: CRUD — PUT, PATCH & DELETE](https://www.youtube.com/watch?v=VyoGAoxQhxM)
  - 💡 *Topics: Create, Read, Update, Delete with DB, proper HTTP status codes*

- [ ] 🎯 11. Jinja2 Templates & UI Integration
  - 📺 **Corey Schafer** → [Part 2: Templates](https://www.youtube.com/watch?v=G4NIB9Rx9Qs)
  - 💡 *Topics: HTML responses, template inheritance, static files*

- [ ] 🎯 12. Alembic Migrations *(Database version control)*
  - 💡 *Topics: Why migrations matter, `alembic init`, `upgrade`, `downgrade`*

---

## Phase 4: Architecture
> **Goal:** Write clean, maintainable, production-like code structure.

- [ ] 🎯 13. Sync vs Async Execution
  - 📺 **Corey Schafer** → [Part 7: Sync vs Async](https://www.youtube.com/watch?v=2JPDt-Jp6fM)
  - 💡 *Topics: `async def` vs `def`, when to use each, aiosqlite*

- [ ] 🎯 14. Dependency Injection
  - 📺 **Corey Schafer** → [Part 8: APIRouter & Dependencies](https://www.youtube.com/watch?v=NkgIHa6KtHg)
  - 💡 *Topics: `Depends()`, reusable DB sessions, shared logic*

- [ ] 🎯 15. APIRouter & Project Organization
  - 📺 **Corey Schafer** → [Part 8: APIRouter](https://www.youtube.com/watch?v=NkgIHa6KtHg)
  - 💡 *Topics: splitting routes, `include_router`, proper folder structure*

- [ ] 🎯 16. Middleware
  - 💡 *Topics: `@app.middleware`, CORS, logging middleware, request timing*

---

## Phase 5: Security
> **Goal:** Protect your API — only the right people can access the right things.

- [ ] 🎯 17. JWT Authentication — Register & Login
  - 📺 **Corey Schafer** → [Part 10: Authentication JWT](https://www.youtube.com/watch?v=Go4wYJJhR3k)
  - 💡 *Topics: `python-jose`, password hashing with `passlib`, access tokens*

- [ ] 🎯 18. Route Protection & Authorization
  - 📺 **Corey Schafer** → [Part 11: Authorization](https://www.youtube.com/watch?v=MY0TFMMm9B0)
  - 💡 *Topics: `OAuth2PasswordBearer`, `get_current_user`, ownership checks*

- [ ] 🎯 19. Background Tasks (Email / Password Reset)
  - 📺 **Corey Schafer** → [Part 12: Background Tasks & Email](https://www.youtube.com/watch?v=AExumWjfbyo)
  - 💡 *Topics: `BackgroundTasks`, sending emails async, password reset flow*

---

## Phase 6: Advanced Features
> **Goal:** Level up with features used in real production APIs.

- [ ] 🎯 20. File Uploads & Image Processing
  - 📺 **CampusX** → [File Uploads](https://www.youtube.com/watch?v=XVu22pTwWE8)
  - 💡 *Topics: `UploadFile`, `File()`, image validation, saving to disk*

- [ ] 🎯 21. AWS S3 Integration
  - 📺 **CampusX** → [AWS S3](https://www.youtube.com/watch?v=lRArylZCeOs)
  - 💡 *Topics: `boto3`, presigned URLs, storing uploads in S3*

- [ ] 🎯 22. WebSockets *(Real-time communication)*
  - 📺 **Corey Schafer** → [Part 13: WebSockets](https://www.youtube.com/watch?v=f1zggIOxmJg)
  - 💡 *Topics: `WebSocket`, real-time notifications, chat apps*

- [ ] 🎯 23. Unit Testing with Pytest
  - 📺 **Corey Schafer** → [Part 14 & 15: Testing](https://www.youtube.com/watch?v=4HxjBvZMAg8) · [Part 15](https://www.youtube.com/watch?v=e8NnDz8uT7o)
  - 💡 *Topics: `TestClient`, fixtures, test DB, mocking*

- [ ] 🎯 24. Serving ML Models
  - 📺 **CampusX** → [Serving ML Models](https://www.youtube.com/watch?v=JdDoMi_vqbM) · [Improving the API](https://www.youtube.com/watch?v=M17qwKnmG38)
  - 📺 **CampusX** → [Docker + FastAPI for ML](https://www.youtube.com/watch?v=GToyQTGDOS4) · [AWS Deployment](https://www.youtube.com/watch?v=jlLs6hfAga4)
  - 💡 *Topics: loading `.pkl` models, Pydantic input/output schemas, prediction endpoints*

---

## Phase 7: Deployment
> **Goal:** Put your app on the internet. Make it production-ready.

- [ ] 🎯 25. Dockerizing the Application
  - 📺 **CampusX** → [Docker Fundamentals](https://www.youtube.com/watch?v=GToyQTGDOS4)
  - 📺 **Corey Schafer** → [Part 16: Docker](https://www.youtube.com/watch?v=zCTJ3AdDym4)
  - 💡 *Topics: Dockerfile, docker-compose, building & pushing images*

- [ ] 🎯 26. VPS Deployment (Nginx + SSL)
  - 📺 **Corey Schafer** → [Part 18: VPS Deployment](https://www.youtube.com/watch?v=wd1wt2d0eus)
  - 💡 *Topics: Nginx reverse proxy, SSL certificates, systemd services*

- [ ] 🎯 27. AWS Cloud Deployment
  - 📺 **CampusX** → [AWS Deployment](https://www.youtube.com/watch?v=jlLs6hfAga4) · [Full ML Deployment](https://www.youtube.com/watch?v=X0lnToYN21k)
  - 📺 **Corey Schafer** → [Part 17: AWS](https://www.youtube.com/watch?v=SO7m7nod0ts)
  - 💡 *Topics: EC2, S3, environment variables in cloud, CI/CD basics*

---

## 📊 Progress Summary

| Phase | Topics | Completed | Status |
|-------|--------|-----------|--------|
| Phase 1: Foundation | 4 | 0 | 🔴 Not Started |
| Phase 2: Pydantic In Depth | 4 | 0 | 🔴 Not Started |
| Phase 3: Data Layer | 4 | 0 | 🔴 Not Started |
| Phase 4: Architecture | 4 | 0 | 🔴 Not Started |
| Phase 5: Security | 3 | 0 | 🔴 Not Started |
| Phase 6: Advanced Features | 5 | 0 | 🔴 Not Started |
| Phase 7: Deployment | 3 | 0 | 🔴 Not Started |
| **Total** | **27** | **0** | **0%** |

> Update this table as you progress. Change 🔴 → 🟡 (In Progress) → 🟢 (Done)

---

## 📺 Full Playlist References

### CampusX — FastAPI for Machine Learning (12 videos)
| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=WJKsPchji0Q |
| 2 | https://www.youtube.com/watch?v=lXx-_1r0Uss |
| 3 | https://www.youtube.com/watch?v=O8KrViWNhOM |
| 4 | https://www.youtube.com/watch?v=VVVKEfhXCQ4 |
| 5 | https://www.youtube.com/watch?v=lRArylZCeOs |
| 6 | https://www.youtube.com/watch?v=sw8V7mLl3OI |
| 7 | https://www.youtube.com/watch?v=XVu22pTwWE8 |
| 8 | https://www.youtube.com/watch?v=JdDoMi_vqbM |
| 9 | https://www.youtube.com/watch?v=M17qwKnmG38 |
| 10 | https://www.youtube.com/watch?v=GToyQTGDOS4 |
| 11 | https://www.youtube.com/watch?v=jlLs6hfAga4 |
| 12 | https://www.youtube.com/watch?v=X0lnToYN21k |

### Corey Schafer — Python FastAPI Tutorials (18 videos)
| Part | Topic | Link |
|------|-------|------|
| 1 | Getting Started — Web App + REST API | https://www.youtube.com/watch?v=7AMjmCTumuo |
| 2 | Jinja2 Templates & HTML Responses | https://www.youtube.com/watch?v=G4NIB9Rx9Qs |
| 3 | Path Parameters & Error Handling | https://www.youtube.com/watch?v=WRjXIA5pMtk |
| 4 | Pydantic Schemas — Request & Response Validation | https://www.youtube.com/watch?v=9GHxnttXxrA |
| 5 | Adding a Database — SQLAlchemy | https://www.youtube.com/watch?v=NvOV3ig2tGY |
| 6 | CRUD — PUT, PATCH & DELETE | https://www.youtube.com/watch?v=VyoGAoxQhxM |
| 7 | Sync vs Async | https://www.youtube.com/watch?v=2JPDt-Jp6fM |
| 8 | APIRouter & Dependencies | https://www.youtube.com/watch?v=NkgIHa6KtHg |
| 9 | Frontend Forms — JavaScript & Fetch API | https://www.youtube.com/watch?v=vqjZOyT4QRs |
| 10 | Authentication — Registration & Login with JWT | https://www.youtube.com/watch?v=Go4wYJJhR3k |
| 11 | Authorization & Route Protection | https://www.youtube.com/watch?v=MY0TFMMm9B0 |
| 12 | Background Tasks & Email | https://www.youtube.com/watch?v=AExumWjfbyo |
| 13 | WebSockets | https://www.youtube.com/watch?v=f1zggIOxmJg |
| 14 | Testing — Part 1 | https://www.youtube.com/watch?v=4HxjBvZMAg8 |
| 15 | Testing — Part 2 | https://www.youtube.com/watch?v=e8NnDz8uT7o |
| 16 | Docker | https://www.youtube.com/watch?v=zCTJ3AdDym4 |
| 17 | AWS Deployment | https://www.youtube.com/watch?v=SO7m7nod0ts |
| 18 | VPS Deployment — Nginx, SSL, Custom Domain | https://www.youtube.com/watch?v=wd1wt2d0eus |
