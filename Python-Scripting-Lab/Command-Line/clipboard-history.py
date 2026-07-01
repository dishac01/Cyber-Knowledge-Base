import pyperclip
import time

print("Clipboard Recorder Started...")
print("Press Ctrl+C to stop.\n")

last_text = ""

try:

    while True:

        current_text = pyperclip.paste()

        if current_text != last_text:

            with open(
                "clipboard_history.txt",
                "a",
                encoding="utf-8"
            ) as file:

                file.write(current_text + "\n")
                file.write("-" * 40 + "\n")

            print("Copied:")
            print(current_text)
            print()

            last_text = current_text

        time.sleep(1)

except KeyboardInterrupt:

    print("\nClipboard Recorder Stopped.")
