# Pomodoro

Pomodoro timer with focus sessions, short breaks, and long breaks — right inside Coco AI.

This is a Coco AI port of the [**Pomodoro** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/pomodoro) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A self-contained HTML view (no build step, no network calls) that:

1. Provides a **25-minute Focus** timer, a **5-minute Short Break**, and a **15-minute Long Break**.
2. Displays a circular **SVG ring** that depletes as time passes.
3. Tracks completed focus sessions with a row of **four dot indicators** (four sessions = one full Pomodoro cycle).
4. Supports **Start / Pause / Resume / Reset** controls.
5. Shows a toast notification when each session completes.
6. Persists mode (focus / short break / long break) independently; switching modes resets the timer for that mode.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `Start Focus` | Click *Focus* tab → *Start* |
| `Start Short Break` | Click *Short Break* tab → *Start* |
| `Start Long Break` | Click *Long Break* tab → *Start* |

## Out of scope for this v0 port

- **macOS menu-bar indicator** — the upstream uses a Raycast menu-bar extension to show the current timer state. No equivalent in Coco today.
- **macOS system notifications** (`osascript` popups) — deliberately omitted; the in-page toast and ring give visual feedback instead.
- **Sound alerts on completion** — deferred.
- **Configurable durations** — the upstream allows customising focus/break lengths in preferences; the Coco port uses the Pomodoro standard defaults.

## Credits

- Original author: **asubbotin** ([@asubbotin on GitHub](https://github.com/asubbotin))
- Upstream source pinned at: [`raycast/extensions@main` › `extensions/pomodoro`](https://github.com/raycast/extensions/tree/main/extensions/pomodoro)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) asubbotin and Pomodoro Raycast extension contributors

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
