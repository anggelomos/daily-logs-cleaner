#!/usr/bin/env python3
"""
Telegram Log Formatter

This script processes Telegram log messages from the clipboard,
reformats them, and puts the processed text back into the clipboard.

Format changes from:
    Message content
    HH:MM AM/PM
To:
    HH:MM AM/PM - Message content
"""

import re
import pyperclip

def process_log(text: str) -> str:
    """
    Process the log text from Telegram format to the desired format.

    Input format:
        Message content
        HH:MM AM/PM

    Output format:
        HH:MM AM/PM - Message content

    Args:
        text: The input text from clipboard

    Returns:
        Processed text with the format "HH:MM AM/PM - Message content"
    """
    time_pattern = re.compile(r"(\d{1,2}:\d{2}\s?(?:AM|PM))$")
    # Split the text into non-empty lines.
    lines = [line for line in text.strip().splitlines() if line.strip()]
    
    formatted_messages = []
    message_content = ""

    for line in lines:
        match = time_pattern.search(line)
        if match:
            timestamp = match.group(1)
            formatted_messages.append(f"{timestamp} - {message_content}")
            message_content = ""
        else:
            message_content = line
    
    return "\n\n".join(formatted_messages)

def main():
    """
    Main function that:
    1. Gets the text from clipboard
    2. Processes the text
    3. Puts the processed text back to clipboard
    """
    try:
        clipboard_text = pyperclip.paste()

        if not clipboard_text:
            print("Clipboard is empty.")
            return
        
        print(f"Original text:\n\n{clipboard_text}")
        
        processed_text = process_log(clipboard_text)
        
        pyperclip.copy(processed_text)
        
        print(f"\n\nFormatted text:\n\n{processed_text}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return

if __name__ == "__main__":
    main() 