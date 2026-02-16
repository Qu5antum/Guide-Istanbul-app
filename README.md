# Guide-Istanbul 

Guide-Istanbul is a web application designed for people who have just arrived in Istanbul. It helps users discover interesting places such as attractions, restaurants, bazaars, beaches, and more.

The app also includes an AI-powered assistant that can recommend places based on user requests. For example, you can ask:

> "Find me interesting places to hang out"

and the system will suggest restaurants, bars, hotels, and other locations — along with distances calculated from your current position.

Additionally, users can:
- Search for places manually
- Filter locations by category
- Leave comments and reviews

---

## 🚀 Features

- 📍 Discover attractions, restaurants, bazaars, and beaches  
- 🤖 AI assistant for personalized recommendations  
- 🗺️ Distance calculation based on user location  
- 🔎 Filtering and search functionality  
- 💬 Commenting system for locations  

---

## Technologies

- **FastAPI** — backend   
- **JavaScript** — frontend  
- **LangChain** — AI agent integration  
- **PostgreSQL** — Database  
- **JwT** — Authorization

---

## Installation & Setup

Follow these steps to run the project locally:

### Create a virtual environment

```bash
python -m venv venv
```

### Acitvate virtual environment

```bash
./venv/Scripts/activate
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Create .env file in src and add

```bash
SECRET_KEY = "<SECRET_KEY>" 
ALGORITHM = "<ALGORITHM>"  
ACCESS_TOKEN_EXPIRE_MINUTES = <MINUTES> 

URL_DATABASE = "postgresql+asyncpg://postgres:<PASSWORD>@localhost:5432/<APP_NAME>"

AI_API_KEY = "<API_KEY>"
MODEL = "<MODEL>"
```

### Launching the application

```bash
python -m backend.src.main
```