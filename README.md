# Jezweb AI App Boilerplate

This repository contains a full-stack boilerplate for building modern, AI-powered web applications. It's designed to provide a robust, scalable, and highly efficient starting point, integrating best practices for development, containerization, and CI/CD.

The primary goal of this boilerplate is to accelerate the development process by providing a pre-configured, production-ready foundation that is **designed to be manipulated and extended by an AI development assistant like Anthropic's Claude Code.**

## ✨ Key Features

*   **Full-Stack & Modern:** Uses a high-performance Python backend with FastAPI and a reactive Vue.js frontend.
*   **AI-Ready:** Includes LanceDB for vector storage, making it easy to build semantic search and RAG applications.
*   **Containerized Environment:** Fully configured with Docker and Docker Compose for consistent development and production environments.
*   **Optimized Developer Experience:** Features hot-reloading for both frontend and backend, allowing changes to be reflected instantly.
*   **CI/CD Ready:** Includes GitHub Actions workflows for automated testing and build validation.
*   **Scalable Architecture:** Built with a modular structure that can grow with your application's complexity.

## ⚙️ Tech Stack

| Layer | Technology / Service | Role |
| :--- | :--- | :--- |
| **Backend** | Python, FastAPI, SQLModel, LanceDB | Core application logic, structured data, and AI memory. |
| **Frontend** | Vue.js, Vite, Vuetify, Tailwind CSS, Pinia | The interactive and responsive user interface. |
| **Authentication** | Clerk | Secure, pre-built user login and management. |
| **File Storage** | Cloudflare R2 (via presigned URLs) | Scalable object storage for user files. |
| **Containerization** | Docker & Docker Compose | Creates portable and consistent application environments. |
| **CI/CD** | GitHub Actions | Automates testing and build processes. |
| **AI Framework** | **Claude Code Framework** | Provides the "guardrails" and best practices for the AI assistant. |

## 🤖 AI-Driven Development with Claude Code

This boilerplate was designed from the ground up to be used in tandem with an AI development assistant, guided by a set of structured best practices from our companion framework.

This "two-repository" system works as follows:

1.  **This Repository (`ai-app-boilerplate`):** This is the **application skeleton**. It's the tangible code, the file structure, and the running application. This is *what* you build.

2.  **The Framework (`jezweb/claude-code-framework`):** This is the AI's **"operating system" or "brain"**. It contains all the best practices, commands, and workflow definitions (like Jira integration) that instruct the AI on *how* to build.
    *   **Framework Link:** [https://github.com/jezweb/claude-code-framework](https://github.com/jezweb/claude-code-framework)

### Example Workflow

1.  **Clone** this `ai-app-boilerplate` repository to start a new project.
2.  **Provide context** to your Claude Code assistant by giving it the contents of the `jezweb/claude-code-framework` repository (e.g., using a Repomix file).
3.  **Issue a command** defined in the framework, such as instructing it to work on a Jira ticket (e.g., `run_claude.sh`).
4.  **Claude Code will then:**
    *   Read the task requirements.
    *   Consult the best practices in the framework (e.g., `vuejs-best-practices.md`).
    *   Write or modify code *inside this boilerplate* that adheres to those established standards.

This process ensures that AI-generated code is consistent, high-quality, and perfectly aligned with your architecture.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   **Docker & Docker Compose:** Essential for running the containerized application. [Install Docker](https://docs.docker.com/get-docker/).
*   **Node.js & npm:** Required for managing frontend dependencies if you choose to run the frontend locally. [Install Node.js](https://nodejs.org/).
*   **Python:** Required for managing backend dependencies if you choose to run the backend locally. [Install Python](https://www.python.org/downloads/).

### Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jezweb/ai-app-boilerplate.git
    cd ai-app-boilerplate
    ```

2.  **Set up environment variables:**
    The backend requires API keys and configuration to run.
    ```bash
    # Navigate to the backend directory
    cd backend

    # Copy the example .env file
    cp .env.example .env
    ```
    Now, open `backend/.env` and fill in the required values for Clerk, Cloudflare R2, etc.

3.  **Build and run the application with Docker:**
    From the root directory of the project, run:
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images for both the frontend and backend services and start them. The `--build` flag is only necessary the first time or after changing dependencies or Dockerfiles.

4.  **Access the running application:**
    *   **Frontend:** [http://localhost:8080](http://localhost:8080)
    *   **Backend API Docs (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)

## 🛠️ Development Workflow

This boilerplate is configured for a seamless development experience with hot-reloading.

### Docker-Based Development (Recommended)

The `docker-compose.yml` file is configured to use `docker-compose.override.yml` by default for development. This setup provides the best experience:

*   **Backend:** The backend source code (`/backend/app`) is mounted as a volume. `uvicorn` is run with the `--reload` flag, so any changes you make to the Python files will automatically restart the server.
*   **Frontend:** The frontend source code (`/frontend`) is mounted as a volume. The dev container runs the Vite dev server (`npm run dev`), which provides Hot Module Replacement (HMR). Any changes to `.vue` or `.ts` files will be reflected in your browser almost instantly, without a full page reload.

Your main `Dockerfile` for each service is optimized for production, while the `docker-compose.override.yml` points the frontend to use `Dockerfile.dev` for the best development environment.

## 📚 Project Structure

The repository is organized into two main parts: `backend` and `frontend`.

```
.
├── .github/              # GitHub Actions CI/CD workflows
│   └── workflows/
├── backend/              # FastAPI application
│   ├── app/              # Main application source code
│   │   ├── api/          # API endpoint routers
│   │   ├── core/         # Configuration and core logic
│   │   ├── crud/         # CRUD database operations
│   │   ├── db/           # Database session management
│   │   ├── models/       # SQLModel and Pydantic data models
│   │   └── services/     # Business logic services
│   ├── tests/            # Backend tests
│   ├── .env.example      # Example environment variables
│   └── Dockerfile        # Production Dockerfile
├── frontend/             # Vue.js application
│   ├── src/              # Main application source code
│   │   ├── components/   # Reusable UI components
│   │   ├── views/        # Page-level components
│   │   ├── stores/       # Pinia state management stores
│   │   └── router/       # Vue Router configuration
│   ├── Dockerfile        # Production Dockerfile
│   └── Dockerfile.dev    # Development Dockerfile
├── .gitignore
├── docker-compose.yml      # Main Docker Compose configuration
├── docker-compose.override.yml # Development-specific overrides
└── README.md             # This file
```

## 🚀 Next Steps

With the boilerplate running, you can start building your application:
1.  **Define your data models** in `backend/app/models/`.
2.  **Create CRUD operations** for your models in `backend/app/crud/`.
3.  **Expose API endpoints** for your models in `backend/app/api/`.
4.  **Create reusable UI components** in `frontend/src/components/`.
5.  **Build out your application pages** in `frontend/src/views/`.
6.  **Manage shared state** using Pinia stores in `frontend/src/stores/`.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/jezweb/ai-app-boilerplate/issues) if you want to contribute.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
