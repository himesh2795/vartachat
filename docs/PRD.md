# 💬 VartaChat – Product Requirements Document (PRD)

> A self-hostable, open-source chat platform built with **FastAPI (Python)** and **React**.

---

## 🧱 1. Overview / Vision

VartaChat is an open-source, self-hostable chat platform that enables anyone — individuals, teams, or communities — to host their own real-time messaging system with full control over data and customization.
The long-term vision is to evolve into a modular communication platform supporting both **chat** and **social interactions**, combining simplicity with extensibility.

---

## 👥 2. Target Users

* Developers who want a ready-to-use chat backend.
* Small communities or startups needing private chat solutions.
* Makers building custom products on top of an existing chat foundation.
* Self-hosting and privacy enthusiasts.

---

## 🧩 3. Product Goals (MVP)

* Enable two or more users to chat in real-time.
* Secure authentication system (JWT-based).
* Store message history persistently.
* Simple, modern React-based UI.
* One-command Docker setup for self-hosting.
* Clean documentation for easy setup.

---

## 🚫 4. Non-Goals (MVP)

* No audio/video calls.
* No media/file sharing.
* No mobile app (planned for later).
* No social feed or posts (future addition).

---

## ⚙️ 5. Core Features (MVP Scope)

| Area           | Feature                                    |
| -------------- | ------------------------------------------ |
| Authentication | Register, Login, Logout, JWT tokens        |
| User           | Edit profile, status (online/offline)      |
| Chat           | 1-on-1 real-time messaging                 |
| Storage        | Save messages & chat history in PostgreSQL |
| Frontend       | Basic chat UI (React + WebSocket)          |
| Infrastructure | Docker-based deployment                    |

---

## 🧭 6. Future Roadmap

| Phase | Focus        | Description                      |
| ----- | ------------ | -------------------------------- |
| v1.0  | MVP Chat     | 1-on-1 chat, login, self-hosting |
| v1.1  | Groups       | Group chat, user presence        |
| v1.2  | Media        | Send images/files                |
| v2.0  | Social Layer | Posts, comments, follows         |
| v3.0  | Mobile App   | React Native client              |
| v3.5  | Plugins      | Custom module support            |
| v4.0  | Federation   | Connect multiple servers         |

---

## 🏗️ 7. Tech Stack

| Component  | Tech                    |
| ---------- | ----------------------- |
| Backend    | FastAPI (Python)        |
| Frontend   | React + Tailwind        |
| Database   | PostgreSQL              |
| Realtime   | WebSocket (FastAPI)     |
| Cache      | Redis                   |
| Auth       | JWT (OAuth2)            |
| Deployment | Docker / docker-compose |

---

## 🧠 8. Development Plan

| Milestone | Deliverables                        |
| --------- | ----------------------------------- |
| M1        | Setup backend (FastAPI + DB + Auth) |
| M2        | WebSocket chat implementation       |
| M3        | Frontend integration (React)        |
| M4        | Dockerization & documentation       |
| M5        | Public v1.0 open-source release     |

---

## 🧰 9. Guiding Principles

* Simple setup — one-command deployment.
* Modular and readable code.
* Use open standards (JWT, WebSocket, REST).
* Privacy-first: no hidden telemetry.
* Clear documentation and contribution guidelines.

---

## 🚀 10. Future Expansion Ideas

* Social features (posts, comments, profiles)
* Plugin system for bots/integrations
* Webhooks and API extensions
* Mobile app (React Native)
* Custom themes
* Notifications / push system
* Admin dashboard

---
