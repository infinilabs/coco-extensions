# Coffee

Prevent your Mac from sleeping, from inside Coco AI.

This is a Coco AI port of the [**Coffee** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/coffee) (MIT licensed). All credit for the original idea, naming and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## Commands

| Command | Action |
| --- | --- |
| **Caffeinate** | Start `caffeinate -dimsu` in the background. |
| **Decaffeinate** | Stop any running `caffeinate` process. |
| **Toggle Caffeinate** | Toggle caffeination on/off. |
| **Caffeinate for 1 Hour** | Caffeinate for exactly 3600 seconds. |
| **Caffeinate for 8 Hours** | Caffeinate for exactly 28800 seconds. |

## Out of scope for this v0 port

The original Raycast extension also ships menu-bar status, scheduled caffeination, "caffeinate while an app is running", `caffeinateUntil`, and AI tools. Those features rely on Raycast-only runtime APIs (menu bar mode, LocalStorage, AI tools) and are deferred for a follow-up Coco `view` extension.

## Credits

- Original author: **mooxl** ([@mooxl on GitHub](https://github.com/mooxl))
- Contributors: bibixx, GastroGeek, pernielsentikaer, oasaleh, xilopaint, ridemountainpig, zakj, Visual-Studio-Coder, Katsuba
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/coffee`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/coffee)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) mooxl and Coffee Raycast extension contributors

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
