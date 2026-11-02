# What Is a Terminal?

*Read this if you've never used one. No experience needed. It takes about five minutes.*

*You'll need the course files, Python and VS Code first (steps 0 to 2 of [SETUP.md](SETUP.md)). Then read this before step 3.*

## The short version

A **terminal** is a window where you control your computer by **typing** instead of clicking.

You type an instruction, press **Enter**, and the computer does it and prints its reply right underneath. That's the whole idea.

You already do the same kinds of things with the mouse: open a folder, look at the files inside, start a program. The terminal lets you do them with words instead. It looks old-fashioned (plain text, no buttons), but nearly every developer uses one every day.

## Why bother with it?

- **It's how Python programs get run.** (VS Code's ▶ button is really just typing the command into a terminal for you.)
- **It's exact and shareable.** "Click the third menu, then the second item" is hard to pass on. "Type this line" can be copied and pasted by anyone, on any computer.
- **Most developer tools are built for it:** Git, `pip`, `pytest` and thousands more.
- **It gets faster than clicking** once you know a handful of commands.

## Words you'll hear

| Word | What it means |
|------|---------------|
| **Terminal** (or **console**) | The window itself: a place to type text and read replies. |
| **Shell** | The program running *inside* the window that understands what you type. On Windows it's usually **PowerShell**. On macOS it's **zsh**, and on Linux **bash**. |
| **Command** | One instruction you type, such as `python --version`. |
| **Command line** | Using commands instead of buttons and menus. |
| **Prompt** | The text just before the blinking cursor. It means "I'm ready for your next command". |
| **Current folder** (or *working directory*) | The folder the terminal is "standing in". Many commands act on whatever is in this folder. |
| **Output** | Whatever the command prints back. |

People use "terminal" and "shell" interchangeably, and that's fine. If it helps: the terminal is the window, and the shell is the translator inside it.

## Open a terminal in VS Code

1. In VS Code, open the course folder with **File → Open Folder…**.
2. Press `` Ctrl+` `` (hold Control and press the backtick key, usually just above `Tab` and left of `1`). You can also use the menu: **Terminal → New Terminal**.
3. A panel opens at the bottom of the window. That's your terminal.

Because you opened the course folder first, the terminal starts *inside* that folder. This matters, as you'll see below.

Click inside the panel before typing, so the keystrokes go to the terminal and not to a file.

## Reading the prompt

Your prompt will look something like one of these:

```text
PS C:\Users\ada\Basic Python Training>          (Windows, PowerShell)
ada@laptop Basic Python Training %              (macOS)
ada@laptop:~/Basic Python Training$             (Linux)
```

It tells you two things:

1. The terminal is **ready** and waiting for you to type.
2. Which **folder** you're in (here, `Basic Python Training`).

Nothing happens until you press **Enter**. If you make a typo, use Backspace and fix it first, just like in a text editor.

> **Windows tip:** if your prompt looks like `C:\Users\ada>` without the `PS` at the start, you're in the older *Command Prompt*. Most commands below still work, but `pwd`, `ls` and `cat` don't. Use `cd` (on its own) to see the folder, `dir` to list files and `type README.md` to show a file. Or open a PowerShell terminal from the **+ ▾** dropdown at the top right of the terminal panel.

## Your first commands

Try these one at a time, pressing Enter after each. They only *look* at things, so you can't break anything.

| What you want | What you type |
|---------------|---------------|
| Where am I? | `pwd` |
| What's in this folder? | `ls` |
| Go into the `lessons` folder | `cd lessons` |
| Go back up one folder | `cd ..` |
| Show what's inside a text file | `cat README.md` |
| Clear the screen | `cls` (Windows) or `clear` (macOS/Linux) |
| Check your Python version | `python --version` |

(`pwd` stands for "print working directory", `ls` for "list", and `cd` for "change directory".)

A suggested warm-up:

```text
pwd
ls
cd lessons
ls
cd ..
```

After `ls` in the course folder you should see names like `README.md`, `lessons` and `tests`. After `cd lessons` and `ls` you'll see the lesson folders. `cd ..` takes you back, so you finish where you started.

## Shortcuts that save a lot of typing

| Shortcut | What it does |
|----------|--------------|
| `Tab` | **Auto-completes** a name. Type `cd les` then press Tab and it fills in `cd lessons`. |
| `↑` (Up arrow) | Brings back the previous command so you can run it again or tweak it. |
| `Ctrl+C` | **Stops** whatever is running. Your emergency brake. |
| Right-click, or `Ctrl+V` (`Cmd+V` on Mac) | Pastes text into the terminal. |

## Running a Python file

This is the command you'll use most:

```bash
python lessons/01_hello_python/examples.py
```

Breaking it down:

- `python` is the program you're starting.
- `lessons/01_hello_python/examples.py` is the **path** to the file you want it to run. It's like an address: "from where I'm standing, go into `lessons`, then `01_hello_python`, and find `examples.py`."

Python prints whatever the file tells it to, right below the command. When it's finished, the **prompt comes back**. That's how you know it's done.

If the program asks a question (with `input()`), it pauses and waits. Click in the terminal, type your answer, and press Enter. If you ever see no prompt and nothing happening, the program is still running or waiting for you. `Ctrl+C` stops it.

Two more things worth knowing:

- Where you're standing matters. The course commands assume your terminal is in the **top course folder** (the one containing `README.md`). Run `pwd` and `ls` if you're not sure.
- On Windows, `/` and `\` both work in the commands in this course.

## Odd things you might see

| What you see | What it means |
|--------------|---------------|
| `(.venv)` at the start of the prompt | The course's *virtual environment* is switched on (see [SETUP.md](SETUP.md)). That's a good sign. |
| The prompt changes to `>>>` | You've started Python's interactive mode, not the shell. Type `exit()` and press Enter to leave. |
| Lots of red text after a command | An error message. It looks scary but it's help: read the **last line** first (see Lesson 1). |

## Is it safe?

For the commands in this course, yes: they look at files or run your own programs.

In general, keep two things in mind:

- **The terminal doesn't ask "are you sure?"** Commands that delete files (`rm`, `del`, `Remove-Item`) act immediately and skip the recycle bin.
- **Only type commands you understand,** or that come from a source you trust, like this course. Don't paste a command from a random website just because it claims to fix something.

Typos are harmless. You'll just get an error message and can try again.

## When things go wrong

| What you see | What to do |
|--------------|------------|
| `'python' is not recognized…` or `command not found` | Python isn't installed, or the terminal can't find it. Follow [SETUP.md](SETUP.md) and open a **new** terminal afterwards. |
| `can't open file … No such file or directory` | You're in the wrong folder, or there's a typo in the path. Run `pwd` and `ls` to see where you are, and use `cd` to move. |
| `ERROR: file or directory not found: tests/…` (from `pytest`) | Same cause: you're not in the top course folder. Use `pwd` to check and `cd` to get there. |
| Nothing happens and there's no prompt | The program is still running or waiting for you. Click in the terminal and try typing, or press `Ctrl+C`. |
| You pasted a command and nothing happened | Press Enter. Pasting only types the text. |
| The screen is full of old output | Run `cls` (Windows) or `clear` (macOS/Linux). |

## Quick check

1. What's the difference between the terminal and the shell?
2. What two things does the prompt tell you?
3. You run `python lessons/01_hello_python/examples.py` and get "No such file or directory". Which two commands do you try first?

<details>
<summary>Answers</summary>

1. The terminal is the window you type in. The shell is the program inside it that understands your commands.
2. That the terminal is ready for a command, and which folder you're currently in.
3. `pwd` (to see which folder you're in) and `ls` (to see whether `lessons` is in it). If you're in the wrong place, use `cd` to get to the course folder.

</details>

Ready? Continue with step 3 of [SETUP.md](SETUP.md) to set up your environment, then start [Lesson 1](lessons/01_hello_python/README.md).
