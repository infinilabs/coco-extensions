# Timer

Simple countdown timer with preset durations and custom time input inside Coco AI.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. **Preset Timers**: Quick-start with common durations (1, 5, 10, 15, 25, 30 minutes).
2. **Custom Duration**: Set any time in minutes and seconds.
3. **Visual Progress**: Animated ring shows time remaining.
4. **Audio Alert**: Plays a pleasant chime when timer completes.

## Features

- Clean, minimal interface
- Visual progress ring with color changes (warning at 1 min, danger at 10 sec)
- Start/Pause/Reset controls
- Audio completion notification using Web Audio API
- Dark mode support (follows system preference)
- No external dependencies, works offline

## Use Cases

- Pomodoro technique (25-minute focus sessions)
- Quick reminders
- Cooking timers
- Break reminders
- Meeting timeboxes

## Technical Notes

- Uses `setInterval` for timing (1-second precision)
- SVG ring animation with CSS transitions
- Web Audio API for completion sound (sine wave chord)
- Tabular numeric font for consistent digit width

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
