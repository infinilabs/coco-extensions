# QR Code Generator

Generate a QR code from any text or URL directly inside Coco AI — no internet connection required.

This is a Coco AI port of the [**QR Code Generator** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/qrcode-generator) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A self-contained HTML page (no build step, no remote network calls) that:

1. Encodes any text or URL as a **Byte-mode QR code** (UTF-8 aware).
2. Lets you choose the **error correction level**: L (7%), M (15%), Q (25%), or H (30%).
3. Auto-selects the minimum **QR version** (1–10) that fits the input at the chosen EC level.
4. Renders the result as an inline **SVG** with correct quiet zone.
5. Supports both **light and dark** colour schemes (the SVG uses CSS classes that respond to `prefers-color-scheme`).
6. Lets you **copy the SVG markup** to the clipboard with one click (paste into any SVG-aware editor or browser).
7. The entire QR encoding pipeline (Reed-Solomon error correction, BCH format/version info, masking, penalty scoring) runs **in-browser** via a hand-rolled, dependency-free implementation derived from ISO/IEC 18004:2015.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `Create QR Code` | Type in the text box — the QR code updates live |
| Copy QR to clipboard | *Copy SVG* button |

## Maximum input capacity (version 10)

| EC level | Max bytes |
| --- | --- |
| L | 271 |
| M | 216 |
| Q | 154 |
| H | 122 |

## Out of scope for this v0 port

- **Versions 11–40** — extending to larger versions requires additional EC block tables and alignment pattern data. The current port supports up to version 10 which covers the most common use cases (URLs ≤ ~200 bytes).
- **Numeric / alphanumeric modes** — these would increase capacity for all-digit or uppercase-alphanumeric inputs but are deferred in favour of the simpler, universal Byte mode.
- **Download as PNG** — the Canvas `toDataURL` path is not wired up; copy-as-SVG is the primary export.

## Credits

- Original author: **Kaiyun** ([@Kaiyun on GitHub](https://github.com/Kaiyun))
- Upstream source pinned at: [`raycast/extensions@main` › `extensions/qrcode-generator`](https://github.com/raycast/extensions/tree/main/extensions/qrcode-generator)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) Kaiyun and QR Code Generator Raycast extension contributors

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
