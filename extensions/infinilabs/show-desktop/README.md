# Show Desktop

Show the desktop by hiding all windows inside Coco AI (macOS only).

## What it does

A simple command that triggers the macOS "Show Desktop" function:

1. **First run**: Hides all windows to reveal the desktop.
2. **Run again**: Restores all windows to their previous positions.

## How it works

Uses AppleScript to simulate the keyboard shortcut Command+F3 (Fn+F11 on some keyboards), which is the macOS system shortcut for "Show Desktop".

## Requirements

- macOS only
- System Events access (may require Accessibility permissions)

## Technical Notes

The command executes:
```applescript
tell application "System Events" to key code 103 using {command down, fn down}
```

Key code 103 corresponds to F11, and combined with Command and Fn modifiers, this triggers the Show Desktop action.

## License

MIT License

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
