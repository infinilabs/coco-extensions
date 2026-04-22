# Change Case

Transform a string between **camelCase**, **snake_case**, **CONSTANT_CASE**, **kebab-case**, **PascalCase**, **Title Case**, and 12 more — see all transformations at once and click any row to copy.

This is a Coco AI port of the [**Change Case** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/change-case) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. Accepts text in a textarea (with **Paste from clipboard** and **Clear** buttons).
2. Computes **18 transformations** live as you type and lists them with their names — Camel, Pascal, Snake, Constant, Pascal Snake, Kebab, Kebab Upper, Header, Dot, Path, No, Capital, Sentence, Title, Upper, Lower, Swap, and Sponge case.
3. Click any row to copy that transformation to the clipboard.
4. Toggle **Preserve casing** to control whether the input is lowercased before being split into words (matching the upstream preference of the same name).

All transformations run in pure JavaScript using a hand-rolled word-splitter; no `change-case` npm dependency is bundled.

## Mapping from the upstream

The upstream Raycast extension exposes a single `Change Case` command that opens a list of transformations the user picks from. Each upstream "transformation" is enabled/disabled via a per-transformation preference checkbox; this port shows them all (the upstream defaults).

| Upstream preference | Coco view behaviour |
| --- | --- |
| `preserveCase` | Surfaced as the **Preserve casing** checkbox |
| `source` (Selected vs. Clipboard) | The textarea is the source; **Paste from clipboard** is one click |
| `action` (Copy vs. Paste) | Click a row → copy. Paste-into-active-app is not implemented. |

## Out of scope for this v0 port

- The upstream **`preservePunctuation`** / **`prefixCharacters`** / **`suffixCharacters`** / **`exceptions`** preferences (used by Title and Sentence Case to keep specific words like `iOS`, `macOS` unchanged). Title Case here uses a fixed small list of common stop-words; the rest of the preferences are not surfaced.
- The upstream's per-transformation **enable/disable** preferences. All 18 are always shown.
- The upstream **`popToRoot`** / **`hideHUD`** preferences (Raycast-only UX flags).

## Credits

- Original author: **erics118** ([@erics118 on GitHub](https://github.com/erics118))
- Contributors: pernielsentikaer, nagauta, PWrzesinski, yug2005, ridemountainpig, degouville, xmok, chrismessina
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/change-case`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/change-case)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) erics118 and Change Case Raycast extension contributors

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
