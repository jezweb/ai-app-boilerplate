# Jezweb AI App Boilerplate

This repository contains a full-stack boilerplate for building modern, AI-powered web applications, designed for rapid development and scalability.

## Tech Stack

- **Backend:** Python, FastAPI, SQLModel, LanceDB
- **Frontend:** Vue.js, Vite, Vuetify, Tailwind CSS, Pinia
- **Authentication:** Clerk
- **File Storage:** Cloudflare R2 (via presigned URLs)
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions
- **Project Management:** Jira Integration via Claude Code Framework

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js (for local frontend development if not using Docker)
- Python (for local backend development if not using Docker)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jezweb/ai-app-boilerplate.git
    cd ai-app-boilerplate
    ```

2.  **Set up environment variables:**
    - Copy `backend/.env.example` to `backend/.env`.
    - Fill in the required values (Clerk keys, R2 credentials, etc.).

3.  **Build and run the application with Docker:**
    ```bash
    docker-compose up --build
    ```

4.  **Access the application:**
    - **Frontend:** [http://localhost:8080](http://localhost:8080)
    - **Backend API Docs (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)

## Development

The Docker Compose setup includes hot-reloading for both the frontend and backend, so changes you make to the source code will be reflected automatically.

- Backend source code is in the `/backend` directory.
- Frontend source code is in the `/frontend` directory.
