# Color Converter

Convert colors between HEX, RGB, HSL, HSV, and other formats inside Coco AI.

This is a Coco AI port of the **Convert Color** command from the [**Color Picker** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/color-picker) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is a placeholder for this port.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. Parses color input in various formats:
   - **HEX**: `#FF6363`, `#F63`, `#FF6363FF` (with alpha)
   - **RGB**: `rgb(255, 99, 99)`, `rgba(255, 99, 99, 0.5)`
   - **HSL**: `hsl(0, 100%, 69%)`, `hsla(0, 100%, 69%, 0.5)`
2. Shows a **live color preview** swatch.
3. Displays the color in multiple formats:
   - HEX (uppercase and lowercase)
   - RGB and RGBA
   - RGB percentage
   - HSL and HSLA
   - HSV
   - Modern CSS RGB syntax
4. **Click to copy** any format to the clipboard.

## Mapping from the upstream commands

| Upstream Raycast command | Coco view interaction |
| --- | --- |
| `Convert Color` | Enter any color format — all conversions appear instantly |
| Click a format | Click any row to copy that format |

## Out of scope for this v0 port

- **Pick Color** (screen color picker) — requires system-level color picker APIs not available in Coco view extensions.
- **Extract Color from Image** — requires file system access and image processing.
- **Color history/organization** — requires persistent storage.
- **Menu bar access** — not applicable to Coco.
- **OKLCH, LCH, P3 formats** — these advanced color spaces are deferred for simplicity.

## Credits

- Original author: **thomas** ([@thomaslombart on GitHub](https://github.com/thomaslombart))
- Contributors: otakustay, EmersonEmerson, pernielsentikaer, arronhunt, kvdo2, litomore, samuelkraft, ridemountainpig, xilopaint, anwarulislam, yusifaliyevpro
- Upstream source: [`raycast/extensions` › `extensions/color-picker`](https://github.com/raycast/extensions/tree/main/extensions/color-picker)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) thomas (thomaslombart) and Color Picker Raycast extension contributors

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
