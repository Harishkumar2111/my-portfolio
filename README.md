# Harish K. M — Professional Portfolio Website

A modern, high-performance, fully responsive personal portfolio website engineered for **Harish K. M** — final-year B.Sc. Artificial Intelligence and Machine Learning student at Annai College of Arts and Science (Bharathidasan University) and MCA aspirant.

All data, career objectives, educational qualifications, coursework, technical skills, internship experience, certifications, and contact channels are strictly derived from the official candidate resume (**`Harish Kumar.pdf`**).

---

## 🌟 Key Highlights & Features

1. **Aesthetic & Modern Theme:**
   - Dark Navy, Slate, Black, White, and Blue/Cyan accents.
   - Glassmorphic translucent cards with backdrop-blur, subtle borders, and smooth shadows.
   - Responsive typography using **Outfit**, **Plus Jakarta Sans**, and **JetBrains Mono**.

2. **Sections Included:**
   - **Hero / Home:** Professional introduction, active status badge (*Available for Entry-Level AI/ML & Python roles*), quick info tags, social links, and dual-action buttons.
   - **About Me:** Academic and professional narrative, soft skills badges (*Quick learning, Problem-solving, Communication, Teamwork, Adaptability*), and language proficiencies (*Tamil, English*).
   - **Education:** Chronological timeline showing:
     - MCA — Master of Computer Applications *(Pursuing)* — Annai College of Arts and Science
     - B.Sc. Artificial Intelligence and Machine Learning *(2023–2026)* — Bharathidasan University
     - Higher Secondary — Al Ameen Higher Secondary School, Kumbakonam
   - **Technical Skills & Coursework:** Dynamic interactive category tabs (All, Programming & Tools, ML & Deep Learning, GenAI & Systems):
     - Languages: Python, C, C++, HTML5, CSS3, JavaScript
     - Libraries: NumPy, Pandas, scikit-learn, Matplotlib, Seaborn, TensorFlow, Keras, PyTorch
     - Tools: VS Code, Google Colab, Git, GitHub, Kaggle, MS Office, Excel, Canva
     - Domains: Supervised Learning, Deep Learning, NLP & Computer Vision, LLMs, Transformers, AI Systems, MLOps
   - **Internship Experience:** AI & ML Intern at SwordNex Technologies (June 2026) with detailed technical responsibilities.
   - **Featured Projects:** *Citizen AI — Intelligent Citizen Engagement Platform* with architecture overview, tech stack, and direct GitHub links.
   - **Certifications:** Web Development, Microsoft Excel, Artificial Intelligence, Machine Learning.
   - **Resume Preview & Download:**
     - In-browser interactive PDF viewer (`<object>` / `<iframe>`).
     - Instant high-res image view toggle.
     - Direct PDF download button (`/download-resume`) serving `Harish_Kumar_Resume.pdf`.
     - Fullscreen / Open in New Tab action (`/view-resume`).
   - **Verified Contact Details:**
     - Email: `kumarharish4222@gmail.com` with quick copy button.
     - Phone: `+91 9345768795` with quick copy button.
     - Location: Kumbakonam, Tamil Nadu, India.
     - Verified LinkedIn (`linkedin.com/in/harish-kumar-489768284`) and GitHub (`github.com/Harishkumar2111`).
     - Interactive contact form with Flask backend API (`/api/contact`).

---

## 📁 Project File Structure

```text
My-portfolio/
├── app.py                     # Browser launcher & alternative entry point
├── main.py                    # Main Flask application server & API routes
├── requirements.txt           # Project dependencies (Flask)
├── README.md                  # Comprehensive setup & usage guide
├── messages.json              # Contact form inquiries store
├── .gitignore                 # Git ignore rules (.venv, __pycache__)
├── templates/
│   └── index.html             # Main portfolio HTML template
└── static/
    ├── css/
    │   └── style.css          # Design system, dark theme & responsive layout
    ├── js/
    │   └── script.js          # Interactive UI, tabs, clipboard & contact form
    ├── images/
    │   ├── profile.jpg        # Harish's authentic portrait photo
    │   └── resume-preview.png # High-resolution resume preview
    └── files/
        └── Harish_Kumar_Resume.pdf # Original resume PDF
```

---

## 🚀 Setup & Execution Guide (Windows / VS Code)

### Prerequisites
- Python 3.9 or newer installed on Windows.
- Visual Studio Code (or any terminal).

### Step 1: Open the Project in VS Code
Open VS Code, press `Ctrl + K, Ctrl + O`, and select the project directory:
```powershell
d:\My-portfolio
```

### Step 2: Create a Python Virtual Environment
Open the VS Code integrated terminal (`Ctrl + \`` or `Terminal -> New Terminal`) and run:
```powershell
python -m venv .venv
```

Activate the virtual environment:
```powershell
.venv\Scripts\activate
```
*(You will see `(.venv)` in front of your terminal prompt).*

### Step 3: Install Required Dependencies
Run:
```powershell
python -m pip install -r requirements.txt
```

### Step 4: Run the Application
Start the Flask development server using `main.py`:
```powershell
python main.py
```
*(You can also use `python app.py` — both will start the application seamlessly).*

### Step 5: Access the Website
Open your browser and navigate to:
```text
http://127.0.0.1:5000
```

---

## 🌐 Endpoints Reference

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | Renders the complete responsive portfolio homepage |
| `/download-resume` | `GET` | Securely downloads `Harish_Kumar_Resume.pdf` with attachment headers |
| `/view-resume` | `GET` | Streams `Harish_Kumar_Resume.pdf` inline for browser preview |
| `/api/contact` | `POST` | Validates contact messages and saves them safely to `messages.json` |

---

## 👤 Candidate Details Summary
- **Name:** Harish K. M
- **Location:** Kumbakonam, Tamil Nadu
- **Email:** `kumarharish4222@gmail.com`
- **Phone:** `+91 9345768795`
- **LinkedIn:** [harish-kumar-489768284](https://www.linkedin.com/in/harish-kumar-489768284)
- **GitHub:** [Harishkumar2111](https://github.com/Harishkumar2111)
