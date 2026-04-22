# Word Count

Count characters, words, sentences, and paragraphs in any text from inside Coco AI.

This is a Coco AI port of the [**Word Count** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/word-count) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is a placeholder for this port.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. Provides a text input area for typing or pasting content.
2. Displays real-time counts for **words**, **characters**, **sentences**, and **paragraphs**.
3. Shows an **estimated reading time** based on average reading speed (200 words/minute).
4. Supports paste from clipboard and clear functionality.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `Count` (main view) | Type or paste text — stats update live |
| Word/character/sentence/paragraph counts | Displayed in the stats grid |

## Out of scope for this v0 port

- **Count from Screenshot** — requires OCR capabilities not available in Coco view extensions.
- **Word Count Overlay** — requires always-on-top window capabilities.

## Credits

- Original author: **itsmingjie** ([@itsmingjie on GitHub](https://github.com/itsmingjie))
- Contributors: koayon, chrismessina, litomore, aryan_thatte, danulqua
- Upstream source: [`raycast/extensions` › `extensions/word-count`](https://github.com/raycast/extensions/tree/main/extensions/word-count)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) itsmingjie and Word Count Raycast extension contributors

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
