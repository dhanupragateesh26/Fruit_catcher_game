# 🍎 Fruit Catcher 2.0

A **2D arcade-style fruit catching game** built using **Python, Pygame, and Tkinter**.

The player controls a **basket** and catches falling fruits to gain points while **avoiding bombs** that reduce the score.
The game features **multiple levels, increasing difficulty, floating score animations, sound effects, and persistent high score storage**.

---

## 🎮 Features

* Basket movement using keyboard controls
* Multiple fruits with scoring system
* Bombs that reduce score
* Floating score animation when objects are caught
* Persistent high score stored in a file
* Level-based gameplay
* Increasing difficulty with faster falling objects
* Start menu built using Tkinter
* Sound effects for scoring and mistakes

---

## 🛠 Technologies Used

* Python
* Pygame
* Tkinter
* Random module
* OS module

---

## 📂 Project Structure

```
fruit-catcher/
│
├── main.py
│
├── assets/
│   ├── images/
│   │   ├── apple1.png
│   │   ├── mango.png
│   │   ├── grape.jpg
│   │   ├── bomb.png
│   │   ├── basket.png
│   │   └── background images
│   │
│   ├── sounds/
│   │   ├── point1.mp3
│   │   └── error.mp3
│   │
│   └── fonts/
│       ├── venite.ttf
│       ├── knight.otf
│       ├── egmont.ttf
│       └── digi.ttf
│
├── high_score.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```
git clone https://github.com/yourusername/fruit-catcher.git
cd fruit-catcher
```

### Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Game

```
python main.py
```

A start window will appear showing the **current high score**.
Press **START** to begin the game.

---

## 🎮 Controls

| Key          | Action            |
| ------------ | ----------------- |
| Left Arrow   | Move basket left  |
| Right Arrow  | Move basket right |
| Space        | Start the game    |
| Close window | Exit game         |

---

## 🧠 Game Logic

* Fruits and bombs fall from the top of the screen randomly.
* Catch fruits to increase score.
* Catching bombs reduces score.
* Catching too many bombs ends the game.
* Difficulty increases with levels by increasing falling speed and bomb frequency.

---

## 💾 High Score System

The game stores the highest score in:

```
high_score.txt
```

When the game starts, the file is read and the high score is displayed on the start screen.

---

## 🚀 Future Improvements

* Add leaderboard system
* Add more levels
* Add background music
* Add power-ups
* Improve UI animations
* Add controller support

---

## 👨‍💻 Author

Dhanu Pragateesh
Chennai, India
