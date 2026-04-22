# XML Formatter

Format, beautify, and minify XML documents.

## Features

- **Auto-formatting** - Proper indentation and line breaks
- **Validation** - Check XML validity
- **Minify** - Compact XML to minimal size
- **Configurable indent** - 1-8 spaces

## Supported Elements

- XML declarations (`<?xml ...?>`)
- Opening and closing tags
- Self-closing tags (`<br />`)
- Comments (`<!-- ... -->`)
- Text content
- Attributes

## Options

| Option | Description |
|--------|-------------|
| Indent | Number of spaces for indentation |

## Example

**Input:**
```xml
<root><item id="1"><name>Test</name><value>123</value></item></root>
```

**Output:**
```xml
<root>
  <item id="1">
    <name>Test</name>
    <value>123</value>
  </item>
</root>
```

## Validation

The formatter validates XML using the browser's built-in DOMParser. Invalid XML will show an error indicator.

## Privacy

All processing happens locally.

## License

MIT License
