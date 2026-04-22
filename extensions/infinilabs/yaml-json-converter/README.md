# YAML JSON Converter

Bidirectional converter between YAML and JSON formats.

## Features

- **YAML to JSON** - Convert YAML to JSON
- **JSON to YAML** - Convert JSON to YAML
- **Configurable indent** - 1-8 spaces
- **Swap direction** - Click swap to reverse conversion
- **Error messages** - Clear error feedback

## Supported YAML Features

- Nested objects
- Arrays (with `-` prefix)
- Strings (quoted and unquoted)
- Numbers (integers and floats)
- Booleans (true/false)
- Null values (null, ~)
- Comments (ignored)

## Usage

1. Enter YAML or JSON in the left panel
2. Converted output appears on the right
3. Click swap button to reverse direction
4. Adjust indent as needed

## Example

**YAML:**
```yaml
name: John
age: 30
skills:
  - JavaScript
  - Python
```

**JSON:**
```json
{
  "name": "John",
  "age": 30,
  "skills": ["JavaScript", "Python"]
}
```

## Privacy

All processing happens locally.

## License

MIT License
