#  Lost Item Finder Chatbot

A simple Python command-line chatbot that helps you find lost items by asking smart questions and learning from your feedback over time.

---

##  About

Ever forget where you put your keys, phone, or wallet? This chatbot uses a scoring system to predict the most likely location of your lost item based on your habits, the time of day, and what you were doing — and it gets smarter with every use!

---

## Features

-  **Location scoring** — ranks common places based on your answers
-  **Memory system** — learns from past feedback to improve future guesses
-  **Context-aware** — considers time of day and activity
-  **Simple chat interface** — just answer a few quick questions
-  **Debug mode** — shows scores for all locations so you can understand the reasoning

---

##  Locations Covered

| Location | Location |
|----------|----------|
| Bedroom  | Bag      |
| Kitchen  | Table    |
| Hall     | Sofa     |
| Car      | Office   |

---

##  Getting Started

### Prerequisites

- Python 3.x (no external libraries needed)

### Installation

```bash
git clone https://github.com/your-username/lost-item-finder.git
cd lost-item-finder
```

### Run the chatbot

```bash
python lost_item_finder.py
```

---

##  How to Use

1. Run the program
2. Type the item you lost (e.g. `keys`, `phone`, `wallet`)
3. Answer 5 quick questions:
   - Where did you **last use** it?
   - Where do you **usually keep** it?
   - **When** did you last use it? (`morning` / `afternoon` / `night`)
   - What were you **doing**? (`study` / `cooking` / `rest` / `travel` / `work`)
   - How **sure** are you about your answers? (`low` / `medium` / `high`)
4. The bot predicts the most likely location with a confidence level
5. Tell it if it was right — it will remember for next time!
6. Type `exit` anytime to quit

---

##  Example Session

```
Hey! I will help you find your lost item
(Type 'Exit' anytime to stop)

What did you lose? keys
Okay, let's find your keys

Some quick questions...
Where did you last use it? kitchen
Where do you usually keep it? bag
When did you last use it? (morning/afternoon/night) morning
What were you doing? (study/cooking/rest/travel/work) cooking
How sure are you? (low/medium/high) high

Thinking...

I think your item is most likely in: KITCHEN
Confidence: High
Tip: Check carefully around the kitchen

Did you find it there? (yes/no) yes
Nice! I'll remember that for next time
Memory so far: {'kitchen': 1}
```

---

##  How the Scoring Works

Each location gets a score based on your answers:

| Factor | Points |
|--------|--------|
| Last used location match | +6 |
| Usual storage location match | +4 |
| Time-of-day match (e.g. night → bedroom) | +3 |
| Activity match (e.g. cooking → kitchen) | +3 |
| High confidence | +2 |
| Low confidence | -1 |
| Memory from past correct guesses | +n |

The location with the highest score wins!

---

##  Project Structure

```
lost-item-finder/
│
└── lost_item_finder.py   # Main chatbot script
```

---

## 🔮 Future Improvements

- [ ] Save memory data to a file so it persists between sessions
- [ ] Add more locations (e.g. bathroom, garage, garden)
- [ ] Support custom locations entered by the user
- [ ] Add a GUI version using Tkinter or a web app
- [ ] Track multiple items at once

---

##  Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

##  License

This project is open source and available under the [MIT License](LICENSE).

---

##  Author

Made with  — feel free to reach out or star  the repo if it helped you!
