# LiuYao Divination System

## Project Overview

This is a graphical user interface (GUI) application based on traditional Chinese LiuYao divination, implemented using Python's built-in **tkinter** library.

The system simulates coin-throwing (complete with animation) to generate a hexagram. It then analyzes the user's question to highlight the most relevant interpretation, covering six aspects: exams, work, love, money, travel, and health.

---

## AI Usage Declaration

In accordance with the University's Academic Integrity Policy, I declare that I used a generative AI tool (Gemini) during the development of this project.

My use of AI was for the following purposes:

* **Code Debugging:** Identifying errors, such as fixing layout issues in `tkinter`.
* **Code Refinement:** Improving code structure, such as implementing the `for` loop for the interpretation display.
* **Documentation:** Assisting with the drafting and translation of the `README.md` files.

All core logic, the implementation of advanced concepts (OOP, data structures), and the final `HEXAGRAMS` dataset were my own work.

---

## IMPORTANT: HOW TO RUN THIS PROJECT

1. **GUI Application**: This program is a GUI application built with tkinter.
2. **Dependencies**: tkinter is a built-in library included with Python 3. You do not need to install any external libraries.
3. **Execution**: As this is a GUI application, it will not run on Ed's environment and must be executed on a local machine.

Please run it from your terminal using Python 3:

```bash
python3 main.py
```

---

## Features

* Full Graphical User Interface (GUI) built with tkinter.
* Dynamic coin-throwing animation ("X / O") for each of the six lines.
* Calculates both the "Original Hexagram" and, if applicable, the "Changed Hexagram".
* Smart Interpretation: Analyzes the user's question for keywords (e.g., "exam", "love").
  * Note: This feature works best with Chinese keywords (e.g., "考试", "感情").
* Targeted Results: Automatically highlights the most relevant category in the final interpretation.
* Bilingual Data: All 64 hexagrams, descriptions, and interpretations are stored in a comprehensive Chinese/English data structure.
  * Note: Users can copy the Chinese hexagram name (e.g., "乾为天") to search online for more detailed classical interpretations.
* Custom Chinese-style color scheme.

---

## Technical Highlights & Advanced Concepts

This project meets the "Advanced Concepts" requirement by implementing:

* **Object-Oriented Programming (OOP)**: The entire application is encapsulated within a single `LiuYaoGUI` class.
* **Event-Driven Programming**: A full GUI built with `tkinter`.
* **Advanced Control Flow**: Use of `lambda` functions and `self.root.after()` with nested functions (`animate`) to create a non-blocking animation.
* **Complex Data Structures**: A large, nested dictionary (`HEXAGRAMS`) to act as the database.
* **Dictionary Comprehensions**: Used to initialize the keyword-matching dictionary.
* **Dynamic Text Styling**: Used `tkinter` text tags (`tag_config`) to color and highlight results.

---

## Author

Jiaxin
