# Apple Music

Control the Apple Music app from inside Coco AI.

This is a Coco AI port of the [**Music** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/music) (MIT licensed). All credit for the original idea, naming and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

The implementation pattern mirrors the existing [`stevelauc/spotify_controls`](../../stevelauc/spotify_controls) extension in this repository: each command is a thin one-line `osascript` invocation against the macOS `Music` application.

## Commands

| Command | Action |
| --- | --- |
| **Toggle Play/Pause** | `tell application "Music" to playpause` |
| **Next Track** | `tell application "Music" to next track` |
| **Previous Track** | `tell application "Music" to previous track` |
| **Volume Up** | Increase Apple Music's volume by 10. |
| **Volume Down** | Decrease Apple Music's volume by 10. |
| **Like Current Track** | Set the current track as `favorited`. |
| **Reveal Current Track** | Reveal the current track and bring Apple Music to the front. |

## Out of scope for this v0 port

The original Raycast extension also provides search, library browsing, AirPlay device picking, menu-bar status, AI tools, and `Just Play`. These rely on Raycast-only runtime APIs (`<List>`, AI tools, menu-bar mode, frontmost app integration) and are deferred for a follow-up Coco `view` extension.

## Credits

- Original author: **fedevitaledev** (Raycast Store handle)
- Contributors: peterdev22, danpalmer, itsjustxan, Shpigford, urwrstkn8mare, michalzuch, validate, hrishabhn, bogdan_bucur, xmok, byheaven
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/music`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/music)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) fedevitaledev and Music Raycast extension contributors

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
