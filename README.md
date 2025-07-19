
# MeowShell

MeowShell is a cat-themed command-line interface where all commands purr, hiss, or meow their way through your terminal. Each command mimics a real shell command, but wrapped in cat behavior, strange ASCII art, and utter nonsense.

Because why not?

---

## Features

- Cat equivalents of common shell commands  
- Full-size ASCII cats with every action  
- Completely unnecessary chaos mode  
- Whimsical, absurd, and terminal-breaking

---

## Installation Instructions (Windows)

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/aditi-pai04/Meowshell.git
cd meowshell
```

---

### 2. Add MeowShell to System PATH

To make `meow` available globally:

1. Find the **full path** to the `meowshell` folder (e.g. `C:\Users\YourName\meowshell`)
2. Open the **Start Menu**, search for **"Environment Variables"** and click **"Edit environment variables for your account"**
3. Under **User variables**, select the `Path` variable and click **Edit**
4. Click **New**, then paste the folder path (not the Python file itself)
5. Click **OK** to close all dialogs

---

### 3. Rename the Python File (Optional but Recommended)

Rename `meowshell.py` to `meow` (no `.py`) so you can run it just by typing `meow`.

Your folder should look like:

```
meowshell/
├── meow         ← (this is the renamed Python script)
└── README.md
```

---

### 4. Install Python Dependencies

Install required Python packages:

```bash
pip install click rich
```

---

### 5. Test It Works

Open a new terminal window and run:

```bash
meow --help
```

If you see the help message with all available commands, you're ready.

---

## Usage

Here are some commands you can try:

```bash
meow sniff                 # List files (like ls)
meow nest fluffball       # Make a folder (like mkdir)
meow slink fluffball      # Change into a folder (like cd)
meow pawpoke toy.txt      # Touch a file (create empty file)
meow judge toy.txt        # Judge a file's name emotionally
meow yowl "Feed me now"   # Print a loud, angry message
meow summon               # Display multiple cat ASCII artworks
meow chaos                # Chaos mode: cats everywhere
meow nap                  # Exit
```

---

## Commands

| Command       | Linux Equivalent | Description                              |
|---------------|------------------|------------------------------------------|
| `sniff`       | `ls`             | List files in current directory          |
| `nest`        | `mkdir`          | Create a new folder                      |
| `slink`       | `cd`             | Change into a folder                     |
| `pawpoke`     | `touch`          | Create an empty file                     |
| `yowl`        | `echo`           | Print a loud message                     |
| `judge`       | —                | Emotionally judge a file by its name     |
| `summon`      | —                | Display multiple cat ASCII artworks      |
| `chaos`       | —                | Flood the terminal with cat nonsense     |
| `nap`         | `exit`           | Exit MeowShell                           |

More are being added soon, like:

- `pounce` (delete a file)
- `drag` (move a file)
- `clonecat` (copy a file)
- `hiss` (search for text)

---

## Contributing

Want to add more nonsense? Feel free to fork, extend, and submit a PR. Requirements: the feature must either be utterly useless, absolutely adorable, or terminal-breaking in a cute way.

---

## License

MIT License. Do what you want.

---

## Credits

ASCII art collected from the wild depths of the internet. If a cat drawing is yours and you’d like it credited, let us know.

---

## This tool is useless. Please enjoy it anyway.
