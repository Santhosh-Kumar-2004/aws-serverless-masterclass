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