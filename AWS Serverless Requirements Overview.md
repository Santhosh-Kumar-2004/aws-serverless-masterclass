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