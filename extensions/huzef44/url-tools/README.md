# URL Tools

URL-encode or URL-decode strings interactively from inside Coco AI.

This is a Coco AI port of the [**URL Tools** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/url-tools) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. Type or paste text into the input pane.
2. The output pane updates live — if the input contains percent-encoded sequences (`%XX`) it shows the **decoded** form, otherwise it shows the **encoded** form. So one box serves both directions.
3. Switch the dropdown between `encodeURIComponent` (encodes every reserved character) and `encodeURI` (preserves URL-structure characters like `: / ? # &`). Both directions use the matching standard `decodeURIComponent` / `decodeURI`.
4. **Swap** moves the output back into the input, **Clear** wipes both panes, and either **Copy** button copies that pane.

Malformed percent-encoding (e.g. a stray `%`) shows an inline error in the output pane instead of silently failing.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `URL Encode` (no-view, operates on clipboard) | Paste into the input → output shows the encoded form → click Copy |
| `URL Decode` (no-view, operates on clipboard) | Paste an encoded string into the input → output shows the decoded form → click Copy |

## Out of scope for this v0 port

- The upstream commands operate **directly on the clipboard** and replace it in-place (no UI). The Coco port surfaces the same logic interactively; if you want clipboard-only round-trip behaviour, that could be added as a separate `command`-type extension later.

## Credits

- Original author: **huzef44** ([@huzef44 on GitHub](https://github.com/huzef44))
- Contributors: xmok
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/url-tools`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/url-tools)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) huzef44 and URL Tools Raycast extension contributors

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
