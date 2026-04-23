# Regex Tester

Test regular expressions against text with live highlighting of matches inside Coco AI.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. **Live Testing**: Type a regex pattern and see matches highlighted instantly.
2. **Flag Support**: Full support for JavaScript regex flags (g, i, m, s, u).
3. **Match Groups**: View captured groups for each match.
4. **Error Feedback**: Shows syntax errors in real-time.

## Features

- Real-time match highlighting as you type
- Match count and group count statistics
- Detailed match breakdown with group values
- Visual error indicators for invalid patterns
- Dark mode support (follows system preference)
- No external dependencies, works offline

## Supported Flags

| Flag | Name | Description |
|------|------|-------------|
| `g` | Global | Find all matches, not just the first |
| `i` | Ignore Case | Case-insensitive matching |
| `m` | Multiline | `^` and `$` match line boundaries |
| `s` | DotAll | `.` matches newlines |
| `u` | Unicode | Enable full Unicode support |

## Use Cases

- Test and debug regular expressions
- Learn regex by experimenting
- Extract patterns from text
- Validate regex syntax before using in code

## Technical Notes

- Uses JavaScript's native `RegExp` engine
- HTML-escapes output to prevent XSS
- Implements debouncing for smooth performance
- Handles edge cases like zero-length matches

## License

MIT License

```
MIT License

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
