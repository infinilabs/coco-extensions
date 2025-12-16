function encodeToBase64(str) {
  str = String(str); // Ensure input is string
  return btoa(str);
}

function decodeFromBase64(base64Str) {
  if (typeof base64Str !== 'string') {
    throw new Error('Input must be a string');
  }

  // Remove whitespace
  base64Str = base64Str.trim().replace(/\s+/g, '');

  // Basic length check
  if (base64Str.length % 4 !== 0) {
    throw new Error('Invalid Base64 length');
  }

  try {
    return atob(base64Str);
  } catch (e) {
    throw new Error('Invalid Base64 content');
  }
}

function isLikelyText(content) {
  let text = '';

  if (typeof content === 'string') {
    text = content;
  } else if (content instanceof Uint8Array) {
    try {
      // Decode binary content to string (throws if invalid UTF-8)
      text = new TextDecoder('utf-8', { fatal: true }).decode(content);
    } catch {
      return false;
    }
  } else {
    return false; // unsupported input type
  }

  // Regex check: only printable ASCII characters and whitespace
  return /^[\x09\x0A\x0D\x20-\x7E]*$/.test(text);
}

function arrayBufferToBase64(buffer) {
  if (!(buffer instanceof ArrayBuffer)) {
    throw new Error('Input must be an ArrayBuffer');
  }
  const bytes = new Uint8Array(buffer);
  let binary = '';
  for (let b of bytes) {
    binary += String.fromCharCode(b);
  }
  return encodeToBase64(binary);
}

export { encodeToBase64, decodeFromBase64, isLikelyText, arrayBufferToBase64 };
