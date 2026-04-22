# Do Not Disturb

Turn macOS Do Not Disturb on, off, or toggle it from inside Coco AI.

This is a Coco AI port of the [**Do Not Disturb** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/do-not-disturb) (MIT licensed). All credit for the original idea, naming and visual identity goes to the upstream authors. The icon (`assets/icon.png`) and the bundled `assets/DND Raycast.shortcut` file are reused unmodified from the upstream extension.

## How it works

Recent versions of macOS no longer expose a stable public API for setting Do Not Disturb / Focus state. The upstream Raycast extension works around this by shipping a small macOS Shortcut (`DND Raycast`) that flips Focus state on the user's behalf, and then invokes that Shortcut from the command line via `shortcuts run "DND Raycast"`. This Coco port uses the **same** approach with the **same** Shortcut file.

## One-time setup

Before the commands work, you must install the bundled Shortcut **once**:

1. Open `extensions/yakitrak/do-not-disturb/assets/DND Raycast.shortcut` (double-click in Finder, or `open "extensions/yakitrak/do-not-disturb/assets/DND Raycast.shortcut"` in Terminal).
2. The macOS Shortcuts app will open and prompt you to add it. Click **Add Shortcut**.
3. Done — the three Coco commands below will now work.

If you have previously installed and used the upstream Raycast Do Not Disturb extension, the Shortcut is already present (it has the same name) and no extra setup is needed.

## Commands

| Command | Action |
| --- | --- |
| **Turn On Do Not Disturb** | Pipes `on` into `shortcuts run "DND Raycast"`. |
| **Turn Off Do Not Disturb** | Pipes `off` into `shortcuts run "DND Raycast"`. |
| **Toggle Do Not Disturb** | Pipes `status` to detect the current state, then flips it. |

## Out of scope for this v0 port

- The upstream `Status` command shows a HUD with the current state. Coco's `command` shape doesn't surface a return value to the user, so this command is not ported. (`Toggle` already inspects status internally.)
- The upstream's `raycast-cross-extension` callback launches (so other Raycast extensions can chain into DND) are not portable to Coco today.
- The upstream's automatic "first-run installer" flow that opens the `.shortcut` file from inside the extension is not replicated; instead, the install step is done manually once, as documented above.

## Credits

- Original author: **yakitrak** ([@Yakitrak on GitHub](https://github.com/Yakitrak))
- Contributors: leyang, mikikiv, litomore
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/do-not-disturb`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/do-not-disturb)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) yakitrak and Do Not Disturb Raycast extension contributors

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
