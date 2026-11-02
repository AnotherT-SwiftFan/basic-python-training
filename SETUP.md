# Setting Up Python and VS Code

About 10 minutes. You only do this once.

## 1. Install Python

Get Python **3.10 or newer** from [python.org/downloads](https://www.python.org/downloads/).

- **Windows:** in the installer, tick **"Add python.exe to PATH"** on the first screen, then click *Install Now*.
- **macOS:** the python.org installer works well. (Homebrew's `brew install python` is fine too.)
- **Linux:** Python is usually pre-installed. If not: `sudo apt install python3 python3-venv python3-pip`.

You can check it worked once you've done step 2 and can open VS Code's terminal (never used one? [TERMINAL.md](TERMINAL.md) shows you how). In a **new** terminal, run:

```bash
python --version
```

On macOS and Linux the command is often `python3 --version`. If so, use `python3` wherever this course says `python`. On Windows, `py --version` also works.

## 2. Install VS Code and the Python extension

1. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
2. Open this course folder with **File → Open Folder…**.
3. VS Code will suggest the recommended extensions (the **Python** extension by Microsoft). Click **Install**. If you miss the prompt, open the Extensions view (`Ctrl+Shift+X`) and search for "Python".

## 3. Create a virtual environment

A *virtual environment* is a private folder of Python packages for one project, so projects don't interfere with each other. Open VS Code's terminal (`` Ctrl+` ``) in the course folder. **New to terminals?** Read [TERMINAL.md](TERMINAL.md) first. It explains what the terminal is and how to use it.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

When the environment is active, your terminal prompt starts with `(.venv)`.

## 4. Tell VS Code to use it

1. Press `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS) to open the Command Palette.
2. Type **Python: Select Interpreter** and press Enter.
3. Pick the one that mentions `.venv`.

New terminals you open in VS Code will now activate it automatically. The interpreter is also shown at the bottom right of the window.

## 5. Check everything works

```bash
python lessons/01_hello_python/examples.py
pytest tests/test_01_hello_python.py
```

The first command should print some friendly text. The second should show **failing** tests, which is correct because you haven't done the exercises yet.

## Everyday VS Code skills

### Run a Python file

- Click the **▶ Run Python File** button at the top right of the editor, **or**
- Right-click in the file → **Run Python File in Terminal**, **or**
- In the terminal: `python path/to/file.py`

### Run the exercise tests

- Terminal: `pytest tests/test_03_strings.py` (or just `pytest` for everything), **or**
- Click the **beaker icon** in the left sidebar (Testing), then press ▶ next to a test file or a single test.

### Debug with breakpoints

Debugging lets you pause a program and look inside it. It's far better than guessing.

1. Click in the margin to the left of a line number. A red dot appears. That's a **breakpoint**.
2. Open the Run and Debug view (`Ctrl+Shift+D`) and click **Run and Debug → Python File** (or press `F5`).
3. The program pauses on your red dot. Look at the **Variables** panel to see the current values.
4. Use the toolbar (or keys) to move through the code:
   - `F10` **Step Over**: run this line, move to the next.
   - `F11` **Step Into**: dive into a function call.
   - `Shift+F11` **Step Out**: finish this function.
   - `F5` **Continue**: run until the next breakpoint.

You can also hover over any variable to see its value, and type expressions into the **Debug Console** to try things out.

### Other handy shortcuts

| Action | Shortcut |
|--------|----------|
| Command Palette | `Ctrl+Shift+P` |
| Toggle terminal | `` Ctrl+` `` |
| Preview a Markdown file | `Ctrl+Shift+V` |
| Comment / uncomment lines | `Ctrl+/` |
| Move a line up / down | `Alt+↑` / `Alt+↓` |
| Rename a symbol everywhere | `F2` |
| Go to file | `Ctrl+P` |

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `python` is "not recognized" (Windows) | Re-run the installer and tick **Add python.exe to PATH**, or use `py` instead of `python`. Open a *new* terminal afterwards. |
| `python` opens the Microsoft Store (Windows) | Python isn't installed yet, or the Store shortcut is in the way. Install from python.org, then search Windows for "Manage app execution aliases" and turn off the *python.exe* entries. |
| `Activate.ps1 cannot be loaded because running scripts is disabled` | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again. You can also skip activation and call the tools directly: `.venv\Scripts\python.exe -m pytest`. |
| `pytest` is "not recognized" or `No module named pytest` | The environment isn't active, or the install was skipped. Activate `.venv` and run `pip install -r requirements.txt`. |
| The Testing panel shows no tests | Make sure the `.venv` interpreter is selected (step 4), then run **Python: Configure Tests** from the Command Palette and choose pytest. |
| Red squiggles under `import` lines | VS Code is using the wrong interpreter. Repeat step 4. |
| `ModuleNotFoundError` when running a lesson file | Run the file directly (the ▶ button or `python path/to/file.py`). Don't rename or move lesson files. |
