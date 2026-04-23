# Lorem Ipsum

Generate placeholder Lorem Ipsum text — paragraphs, sentences, or words — and copy it to the clipboard, all from inside Coco AI.

This is a Coco AI port of the [**Lorem Ipsum** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/lorem-ipsum) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. Lets you pick **paragraphs**, **sentences** or **words** and a count from 1 to 100.
2. Generates placeholder text from the standard ~150-word classical Lorem Ipsum corpus (the same corpus the upstream `lorem-ipsum` npm package uses).
3. Copies the result to the system clipboard with one click.

Random word/sentence/paragraph length distribution is the standard 5–12 words per sentence, 3–6 sentences per paragraph, sampled with `crypto.getRandomValues` when available.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `paragraphs` (no-view, with count argument) | Pick *paragraphs* in the dropdown, set the count |
| `sentences` (no-view, with count argument) | Pick *sentences* in the dropdown, set the count |
| `words` (no-view, with count argument) | Pick *words* in the dropdown, set the count |

## Out of scope for this v0 port

- The upstream `Generate with AI` command (uses Raycast's hosted AI to author topic-specific placeholder text). Not portable to Coco today.
- The upstream **Default Action** preference (Copy / Paste / Paste-and-Copy). The Coco port always copies on click; pasting into the active app is not surfaced as a configurable action.

## Credits

- Original author: **AntonNiklasson** ([@AntonNiklasson on GitHub](https://github.com/AntonNiklasson))
- Contributors: GastroGeek, stelo, enkia, j3lte
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/lorem-ipsum`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/lorem-ipsum)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) AntonNiklasson and Lorem Ipsum Raycast extension contributors

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
