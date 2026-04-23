# Brew

Run the most common no-input Homebrew maintenance commands (update, upgrade, cleanup) from inside Coco AI.

This is a Coco AI port of the [**Brew** Raycast extension](https://github.com/raycast/extensions/tree/main/extensions/brew) (MIT licensed). All credit for the original idea, naming and visual identity goes to the upstream authors. The icon (`assets/icon.png`) is reused unmodified from the upstream extension.

## Prerequisites

Homebrew (`brew`) must be installed and on your PATH. Each command is launched through `zsh -lc` (a login shell) so the standard Homebrew path entries from `~/.zprofile` / `~/.zshrc` are picked up automatically. If your `brew` lives somewhere unusual you may need to add it to your shell init.

## Commands

| Command | Action |
| --- | --- |
| **Brew Update** | `brew update` — refresh the formulae index. |
| **Brew Upgrade** | `brew upgrade` — upgrade every outdated formula and cask. |
| **Brew Cleanup** | `brew cleanup` — remove old downloads and unused versions of installed formulae. |

All three commands are launched detached with `nohup ... &` so they don't block the Coco UI; they will continue running in the background after the command returns. There is no progress UI surfaced to Coco today — open Activity Monitor or `pgrep brew` if you want to confirm completion.

## Out of scope for this v0 port

The upstream Raycast extension is primarily a `<List>`-based browser. The following are deferred to a future Coco `view` port:

- `Search` — interactive search of formulae & casks
- `Show Installed` — browse and uninstall installed packages
- `Show Outdated` — interactive picker for partial upgrades
- Per-formula details panels and cask metadata
- Preferences (custom brew path, terminal app picker, greedy upgrade toggle, zap on uninstall, internal-API toggle, etc.)
- The `Clear Cache` command (operates on Raycast's internal formulae cache and is not relevant in Coco)

## Credits

- Original author: **nhojb** ([@nhojb on GitHub](https://github.com/nhojb))
- Contributors: Aayush9029, mathieudutour, urwrstkn8mare, ashokbaruaakas, millerapps, pernielsentikaer, stelo, vyacheslav, j3lte, alexandercato, ViGeng, ridemountainpig, chrismessina, clins1994
- Upstream source pinned at: [`raycast/extensions@004a0b6` › `extensions/brew`](https://github.com/raycast/extensions/tree/004a0b6b7c846ef7d350217d2c91bc5d34fb265d/extensions/brew)

## License

Upstream is MIT-licensed; that license is preserved for this port:

```
MIT License

Copyright (c) nhojb and Brew Raycast extension contributors

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
