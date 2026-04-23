# Password Generator

Generate cryptographically-secure random passwords with configurable length and character classes (uppercase, lowercase, digits, symbols), all from inside Coco AI.

This is a Coco AI port of the [**Password Generator** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/password-generator) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. Lets you choose a **length** between 5 and 64 (matching upstream).
2. Lets you toggle the four character classes — **A–Z**, **a–z**, **0–9**, **symbols** (`!@#$%^&*()-_=+[]{};:,.<>/?~`).
3. Always uses `crypto.getRandomValues` for randomness, with rejection sampling so each character is **uniformly** drawn from the pool (no modulo bias).
4. Always guarantees at least one character from each enabled class, then shuffles the result.
5. Shows a strength estimate (`length × log₂(pool size)` bits → Weak / Fair / Strong / Excellent).
6. Copies the password to the clipboard with one click.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `Generate Random Password` (length, case, numbers, special chars) | The whole view |
| `Generate Memorable Password` (word-based, with custom format) | **Not ported** — see below |

## Out of scope for this v0 port

- **Generate Memorable Password** — the upstream "memorable" generator depends on a bundled wordlist and a custom format mini-language; not in scope for a v0 port.
- The upstream **Hide Raycast after copy** / **Remember password length** / **Remember numbers and characters** preferences are stateless (no persistence across runs) — the view starts every session at length 20 with all four classes enabled.

## Credits

- Original author: **joshuaiz** ([@joshuaiz on GitHub](https://github.com/joshuaiz))
- Contributors: teziovsky, pernielsentikaer, hnsn, yusifaliyevpro, xmok
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/password-generator`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/password-generator)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) joshuaiz and Password Generator Raycast extension contributors

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
