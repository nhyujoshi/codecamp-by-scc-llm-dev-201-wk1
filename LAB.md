# 🧪 Week 1 Lab — Fundamental Operations in Python
**Mission:** Cover basic ideas in python that covers essential ideas like string manipulation, regular expressions and programmatic looping.
**Mindset:** Ensure that you will be able to write simple functions to perform tasks in these core areas of programming. 
**Time:** ~1 hour
**Deliverables today:** A functional GitHub repository with the intended functions.

---

## What you’ll ship by the end

A working Django project with a structured utilities folder containing your Python problem solutions:

  ```
  codecamp-by-scc-llm-dev-201-wk1/
    ..
    utils/
      lab/
        q1_count_character_frequency.py
        q2_count_word_frequency.py
        ...
  ```

---


## Milestones

### **Milestone A: Core Functionality**
- Each script contains a **function** that solves the assigned problem  
- Django **view imports and runs** these functions  
- Results display clearly on the home page

> You should be able to open a browser page and visually confirm correctness.

---

### **Milestone B: Engineering Improvements**
- Add **edge-case handling** (bad input, empty strings, division by zero, etc.)
- Improve **output messaging**
- Include a short reflection in your submission:
  - What did you struggle with?
  - What tests helped expose bugs?
  - What would you do differently next time?

---

## Learning outcomes (translated to plain English)

* Use Python lists/dicts/sets **idiomatically** (no cleverness for its own sake).
* Apply three evergreen patterns: **two-pointers**, **hash map**, **stack**.
* Explain **Big-O** for each solution—time *and* space—in one sentence.
* Write a small tool (`runner.py`) that loads tests from `problems.json`, calls your functions, and reports truthfully.
* Add **edge-cases** and practice “why did that fail?” debugging.

---

## Act A — Make your machine boring and reliable (≈ 20 mins)

### 1) Open your terminal and install the core tools.

*Why:* The latest stable version of **Python** is required as the base programming language in which these functions will be run. We will also set up **Django**, which is a Python framework, not because we shall immediately start to use it but primarily in order for you to get a feel of what our application at a later stage will look like. Later, we will use **Django** combined with other specific ML related frameworks and library to host our applications and provide meaningful user experience for users to be able to make use of our algorithms.

- **Install Python**

**MacOS**
1. Open browser → go to [Python Official's Download Portal](https://www.python.org/downloads/)
2. Click Download Python 3.x.x for macOS (a yellow button near the top that clearly states that it is the LTS(latest stable version).
3. Open the downloaded .pkg file.
4. Click through installer (keep defaults).
5. After install, open Terminal and run:
```bash
python3 --version
```
You should see something like Python 3.11.6. Please note that if you are unable to see this, please coordinate with one of the faculty members to precisely locate the source of the error. Please **do not** continue if you are not getting this output.

**Ubuntu (Linux)**

1. Open Terminal
2. Check current version:
```bash
python3 --version
```
3. If the version is **3.10+**, you are good to go. *If not, update:* 
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```
4. Verify:
```bash
python3 --version
```

**Windows**

1. Go to [Python's official site](https://www.python.org/downloads/windows/)
2. Click Download **Python 3.x.x (64-bit)**, which is again a button at the very top of the page alongside the Latest Stable Release.
3. Open the installer:
- **Important**: Check the box **Add Python 3.x to PATH** at the bottom.
- Click**Install Now** button.
4.After installing, open the **Command Prompt** or powershell and run:

```bash
python --version
```
or
```bash
py--version
```
You should see Python 3.x.x.

- **Configure pip (Package manager for python)**

The Python package manger will be responsible for handling packages (libraries and frameworks written by other programmers) that will be used in your python applications.

1) **MacOS & Ubuntu (Linux)**

Run:
```bash
python3 -m pip --version
```
You should see a version number.
If you get "No module named pip":

- macOS (using python.org installer). Run:
```bash
python3 -m ensurepip --upgrade
```
- Ubuntu. Install with:
```bash
sudo apt install -y python3-pip
```

2) **Windows**

Run:
```bash
python -m pip --version
```
If that fails, try:
```bash
py -m pip --version
```
If still missing, re-run Python and choose **"Modify" -> Next -> Check** pip.

- **Install a code editor (VS Code Recommended)**

For all OS:
1. Go to [VS code official site](https://code.visualstudio.com/)
2. Download installer for your OS.
3. Installer with defaults.
4. Open VS Code.
5. From the Extensions view, Install:
- **Python** (by Microsoft)
- Optional: **GitLens, Prettier** (helpful but not required)


- **Install Git**

**MacOS**

1. Open `terminal` from your mac and run:
```bash
git --version
```
If git is installed you will see a `git version: 4.x.x` text.

2. If git is not installed, you will see a popup that states:

*“The xcode-select command requires the command line developer tools…”*
Click **Install** and wait.

3. When done, verify again:
```bash
git --version
```

**Ubuntu**

1. Open Terminal.
2. Install Git:
```bash
sudo apt update
sudo apt install -y git
```
3. Verify:
```bash
git --version
```

**Windows**

1. Go to [GitHub's download section](https://git-scm.com/download/win)
2. Download the installer and run it.
3. Accepts the defaults, these will be okay for all the projects that we will do in this course.
- When asked about “Adjusting your PATH environment”, choose **“Git from the command line and also from 3rd-party software”** (default).
4. When done, open **Git Bash** (Installed with Git) or **Command Prompt** and run:
```bash
git --version
```

- **Setting up GitHub Account**

For all the operating systems:
1. Open the browser and go to [GitHub](https://github.com/)
2. Either Sign Up or Login, depending upon if you already have an account.
3. Next up we will configure our name and email address for GitHub. In your bash run (change the email address and name to yours):
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
4. Clone the provided Git Repository in the folder that you set for the project using:
```bash
git clone https://github.com/sammanthp007/codecamp-by-scc-llm-dev-201-wk1
```
**Remember that you must be inside the folder you set in the terminal when you clone**
5. Move into the project that you just cloned using:
```bash
cd codecamp-by-scc-llm-dev-201-wk1
```

- **Creating a Virtual Environment**

Next up, you will create a virtual environment within this project. In short, virtual environment will ensure that all the necessary packages required for the project are managed and up to date. For every project that you will be doing in python, it is always a good idea to set up a virtual environment at the start of the project.

1. Open the project in VScode using:
```bash
code .
```
This opens an instance of VS code in the current folder that you are in. You can access `terminals` from within vs code by going into the `terminal` main option in the top left panel and `new terminal` after.

**MacOS and Ubuntu**
1. Create Venv:
```bash
python3 -m venv venv
```
2. Activate Venv:
```bash
source venv/bin/activate
```
If somehow, you get a ModuleNotFoundError. Use:
```bash
sudo apt install -y python3-venv
python3 -m venv venv
```

**Windows**
1. Create Venv:
```bash
py -m venv venv
```
2. Activate Venv:
```bash
# If in powershell:
venv\Scripts\Activate.ps1

# If in command prompt (cmd)
venv\Scripts\activate.bat
```

- **Install and Run Django server**

`pip install -r requirements.txt`
`python manage.py runserver`

You should see a message saying `Starting development server at http://127.0.0.1:8000/`. Go to `http://127.0.0.1:8000/` to see if the UI is working.

---

### A2) Implement first 3 warm-up questions 

> Think first, code second. Write the story of your approach as comments, then write the code.

Location: `codecamp-by-scc-llm-dev-201-wk1/utils/lab/...`

```python
"""W1D1 Q1 - Count Character Frequency

Count the frequency of each character in a string.

Example:
    >>> q1_count_character_frequency("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""


def q1_count_character_frequency(text):
    """
    Count the frequency of each character in a string.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        dict: A dictionary where keys are characters and values are their frequencies
        
    Example:
        >>> q1_count_character_frequency("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # Your code here
    pass

```

**Feynman nudge:** Before coding, say your idea out loud to a rubber duck (or your classmate). If the duck looks confused, your code will, too.

---

### A3) Add a minimal `problems.json`

Start tiny—one test per function. We’ll expand in Milestone B.

```json
[
  { "func": "reverse_vowels",     "args": ["leetcode"],      "expected": "leotcede" },
  { "func": "two_sum",            "args": [[2,7,11,15], 9],  "expected": [0,1] },
  { "func": "valid_parentheses",  "args": ["([]{})"],        "expected": true }
]
```

**Why JSON tests?** Because tests should be **data**, not code. It keeps the runner small and your thinking visible.

---

### A4) Write `runner.py` (proof over polish)

Your runner should:

1. Load `problems.json` (use Python’s `json` module).
2. Import `solutions.py` dynamically (hint: `import importlib`).
3. For each test: call the function with `*args`, compare to `expected`, and print a **neat table** with pass/fail.
4. Not crash on a failing test—show the error and keep going.
5. Exit with `0` if all pass, else `1` (lets CI catch failures later).

**Example (pseudo-output):**

```
Problem               Result         Expected        Pass?
reverse_vowels        leotcede       leotcede        ✓
two_sum               [0, 1]         [0, 1]          ✓
valid_parentheses     True           True            ✓

3/3 passed
```

**Hint (design principle):** The runner is a **truth machine**, not a judge. It reports; it doesn’t argue.

---

### ✅ Milestone A — Acceptance Criteria

* `solutions.py` contains the 3 functions with docstrings + one-line Big-O.
* `problems.json` loads correctly.
* `runner.py` executes all tests, prints a readable summary, **does not crash** on failure, and returns a meaningful exit code.

---

## Milestone B (Session C, ~2 hours): Edge-cases + hardening

### B1) Add **one edge-case test per function** to `problems.json`

Think like an adversary:

* `reverse_vowels`: `"" → ""`, `"aA" → "Aa"`, strings with **no vowels**, **all vowels**, **mixed case**.
* `two_sum`: `[3,3], 6 → [0,1]` (duplicates), **negative numbers**, **large inputs**.
* `valid_parentheses`: `"(]" → false`, `"" → true`, `"(((((" → false`, `")(" → false`.

> **Why edge-cases?** Because production bugs hide at the edges. Catch them now while it’s cheap.

---

### B2) Polish `runner.py` for clarity

* Print totals (`passed/total`) and a **short failure reason** (e.g., `got=[1,2], expected=[0,1]`).
* Add a developer-friendly `--only func_name` flag to run a single function while debugging.
* Optional nicety: align columns; colorize checkmarks if you like—but keep the code simple.

---

### B3) Add a short note to `README.md`

In 3–5 sentences:

* What failed first?
* What hypothesis did you form?
* What exactly fixed it? (show one line of code or the idea)
* What trade-off did you accept (readability vs micro-optimization)?

> **Why write this?** Writing clarifies thinking. You’ll do the same in Weeks 6–7 when debugging retrieval and RAG.

---

### ✅ Milestone B — Acceptance Criteria

* At least **1 thoughtful edge-case** per function (≥ 6 total tests).
* Runner prints **clear failure messages** and accurate totals.
* `README.md` contains a brief, honest debugging reflection.

---

## Thinking prompts (use them while coding)

* **Two-pointers:** What invariant do the pointers maintain? When do they **both** move?
* **Hash map:** What key do you store? What do you do if the pair uses the same element twice?
* **Stack:** What’s the exact matching rule? What happens on an unexpected close? On leftover opens?

If you can answer those three without peeking, you understand the pattern.

---

## Troubleshooting (cause → fix you can try)

* **ImportError (`solutions` not found):** check the filename and `PYTHONPATH`; prefer relative import via `importlib`.
* **TypeError (args mismatch):** your `args` list in JSON must match the function signature exactly.
* **List vs tuple confusion:** JSON turns everything into lists; compare apples to apples.
* **Unicode / empty strings:** add at least one empty input and one mixed-case input.
* **Two-pointers stuck:** ensure **both** pointers advance on every loop, even when skipping consonants.

---

## Stretch goals (only if you finish early)

* Measure runtime with `time.perf_counter()` and show per-test ms (helps spot O(n²)).
* Add `--fail-fast` to stop on the first failure.
* Add a `tests/` folder with an additional JSON suite (e.g., `tests/edge.json`) and `--suite` flag.

---

## Hand-in checklist (end of Session C)

* `python week1_leet_ladder/runner.py` runs and prints a table.
* `solutions.py` has docstrings + Big-O notes.
* `problems.json` includes edge-cases.
* `README.md` contains your debugging note.

---

## Where this pays off later

* Week 5–6: you’ll adapt this runner style to sanity-check **retrieval snippets** and **budgeted context**.
* Week 7: you’ll test **agent** traces step-by-step.
  Your runner is the habit of truth—quiet, fast, and relentless.
