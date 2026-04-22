# IP Address

Copy your primary local IP address to the clipboard from inside Coco AI.

This is a Coco AI port of the [**IP Address** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/ip-address) (MIT licensed). All credit for the original idea, naming, and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## What it does

A single `command`-type extension that resolves the primary local IP address (Wi-Fi `en0`, then `en1`, then the first non-loopback interface) and copies it silently to the macOS clipboard via `pbcopy`.

## Mapping from the upstream commands

| Upstream Raycast command | Coco command |
| --- | --- |
| Copy Local IPv4 Address | Run the command — IP is copied to clipboard |

## Platform

macOS only (uses `ipconfig getifaddr` / `ifconfig` + `pbcopy`).

## Out of scope for this v0 port

- **IPv6 addresses** — the upstream also lists IPv6; this port focuses on the primary IPv4 address.
- **Public IP address** — requires an outbound HTTP call to an IP-echo service; intentionally omitted to keep the extension offline.
- **Multiple interface list** — upstream shows all network interfaces as a list; the Coco `command` shape copies a single value.

## Credits

- Original author: **thomas** ([@thomaslombart on GitHub](https://github.com/thomaslombart))
- Upstream source pinned at: [`raycast/extensions@main` › `extensions/ip-address`](https://github.com/raycast/extensions/tree/main/extensions/ip-address)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) thomas (thomaslombart) and IP Address Raycast extension contributors

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
