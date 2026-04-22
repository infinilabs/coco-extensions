# System Monitor

Capture CPU, memory, or disk-usage snapshots from macOS and copy them to the clipboard, directly from Coco AI.

This is a Coco AI port of the [**System Monitor** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/system-monitor) (MIT licensed). All credit for the original idea, naming and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## Approach

The upstream Raycast extension is a rich, real-time `<List>`-based dashboard with sub-views for CPU, memory, network, power, and temperature, plus a menu-bar variant. None of those surfaces map cleanly to Coco's `command` shape today.

This v0 port instead exposes the simplest useful shell-pipeline-based subset: each command samples one subsystem with a built-in macOS utility and pipes the human-readable output into `pbcopy`, so you can paste a one-shot snapshot anywhere (chat, ticket, note, etc.).

## Commands

| Command | Underlying pipeline |
| --- | --- |
| **Copy CPU Snapshot** | `top -l 1 -n 0 -s 0 \| grep -E '^(CPU usage\|Load Avg)' \| pbcopy` |
| **Copy Memory Snapshot** | `top -l 1 -n 0 -s 0 \| grep -E '^PhysMem'; vm_stat \| pbcopy` |
| **Copy Disk Snapshot** | `df -h -t nodevfs,nodevtmpfs,noautofs \| pbcopy` |

## Out of scope for this v0 port

- The full live `<List>` dashboard with tabbed CPU / Memory / Power / Network / SystemInfo views.
- The menu-bar variant (Coco has no menu-bar surface today).
- Network-throughput sampling and the per-process top-talkers list (these need long-running sampling, not a one-shot pipe).
- Power / battery readouts (would need `pmset -g batt` parsing — feasible in a follow-up).
- CPU temperature readouts (upstream ships a clang-built `temperature-reader` Mach helper; not portable as a pure shell wrapper).
- All upstream preferences (default tab, free-vs-used display modes, custom menubar formatting, custom icon URL).

## Credits

- Original author: **hossammourad** ([@hossammourad on GitHub](https://github.com/hossammourad))
- Contributors: crehan144, pernielsentikaer, lucasmezencio, ridemountainpig, xmok, jadenmajid, ADCAdams
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/system-monitor`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/system-monitor)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) hossammourad and System Monitor Raycast extension contributors

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
