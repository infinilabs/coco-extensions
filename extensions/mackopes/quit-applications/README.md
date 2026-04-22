# Quit Applications

Quit running macOS applications from inside Coco AI.

This is a Coco AI port of the [**Quit Applications** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/quit-applications) (MIT licensed). All credit for the original idea, naming and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

The implementation pattern mirrors the existing [`stevelauc/spotify_controls`](../../stevelauc/spotify_controls) extension in this repository: each command is a thin one-line `osascript` invocation against the macOS `System Events` and the target application.

## Commands

| Command | Action |
| --- | --- |
| **Quit Frontmost Application** | Quit the application that is currently in the foreground. |
| **Restart Frontmost Application** | Quit the frontmost application and immediately reactivate it. |
| **Quit All Other Applications** | Quit every other foreground application; Finder is left alone (it would auto-relaunch anyway). |

## Out of scope for this v0 port

The original Raycast extension is a `<List>`-based picker that lets you browse all running applications and pick one (or many) to quit or restart. That UX requires a Coco `view` extension; this v0 port only ships the no-input subset (frontmost, all-other) that fits the Coco `command` shape.

The upstream extension also provides:

- An "Excluded Applications" preference for `Quit All Applications`. Coco does not yet expose extension preferences to `command`-type extensions, so this is deferred to the future `view` port.
- A "Show Quit All Applications Option" preference toggle.
- Quicklink generation (`raycast://...`) for quitting/restarting a specific app from the URL bar.

## Caveats

- "Quit All Other Applications" will also quit the application that triggered Coco (e.g. Coco itself, if Coco is the frontmost app at the time). This matches the upstream behavior, which similarly does not exempt the launcher.
- Apple Events authorization may need to be granted to Coco the first time these commands run. The upstream extension falls back to a `ps` parse when `System Events` is not authorized; that fallback is not replicated here because our subset only targets the frontmost / all-other shapes that intrinsically need `System Events` either way.

## Credits

- Original author: **mackopes** ([@mackopes on GitHub](https://github.com/mackopes))
- Contributors: jrnxf, 3llomi, sxn, yvysunu, ridemountainpig, erayack
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/quit-applications`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/quit-applications)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) mackopes and Quit Applications Raycast extension contributors

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
