# 🐱 Profile API – FastAPI (MVC + Redis Rate Limiting)

## 📘 Overview
This is a simple but professionally structured **FastAPI** RESTful API built using the **MVC (Model–View–Controller)** pattern.  
It exposes a single endpoint `/me` that returns static profile information and a **dynamic cat fact** fetched from an external API.  

Additionally, the API implements **rate limiting** using **Redis** to prevent abuse and ensure fair use.

---

## 🚀 Features
✅ RESTful `GET /me` endpoint  
✅ Dynamic data from [Cat Facts API](https://catfact.ninja/fact)  
✅ Real-time UTC timestamp in **ISO 8601 (Z-suffix)** format  
✅ Graceful error handling and logging  
✅ Redis-powered rate limiting (no Docker required)  
✅ CORS enabled  
✅ Modular MVC architecture for scalability  
✅ Fully testable with `pytest`

---

## 🏗️ Project Structure
```
📦 HNG13-STGE0
├── api/
│   ├── __init__.py
│   ├── controllers/
│   │   └── profile_controller.py
│   ├── services/
│   │   └── cat_service.py
│   ├── routes_profile.py
│
├── main.py
├── tests/
│   └── test_me_endpoint.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack
| Component | Technology |
|------------|-------------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Rate Limiting** | Redis + fastapi-limiter |
| **HTTP Client** | httpx |
| **Testing** | pytest, httpx.AsyncClient |
| **Logging** | Python `logging` |
| **Format** | JSON (application/json) |

---

## 📡 API Endpoint Documentation

### **GET** `/me`
Returns your profile information along with a random cat fact.

#### ✅ Example Request
```bash
GET /me
```

#### ✅ Example Response
```json
{
  "status": "success",
  "user": {
    "email": "abdulnurakani@gmail.com",
    "name": "Abdulaziz Nura Kani",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-15T12:34:56.789Z",
  "fact": "Cats sleep 70% of their lives."
}
```

---

## ⏱️ Rate Limiting
Implemented using **Redis** and **fastapi-limiter**.  
Default setting allows **5 requests per minute per IP**.

You can modify limits in your route:
```python
@app.get("/", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
```

---

## 🧩 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Dan-Gaya/HNG13-STAGE0.git
cd HNG13-STGE0
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv .project
.project\Scripts\activate
# OR
source .project/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start Redis (Locally)
Install Redis on your system and run:
```bash
redis-server
```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

Visit:
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Endpoint: [http://127.0.0.1:8000/me](http://127.0.0.1:8000/me)

---

## 🧪 Running Tests
```bash
pytest -v
```

---

## 📦 Dependencies (requirements.txt)
```
fastapi
uvicorn
httpx
redis
fastapi-limiter
pytest
pytest-asyncio
```

---

## 👨‍💻 Author
**Abdulaziz Nura Kani**  
📧 Email: abdulnurakani@example.com  
💼 Stack: Python / FastAPI  
🌐 GitHub: [@Dan-Gaya](https://github.com/Dan-Gaya)

---

## 🏁 License
Licensed under the **MIT License**.
