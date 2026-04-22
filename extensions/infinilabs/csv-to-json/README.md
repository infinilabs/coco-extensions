# CSV to JSON

Convert CSV data to JSON format with various options.

## Features

- **Delimiter options** - Comma, semicolon, tab, pipe
- **Header support** - First row as keys or raw arrays
- **Type inference** - Numbers and booleans auto-detected
- **Quote handling** - Proper CSV quote escaping
- **Bidirectional** - Also converts JSON to CSV

## Usage

1. Paste CSV data in the left panel
2. Configure delimiter and header options
3. JSON appears in the right panel
4. Click "Copy JSON" to copy result

## Options

| Option | Description |
|--------|-------------|
| First row is header | Use first row as object keys |
| Delimiter | Character separating values |
| Pretty print | Format JSON with indentation |

## Example

**Input CSV:**
```csv
name,email,age
John,john@example.com,30
Jane,jane@example.com,25
```

**Output JSON:**
```json
[
  {"name": "John", "email": "john@example.com", "age": 30},
  {"name": "Jane", "email": "jane@example.com", "age": 25}
]
```

## Privacy

All processing happens locally. No data is sent anywhere.

## License

MIT License
