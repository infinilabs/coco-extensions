# Single Disk Eject

Safely eject mounted, ejectable disks on macOS from inside Coco AI.

This is a Coco AI port of the [**Single Disk Eject** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/single-disk-eject) (MIT licensed). All credit for the original idea, naming and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

The implementation pattern mirrors the existing [`stevelauc/spotify_controls`](../../stevelauc/spotify_controls) extension in this repository: the command is a thin one-line `osascript` invocation against the macOS `Finder`.

## Commands

| Command | Action |
| --- | --- |
| **Eject All Ejectable Disks** | `tell application "Finder" to eject (every disk whose ejectable is true)` — ejects every mounted volume the system reports as ejectable (USB drives, SD cards, external SSDs, mounted disk images, etc.). Internal disks are skipped. |

## Out of scope for this v0 port

The original Raycast extension is a `<List>`-based picker that lets you choose which single disk to eject, and supports an "Ignored Volumes" preference. That UX requires a Coco `view` extension; this v0 port only ships the no-input "eject everything ejectable" variant that fits the Coco `command` shape.

The upstream extension also targets Windows (using a bundled `eject.ps1` helper). Windows support is not included in this Coco port — the AppleScript implementation is macOS-only.

## Caveats

- macOS will report an error sound if a volume cannot be unmounted (e.g. a file on it is in use). This matches the system's default eject behavior.

## Credits

- Original author: **johndturn** ([@johndturn on GitHub](https://github.com/johndturn))
- Contributors: LostViking09
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/single-disk-eject`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/single-disk-eject)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) johndturn and Single Disk Eject Raycast extension contributors

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
