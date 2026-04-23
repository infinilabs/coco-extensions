# JWT Decoder

Decode and inspect JWT (JSON Web Token) tokens.

## Features

- **Header**: View algorithm and token type
- **Payload**: View all claims with syntax highlighting
- **Expiration**: Shows issued at, expiration time, and time remaining
- **Status**: Visual indicator if token is expired or valid
- **Signature**: View the signature (NOT verified)

## Usage

1. Paste a JWT token (starts with `eyJ...`)
2. View decoded header and payload
3. Check expiration status

## Common Claims

- `iss` - Issuer
- `sub` - Subject
- `aud` - Audience
- `exp` - Expiration time
- `iat` - Issued at
- `nbf` - Not before

## Security Note

This tool only DECODES tokens - it does NOT verify signatures. Never trust token contents without server-side verification.

## Privacy

All decoding happens locally. No tokens are sent anywhere.

## License

MIT License
