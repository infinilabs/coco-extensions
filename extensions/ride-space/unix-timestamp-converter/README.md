# Unix Timestamp Converter

Convert Unix timestamps to readable date/time formats or generate timestamps from human-readable dates inside Coco AI.

This is a Coco AI port of the [**Unix Timestamp Converter** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/unix-timestamp-converter) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is a placeholder for this port.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. **Timestamp → Date/Time**: Enter a Unix timestamp (seconds or milliseconds) and see it converted to:
   - Local date/time (formatted in your locale)
   - ISO 8601 format
   - UTC format
2. **Date/Time → Timestamp**: Pick a date/time and see the corresponding:
   - Unix timestamp in seconds
   - Unix timestamp in milliseconds
3. **"Now" buttons**: Quickly populate either input with the current time.
4. **Click to copy**: Click any result to copy it to the clipboard.

## Auto-detection

The converter automatically detects whether input is in seconds or milliseconds:
- Values > 32503680000 (year 3000 in seconds) are treated as milliseconds
- Smaller values are treated as seconds

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `Convert Timestamp` | Enter timestamp in the top section |
| `Generate Timestamp` | Pick date/time in the bottom section |

## Out of scope for this v0 port

- **Timezone selector** — the upstream supports selecting specific timezones; this port uses your system's local timezone.
- **Multiple format options** — the upstream has configurable output formats; this port shows the most common formats.

## Credits

- Original author: **ride-space** ([@ride-space on GitHub](https://github.com/ride-space))
- Upstream source: [`raycast/extensions` › `extensions/unix-timestamp-converter`](https://github.com/raycast/extensions/tree/main/extensions/unix-timestamp-converter)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) ride-space and Unix Timestamp Converter Raycast extension contributors

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
