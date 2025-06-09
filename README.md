An interactive chatbot interface for users to explore products in a simulated e-commerce environment. Built with Flask (Python backend) and vanilla HTML/CSS/JavaScript (frontend), this chatbot enables users to view product details, initiate new chat sessions, and review previous conversations — all stored locally.
Features
Login authentication using localStorage
Chatbot interface with smart responses
“New Chat” button to start fresh conversations
Auto-saved chat history (session-based)
Product listing with dynamic responses
100+ mock products generated with Faker
RESTful API using Flask backend
Responsive and clean frontend design


Tech Stack
| Layer       | Technology           |
|-------------|----------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Python, Flask         |
| Database    | SQLite via SQLAlchemy |
| Mock Data   | Faker (Python)        |
| API Format  | JSON (REST API)       |


Assignment Scope
This project was developed as part of the Uplyft Full Stack Intern Case Study , with focus on: Chatbot product query simulation, Full-stack integration with backend API, UI/UX considerations and chat persistence and Code organization and clean architecture



Project Structure

```bash
uplyft-sales-chatbot/
│
├── backend/
│   ├── app.py                  # Flask backend API
│   ├── products.db             # SQLite database
│   └── venv/                   # Virtual environment (optional)
│
├── frontend/
│   └── index.html              # Full UI with chat logic and history
│
├── README.md                   # You are here
└── requirements.txt            # Python dependencies (Flask, Flask-Cors, SQLAlchemy, Faker)

