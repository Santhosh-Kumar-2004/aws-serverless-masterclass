# 📦 AWS Serverless Requirements Overview

This file provides a short and clear explanation of all dependencies used in this project.  
These libraries are essential for building, running, and deploying **FastAPI** applications on **AWS Lambda** using **Mangum** and related tools.

---

## 🧠 Core Web Frameworks

| Library | Description |
|----------|--------------|
| **fastapi** | Modern, fast (high-performance) web framework for building APIs with Python, based on type hints. |
| **starlette** | Lightweight ASGI framework used internally by FastAPI for routing, middleware, and request handling. |
| **uvicorn[standard]** | ASGI web server used to run FastAPI locally (like running Flask apps with `flask run`). |
| **httptools** | HTTP parser used by Uvicorn to process HTTP requests efficiently. |
| **websockets** | Enables WebSocket connections (real-time communication) in FastAPI apps. |
| **uvloop** | High-performance event loop for asyncio — speeds up FastAPI apps. |

---

## 🧩 AWS Integration

| Library | Description |
|----------|--------------|
| **mangum** | AWS Lambda adapter that allows FastAPI/Starlette apps to run inside AWS Lambda via API Gateway. This is the key library for **serverless deployment**. |
| **python-dotenv** | Loads environment variables from `.env` files (useful for AWS credentials, DB URLs, etc.). |
| **pyyaml** | Handles YAML files (used in AWS configuration or SAM/CDK templates). |

---

## 📬 Networking & Async Handling

| Library | Description |
|----------|--------------|
| **anyio** | Abstraction over async frameworks (asyncio, trio), used by FastAPI for async operations. |
| **httpx** | Modern HTTP client (like `requests`, but async) for making API calls from your Lambda. |
| **httpcore** | Low-level core networking library used by `httpx`. |
| **h11** | Pure-Python HTTP/1.1 protocol library used internally by Starlette and HTTP servers. |
| **sniffio** | Detects which async library (asyncio/trio) is running. Required for async compatibility. |
| **dnspython** | DNS toolkit used internally by libraries like `httpx` for DNS resolution. |

---

## 💾 Data Handling & Serialization

| Library | Description |
|----------|--------------|
| **pydantic** | Data validation and serialization using Python type hints. Core of FastAPI’s request/response models. |
| **pydantic-core** | Internal engine for Pydantic, optimized in Rust for performance. |
| **typing-extensions** | Backports new Python typing features for older versions. |
| **annotated-types** | Supports custom type annotations and metadata for Pydantic validation. |
| **orjson** | Ultra-fast JSON parser (used instead of Python’s default `json` module). |
| **ujson** | Another fast JSON encoder/decoder — sometimes used by FastAPI for response serialization. |

---

## ✉️ Input Validation & Forms

| Library | Description |
|----------|--------------|
| **email-validator** | Validates email addresses in Pydantic models (useful in user signups). |
| **python-multipart** | Handles file uploads and form-data parsing in FastAPI. |

---

## 🧱 CLI & Utilities

| Library | Description |
|----------|--------------|
| **click** | Command-line interface builder used by many tools. |
| **typer** | CLI framework (built by FastAPI creator) used for developer tools like FastAPI CLI. |
| **fastapi-cli** | Command-line utility to manage FastAPI apps (run, create, debug). |
| **shellingham** | Detects the current shell — helps Typer/Click tools behave correctly. |

---

## 🧰 Debugging & Developer Tools

| Library | Description |
|----------|--------------|
| **rich** | Beautiful console output formatting (colors, tables, syntax highlighting). |
| **pygments** | Syntax highlighter used by Rich and FastAPI’s API docs. |
| **markdown-it-py** | Markdown parser — used by FastAPI’s auto-docs (`/docs`). |
| **mdurl** | URL parsing for Markdown links. |
| **jinja2** | Template engine (used for rendering HTML in FastAPI). |
| **markupsafe** | Escapes unsafe characters in HTML templates for security. |
| **watchfiles** | Automatically reloads the app during development when files change (like `npm run dev`). |

---

## 🌍 Certificates & Encoding

| Library | Description |
|----------|--------------|
| **certifi** | Provides trusted root certificates (for HTTPS connections). |
| **idna** | Handles Internationalized Domain Names (Unicode domain names). |

---

## 💬 Summary

This setup allows you to:
- Develop APIs using **FastAPI**
- Run locally using **Uvicorn**
- Deploy seamlessly on **AWS Lambda** using **Mangum**
- Manage configurations and async tasks efficiently
- Validate inputs and output clean JSON responses

---

## ☁️ In Real-Life AWS Use

| Library | AWS Usage Example |
|----------|------------------|
| `fastapi` | Create API endpoints to serve through API Gateway. |
| `mangum` | Connect FastAPI to Lambda’s handler for serverless deployment. |
| `pydantic` | Validate input data in Lambda functions. |
| `python-dotenv` | Load secrets/configs locally (instead of hardcoding). |
| `httpx` | Call external APIs (like AWS Cognito, SNS, etc.) from Lambda. |
| `jinja2` | Render HTML templates in AWS-hosted web apps. |
| `rich` | Print colored debug logs to CloudWatch. |
| `pyyaml` | Parse AWS config files (SAM, CloudFormation). |
| `uvicorn` | Run the same app locally before deploying to Lambda. |

---