# Daily Logs Cleaner

A Python utility that reformats daily log messages copied from Telegram into a cleaner, more readable format. It takes the text from the clipboard and reformats it to the desired format, and puts it back to the clipboard.

## 🎯 Purpose

When copying logs from Telegram, they come in this format:

```
Good Morning I just woke up

07:04 AM
```

This tool automatically reformats them to:

```
07:04 AM - Good Morning I just woke up
```

Making your logs more readable and consistent.

## 📦 Creating an Executable

To create a standalone executable file that doesn't require Python to be installed:

```
poetry run pyinstaller --onefile --noconsole --optimize=2 --clean log_formatter.py
```

This will create a single executable file in the `dist` directory that you can distribute or use on systems without Python.