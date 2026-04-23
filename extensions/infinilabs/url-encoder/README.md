# URL Encoder/Decoder

Encode and decode URL components and full URLs.

## Features

- **Component Mode**: Uses `encodeURIComponent`/`decodeURIComponent` for query parameters
- **Full URL Mode**: Uses `encodeURI`/`decodeURI` for complete URLs (preserves special characters like `://`, `?`, `&`)
- **Swap**: Exchange input and output
- **Copy**: Copy result to clipboard

## Usage

1. Select encoding mode (Component or Full URL)
2. Enter or paste text
3. Click Encode or Decode
4. Copy the result

## Component vs Full URL

- **Component**: Encodes ALL special characters including `/ ? & =`. Use for query parameter values.
- **Full URL**: Preserves URL structure characters. Use for encoding entire URLs with special characters in paths.

## Privacy

All encoding/decoding happens locally. No data is sent anywhere.

## License

MIT License
