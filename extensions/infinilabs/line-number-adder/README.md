# Line Number Adder

Add or remove line numbers from text.

## Features

- **Add line numbers** - Prefix each line with a number
- **Remove line numbers** - Strip existing numbers
- **Custom separator** - ". ", ": ", ") ", etc.
- **Padding** - Align numbers with leading spaces
- **Skip empty lines** - Optionally skip blank lines

## Options

| Option | Description |
|--------|-------------|
| Start | Starting line number (default: 1) |
| Separator | Text between number and content |
| Pad Numbers | Add leading spaces for alignment |
| Skip Empty Lines | Don't number blank lines |

## Example

**Input:**
```
First line
Second line
Third line
```

**Output (with padding):**
```
1. First line
2. Second line
3. Third line
```

## Remove Numbers

The tool can detect and remove common line number formats:
- `1. text` or `  1. text`
- `1: text`
- `1) text`
- `[1] text`
- `(1) text`
- `1 text` (number + space)

## Use Cases

- Preparing code for documentation
- Forum posts and discussions
- Email quotes
- Reference numbering

## Privacy

All processing happens locally.

## License

MIT License
