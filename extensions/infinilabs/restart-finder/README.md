# Restart Finder

Restart the macOS Finder application inside Coco AI.

## What it does

Terminates and automatically restarts the Finder process. Useful when:

1. Finder becomes unresponsive or frozen
2. You need to apply certain system changes that require a Finder restart
3. Finder is consuming too many resources
4. Desktop icons stop responding

## How it works

Executes `killall Finder` which terminates the Finder process. macOS automatically restarts Finder immediately after it's terminated, so you'll see a brief flash as Finder relaunches.

## Requirements

- macOS only
- No special permissions required

## Technical Notes

The `killall` command sends a SIGTERM signal to all processes named "Finder". Since Finder is a core system service, launchd automatically restarts it.

## Caution

Any unsaved Finder operations (like file copying in progress) may be interrupted. The command is safe to use but be aware of ongoing file operations.

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
