# UUID Generator

Generate one or more UUIDs (v4 or v7) and copy them to the clipboard from inside Coco AI.

This is a Coco AI port of the [**UUID Generator** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/uuid-generator) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. Lets you pick **UUID v4** (random) or **UUID v7** (time-ordered, RFC 9562 §5.7).
2. Lets you set a count from 1 to 500 and toggle uppercase output.
3. Generates UUIDs as a newline-separated list and copies them with one click.
4. Uses `crypto.randomUUID()` when available (browser-native v4); falls back to a 16-byte `crypto.getRandomValues` implementation otherwise. v7 always uses a small inline RFC-9562 implementation.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `Generate UUIDs` (v4) | Pick *v4* in the dropdown |
| `Generate V7 UUIDs` | Pick *v7* in the dropdown |
| `Uppercase Letters` preference | Uppercase checkbox |

## Out of scope for this v0 port

- **`Generate V5 UUIDs`** — needs a configurable namespace + name and a SHA-1 implementation. Not portable inline without bringing in a UUID library; deferred.
- **`Generate ULIDs`** — different identifier format with its own Crockford-Base32 alphabet; deferred.
- **`Generate TypeIDs`** / **`Parse TypeIDs`** / **`Pack TypeID`** — depend on the `typeid-js` library and a prefix UX. Deferred.
- **`Format UUID`** — converts dash-less hex into canonical form. Trivial, but it needs an input field that the upstream Raycast `arguments` UI gave for free.
- **`View History`** — would require persistence across sessions.
- The upstream **Default Action** preference (Copy / Paste). The Coco port always copies on click.

## Credits

- Original author: **jmaeso** ([@jmaeso on GitHub](https://github.com/jmaeso))
- Contributors: GastroGeek, pernielsentikaer, LunaticMuch, hmarr, harsh_khandelwal, lukas-runge, ridemountainpig
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/uuid-generator`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/uuid-generator)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) jmaeso and UUID Generator Raycast extension contributors

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
