# Hide All Apps

Hide all application windows on macOS inside Coco AI.

## What it does

Hides all visible application windows, leaving only the desktop and menu bar visible. Unlike "Show Desktop", hidden apps remain hidden until you click on them in the Dock or use Command+Tab to switch to them.

## How it works

Uses AppleScript to iterate through all visible processes and set their visibility to false:

```applescript
tell application "System Events" to set visible of every process whose visible is true to false
```

## Differences from Show Desktop

| Feature | Hide All Apps | Show Desktop |
|---------|--------------|--------------|
| Windows hidden | Yes | Yes |
| Click desktop restores | No | Yes |
| Apps remain hidden | Yes | No |
| Per-app restore | Yes (click Dock) | No (all at once) |

## Requirements

- macOS only
- Accessibility permissions may be required

## Use Cases

- Clear screen for a presentation
- Quick privacy when someone approaches
- Start fresh without closing apps
- Focus on one app at a time

## Technical Notes

The command uses System Events to modify the `visible` property of all processes. This is equivalent to pressing Command+H on every running application.

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
