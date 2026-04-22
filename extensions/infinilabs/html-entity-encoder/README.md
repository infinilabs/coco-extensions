# HTML Entity Encoder

Encode and decode HTML entities.

## Features

- **Named Entities**: Convert to named entities like `&amp;`, `&lt;`, `&gt;`
- **Numeric**: Convert to numeric entities like `&#38;`, `&#60;`
- **All Characters**: Encode all non-ASCII characters
- **Decode**: Convert entities back to characters
- **Quick Reference**: Common entities at a glance

## Encoding Modes

| Mode | Description | Example |
|------|-------------|---------|
| Named | Standard HTML entities | `&` → `&amp;` |
| Numeric | Decimal code points | `&` → `&#38;` |
| All | All non-ASCII + special | `é` → `&#233;` |

## Common Entities

| Character | Named | Numeric |
|-----------|-------|---------|
| `&` | `&amp;` | `&#38;` |
| `<` | `&lt;` | `&#60;` |
| `>` | `&gt;` | `&#62;` |
| `"` | `&quot;` | `&#34;` |
| `'` | `&#39;` | `&#39;` |
| (space) | `&nbsp;` | `&#160;` |

## Usage

1. Select encoding mode
2. Enter text or HTML
3. Click Encode or Decode
4. Copy the result

## Privacy

All encoding/decoding happens locally. No data is sent anywhere.

## License

MIT License
