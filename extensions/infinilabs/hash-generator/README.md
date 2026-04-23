# Hash Generator

Generate MD5, SHA-1, SHA-256, and SHA-512 hashes from text input inside Coco AI.

## What it does

A single self-contained HTML page (no build step, no remote network calls) that:

1. **Real-time Hashing**: Type or paste text and see all hash outputs update instantly.
2. **Multiple Algorithms**: Supports MD5, SHA-1, SHA-256, and SHA-512.
3. **Copy to Clipboard**: One-click copy for any hash value.
4. **Privacy First**: All computation happens locally in your browser.

## Features

- Live hash generation as you type
- Web Crypto API for SHA family (cryptographically secure)
- Pure JavaScript MD5 implementation
- Dark mode support (follows system preference)
- Copy to clipboard with visual feedback
- No external dependencies, works offline

## Technical Notes

- SHA-1, SHA-256, and SHA-512 use the Web Crypto API (`crypto.subtle.digest`)
- MD5 uses a pure JavaScript implementation (Web Crypto doesn't support MD5)
- All text is encoded as UTF-8 before hashing
- Output is lowercase hexadecimal

## Use Cases

- Verify file integrity by comparing hashes
- Generate checksums for passwords or tokens
- Quick hash lookups for development
- Learning and comparing hash algorithms

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
