# 🧠 AI Fitness Trainer

An AI-powered full-body workout assistant that leverages **Computer Vision**, **MediaPipe**, and **Flask** to track your exercise postures in real-time. It also includes an interactive **AI FitBot** for personalized fitness advice and a **BMI calculator** to assess your health.

---


## 🧩 Key Features

- 🎯 **Real-time posture detection** using MediaPipe
- 🔁 **Repetition counting** with posture validation
- ⏱️ **Automatic timer** for time-based exercises (e.g., walking)
- 🤖 **AI FitBot** for personalized fitness and diet queries
- 🧮 **BMI Calculator** to assess body composition
- 🌐 Web-based UI powered by **Flask**

---

## 🧠 How It Works

### 📹 Real-Time Exercise Tracker (`main.py` / `main1.py`)
- Uses **MediaPipe Pose** to detect body landmarks from webcam feed.
- Calculates joint angles using OpenCV to verify posture.
- Repetition logic handled based on specific body part movement.
- Supports sequential flow of exercises or single-mode (push-ups, walk, etc.)

> `main.py` – full body with timers  
> `main1.py` – single exercise routine

---

### 🧮 BMI Calculator (in `bmi.html`)
- Accepts **height and weight** from user.
- Calculates **Body Mass Index** and classifies health level:
  - Underweight
  - Normal
  - Overweight
  - Obese

---

### 🤖 AI FitBot (`fit.html`)
- Users can ask fitness-related queries (e.g., "Suggest a diet for muscle gain").
- Powered by **Gemini AI API** for AI chat experience.
- Embedded in an elegant, mobile-responsive UI.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **OpenCV**
- **MediaPipe**
- **Flask**
- **HTML/CSS/JS**
- **Puter.ai API (Chatbot)**

---

## 🚀 Getting Started

### 🔧 Installation
``` 
git clone https://github.com/Abhi0804-M/AI-Fitness-Trainer.git
cd AI_FITNESS_TRAINER
pip install -r requirements.txt
 ```



### 🏃‍♂️ Run the Flask App
```
python app.py
```
Open http://127.0.0.1:5000/ in your browser.

### 🏋️ Supported Exercises
- Exercise	Mode	Description
- Push-ups	Count-based	Detects elbow & shoulder angles
- Sit-ups	Count-based	Tracks torso movement
- Walk	Time-based	2-minute walking timer
- Burpees	Count-based	Full-body transition detection
- Jumping Jacks	Count-based	Arm and leg spread detection
- Squats	Count-based	Knee and hip angles monitored
- Lunges	Count-based	Alternating leg step validation
- Pull-ups	Count-based	Arm pull range
- Leg Raises	Count-based	Hip and leg elevation angle check

### ✅ Example Commands
```
python main.py -t squat
python main1.py -t push-up
```

### 🔮 Future Scope

- 🔊 Voice assistant feedback
- 📈 Dashboard for user progress
- 👥 Multi-user support
- 📱 Mobile app interface

### 🤝 Contributing
- Want to improve this project? Pull requests are welcome. Please fork this repository and open a PR after making necessary changes.

### 🙋 Author
- Developed by ABHILASH M
<img width="1891" height="887" alt="Screenshot 2025-09-03 140900" src="https://github.com/user-attachments/assets/49efe0ea-5f06-4750-9346-efc113c89b5d" />
<img width="1881" height="922" alt="Screenshot 2025-09-03 140929" src="https://github.com/user-attachments/assets/b1794119-307d-42a0-9e1a-24df807da91a" />
<img width="1890" height="919" alt="Screenshot 2025-09-03 141002" src="https://github.com/user-attachments/assets/4e260681-a3a1-4671-94c3-6c57a30c7a9f" />
<img width="1858" height="899" alt="Screenshot 2025-09-03 141016" src="https://github.com/user-attachments/assets/39b688a5-6219-488d-8b0e-e959cfb21fda" />
<img width="1897" height="916" alt="Screenshot 2025-09-03 141043" src="https://github.com/user-attachments/assets/59f0255e-a378-4d3c-a09b-69c384a59c47" />

