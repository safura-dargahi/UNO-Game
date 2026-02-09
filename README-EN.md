🎮 UNO Game – Python Implementation

A fully-featured implementation of the UNO card game written in Python, featuring a terminal-based (CLI) engine and an experimental graphical user interface (GUI).
This project focuses on clean architecture, extensibility, and faithful game mechanics.

✨ Features

🎴 Complete UNO game rules

👥 Multiplayer support (Human & Computer players)

🤖 Simple AI for computer turns

🧠 Card stacking support (optional rule)

🎨 Wild card color selection

🖥 Rich terminal UI (powered by rich)

🌐 Experimental GUI (HTML + React)

⚙️ Modular, object-oriented design

🗂 Project Structure
.
├── main.py           # Entry point (CLI game loop)
├── game.py           # Core game logic and rules
├── enums.py          # Game enums (cards, colors, events)
├── exceptions.py     # Custom exception classes
├── uno-gui.html      # Experimental graphical interface (React)
└── README.md

🚀 Getting Started (CLI Version)
Requirements

Python 3.9+

rich library

Install dependencies:

pip install rich


Run the game:

python main.py

🎮 Game Options

Available command-line arguments:

python main.py [OPTIONS]

Option	Description
-C, --cheats	Enable cheat codes (debug & testing)
-D, --debug	Show debug logs
-V, --version	Print version and exit
🧠 Gameplay Highlights

Wildcard & +4 cards trigger color selection

Reverse behaves correctly in both 2-player and multi-player games

Skip / +2 / +4 effects are applied immediately

Optional card stacking rule for similar card types

Computer players automatically choose optimal colors

🖥 GUI Version (Experimental)

The file uno-gui.html contains a standalone React-based GUI version of the game.

How to run:

Simply open the file in a browser:

uno-gui.html


⚠️ Note:
The GUI version is logic-simulated on the client side and is not yet connected to the Python game engine.

🧪 Cheat Codes (CLI)

When cheats are enabled (--cheats), you can execute Python code during your turn using:

#<python-code>


Example:

#game.turn.hand.clear()


Use responsibly — or irresponsibly, for science.

🛠 Design Philosophy

Clear separation of concerns

Strong use of enums for game state

Event-driven game flow

Easy to extend with new rules or UIs

Written to be readable first, clever second

📌 Version

Current version:

ALPHA-2025-06-02

📜 License

This project is intended for educational and experimental purposes.
UNO is a trademark of Mattel — this is a fan-made implementation.

🌱 Future Ideas

Network multiplayer

Unified engine for CLI & GUI

Smarter AI strategies

Persistent game state
