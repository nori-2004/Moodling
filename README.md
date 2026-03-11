# 🧠 Moodling — Small Habits, Big Impact

A locally-run web app that predicts your **mood**, **productivity**, and **stress levels** based on daily lifestyle habits, powered by Google's Gemini AI.

![Made for cmd-f Hackathon](https://img.shields.io/badge/Made%20for-cmd--f%20Hackathon-blueviolet)

---

## 💡 Motivation

As students, we often find it challenging to balance our health with the rigorous demands of coursework. Neglecting our body's signals — whether it's skipping sleep, overloading on caffeine, or ignoring stress — can backfire, ultimately impairing our ability to focus and perform at our full potential. By understanding the connection between our habits and mental well-being, we can foster a healthier, more sustainable lifestyle.

---

## 🚀 How It Works

1. **Homepage** — The user lands on a welcoming page and clicks to begin.
2. **Age Form** — The user enters their age, which is stored in `localStorage`.
3. **Slider Pages** — The user moves through four interactive sliders to input:
   - Screen time (hours/day)
   - Sleep duration (hours/night)
   - Exercise time (hours/day)
   - Caffeine intake (cups/day)
4. **Prediction** — On the final slider page, the data is sent to the **FastAPI** backend, which calls the **Gemini AI** model to generate mood, productivity, and stress predictions (scored 1–10).
5. **Results Page** — The predictions are displayed with fun, illustrated flip-card visuals.

---

## 🛠️ Tech Stack

| Layer        | Technology                                                                 |
|--------------|---------------------------------------------------------------------------|
| **Frontend** | HTML, CSS, JavaScript                                                     |
| **Backend**  | Python, [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/) |
| **AI Model** | [Google Gemini API](https://ai.google.dev/) (`gemini-2.0`)               |
| **Data**     | JSON (local file storage via `JsonReader` / `JsonWriter`)                 |
| **Styling**  | Custom CSS, [Google Fonts (Poppins)](https://fonts.google.com/specimen/Poppins) |
| **Design**   | Figma, Photoshop (mockups & illustrations)                                |
| **Testing**  | Python `unittest`                                                         |

### Python Dependencies

| Package                  | Purpose                            |
|--------------------------|------------------------------------|
| `fastapi`                | Web framework for the REST API     |
| `uvicorn`                | ASGI server to run FastAPI         |
| `google-generativeai`    | Google Gemini AI SDK               |
| `python-dotenv`          | Load environment variables from `.env` |
| `pydantic`               | Data validation for API inputs     |

---

## 📂 Project Structure

```
Moodling/
├── main/                        # Backend
│   ├── model.py                 # FastAPI server + Gemini AI integration
│   ├── JsonReader.py            # Reads stored data from data.json
│   ├── JsonWriter.py            # Writes user input to data.json
│   └── __init__.py
├── test/
│   └── test_JsonWriter.py       # Unit tests for JsonWriter
├── ui  homepage/                # Landing page & age form
│   ├── index.html               # Homepage
│   ├── age form.html            # Age input page
│   ├── age.js                   # Age form logic
│   ├── home.js
│   ├── style.css
│   ├── age form style.css
│   └── images/
├── ui slider pages/             # Lifestyle habit input sliders
│   ├── slider.html              # Screen time slider
│   ├── slider2.html             # Sleep slider
│   ├── slider3.html             # Exercise slider
│   ├── slider4.html             # Caffeine slider (sends data to API)
│   ├── blob.js – blob4.js       # Slider logic & API call
│   ├── styles.css
│   └── (images)
├── ui result page/              # Prediction results display
│   ├── results copy.html        # Results page with flip cards
│   ├── script.js                # Reads predictions & updates UI
│   ├── styles.css
│   └── images/
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- **Python 3.9+** installed ([Download](https://www.python.org/downloads/))
- **A Google Gemini API key** ([Get one here](https://aistudio.google.com/app/apikey))
- A modern web browser (Chrome, Edge, Firefox, etc.)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Moodling.git
```


### 2. Set Up Your API Key

Create a file named **`.env`** inside the `main/` folder:

```
Moodling/
└── main/
    └── .env   <-- create this file
```

Open the `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ **Important:** Never commit your `.env` file to version control. Add it to your `.gitignore`:
> ```
> .env
> ```

### 3. Start the Backend Server

```bash
cd main
python model.py
```

The FastAPI server will start at **http://127.0.0.1:8000**.

You can verify it's running by visiting **http://127.0.0.1:8000/docs** in your browser to see the auto-generated API docs.

### 4. Open the Frontend

Open the homepage in your browser:

```
ui  homepage/index.html
```

You can do this by:
- **Double-clicking** `index.html` in File Explorer, **or**
- Using a local dev server like the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) VS Code extension (recommended to avoid CORS issues)

---

## 🔌 API Reference

### `POST /predict`

Predicts mood, productivity, and stress based on user input.

**Request Body:**
```json
{
  "age": 21,
  "caffeine_intake": 2.0,
  "exercise_time": 1.5,
  "sleep_time": 7.0,
  "screen_time": 4.0
}
```

**Response:**
```json
{
  "mood": 7,
  "productivity": 6,
  "stress": 4
}
```

Values are scored **1–10** (1 = lowest, 10 = highest).

---

## 🔒 Environment Variables

| Variable         | Description                     | Required |
|------------------|---------------------------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key      | ✅ Yes   |

---

## 📜 License

This project was built for the **cmd-f Hackathon**. Feel free to use and modify it for personal or educational purposes.
