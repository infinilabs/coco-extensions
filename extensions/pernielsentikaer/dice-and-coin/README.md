# Dice & Coin

Roll dice or flip coins with cryptographically secure randomness inside Coco AI.

This is a Coco AI utility inspired by various Raycast random utilities. Useful for tabletop RPGs, quick decisions, or any situation requiring fair random outcomes.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. **Roll Dice**: Click any standard die type to roll:
   - d4, d6, d8, d10, d12, d20, d100
   - 2d6 (two six-sided dice summed)
2. **Flip Coin**: Get heads or tails with a visual indicator.
3. **History**: Shows the last 8 rolls/flips for reference.
4. **Secure Randomness**: Uses `crypto.getRandomValues()` for cryptographically secure, unbiased results.

## Features

- Large, animated result display
- Quick-access buttons for all standard RPG dice
- Emoji-enhanced coin flip results (👑 for heads, 🌙 for tails)
- Recent history for both dice and coin
- Works offline, no external dependencies

## Technical Notes

The random number generation uses rejection sampling to ensure unbiased results:
- Uses `crypto.getRandomValues()` for cryptographic randomness
- Implements rejection sampling to eliminate modulo bias
- Each outcome has exactly equal probability

## Credits

- Concept inspired by various Raycast random/dice extensions
- Implementation: Coco AI extension contributors

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
