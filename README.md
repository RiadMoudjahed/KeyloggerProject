# 𝗞𝗘𝗬𝗟𝗢𝗚𝗚𝗘𝗥 𝗪𝗜𝗧𝗛 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧 𝗔𝗡𝗗 𝗖𝗟𝗜𝗣𝗕𝗢𝗔𝗥𝗗 𝗠𝗢𝗡𝗜𝗧𝗢𝗥𝗜𝗡𝗚

### 𝐃𝐄𝐒𝐂𝐑𝐈𝐏𝐓𝐈𝐎𝐍

This project implements a keylogger with additional monitoring capabilities including automatic screenshot capture and clipboard content monitoring. It's designed as an educational tool to demonstrate how monitoring software works.

### 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒

- Keystroke logging with special key detection (Enter, Backspace, Space)
- Periodic screenshot capture
- Clipboard content monitoring
- Easy termination with ESC key

### 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐌𝐄𝐍𝐓𝐒

- Python 3.6+
- Required libraries:
  - pynput
  - pyperclip
  - pyautogui

### 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍

```bash
pip install pynput pyperclip pyautogui
```

### 𝐔𝐒𝐀𝐆𝐄

To run the keylogger:
```bash
python keylogger.py
```

The program will:
1. Start logging keystrokes to "keys_logged.txt"
2. Capture screenshots every 10 seconds and save as "screenshot.png"
3. Monitor and print clipboard contents every 10 seconds
4. Terminate when ESC key is pressed

### ❗ 𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓 𝐖𝐀𝐑𝐍𝐈𝐍𝐆 ❗

**This software is intended for educational purposes only.** 

Using this software to monitor someone without their knowledge or consent may be illegal in your jurisdiction and violates privacy rights. Always:
- Obtain proper permission before using on any device
- Inform users that their activities are being monitored
- Follow all applicable laws regarding computer monitoring and surveillance

### 𝐂𝐔𝐒𝐓𝐎𝐌𝐈𝐙𝐀𝐓𝐈𝐎𝐍

You can modify the following parameters in the code:
- `log_file` - Change the filename where keystrokes are logged
- Time interval in the main loop - Change how frequently screenshots and clipboard are captured


### ⚠ 𝐃𝐈𝐒𝐂𝐋𝐀𝐈𝐌𝐄𝐑

The author is not responsible for any misuse of this software. This tool should only be used on systems you own or have permission to monitor.

(AI used)
