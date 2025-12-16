import { useState, useRef, useEffect } from 'react';
import {
  encodeToBase64,
  decodeFromBase64,
  isLikelyText,
  arrayBufferToBase64,
} from './functions';
import './App.css';

export default function App() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [darkMode, setDarkMode] = useState(() => {
    const saved = localStorage.getItem('darkMode');
    return saved === 'true';
  });

  const fileInputRef = useRef(null);
  const binaryOutputRef = useRef(null);
  const outputTypeRef = useRef(null);

  useEffect(() => {
    localStorage.setItem('darkMode', darkMode);
  }, [darkMode]);

  const encodeBase64 = () => {
    try {
      const encoded = encodeToBase64(unescape(encodeURIComponent(input)));
      setOutput(encoded);
      binaryOutputRef.current = Uint8Array.from(encoded, (c) =>
        c.charCodeAt(0)
      );
      outputTypeRef.current = 'text';
    } catch (error) {
      setOutput('Error encoding to Base64: ' + error.message);
      binaryOutputRef.current = null;
      outputTypeRef.current = null;
    }
  };

  const decodeBase64 = () => {
    try {
      // Decode the cleaned Base64 string
      const binaryStr = decodeFromBase64(input);
      if (typeof binaryStr !== 'string') {
        throw new Error('Decoded result is not a string');
      }
      const bytes = Uint8Array.from(binaryStr, (c) => c.charCodeAt(0));
      const decoded = new TextDecoder('utf-8').decode(bytes);
      setOutput(decoded);
      binaryOutputRef.current = Uint8Array.from(decoded, (c) =>
        c.charCodeAt(0)
      );

      if (isLikelyText(decoded)) {
        outputTypeRef.current = 'text';
      } else {
        outputTypeRef.current = 'binary';
      }
    } catch (error) {
      // Output specific error message for debugging
      console.error('Decoding Error:', error);
      setOutput('Error decoding Base64: ' + error.message);
      binaryOutputRef.current = null;
      outputTypeRef.current = null;
    }
  };

  const handleLoadFile = () => {
    fileInputRef.current.click();
  };

  const onFileChange = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();

    if (file.name.endsWith('.b64')) {
      // Read .b64 file as text
      reader.onload = (event) => {
        const base64 = event.target.result.trim();
        setInput(base64);

        try {
          const decoded = decodeFromBase64(base64);
          const binary = Uint8Array.from(decoded, (c) => c.charCodeAt(0));
          binaryOutputRef.current = binary;
          outputTypeRef.current = 'binary';

          // Check if the decoded content is likely text
          const isText = isLikelyText(decoded);

          if (isText) {
            outputTypeRef.current = 'text';
            // utf-8
            const utf8Decoder = new TextDecoder('utf-8');
            const decodedText = utf8Decoder.decode(binary);
            setOutput(decodedText);
          } else {
            outputTypeRef.current = 'binary';
            setOutput(decoded);
          }
        } catch {
          setOutput('Error decoding .b64 file.');
          binaryOutputRef.current = null;
          outputTypeRef.current = null;
        }
      };
      reader.readAsText(file);
    } else {
      // Read any other file as binary and encode it to Base64
      reader.onload = (event) => {
        const buffer = event.target.result;
        const base64 = arrayBufferToBase64(buffer);
        setInput('');
        setOutput(base64);
        binaryOutputRef.current = null;
      };
      reader.readAsArrayBuffer(file);
    }
  };

  const handleSaveFile = () => {
    let filename = 'output';
    let blob;

    if (outputTypeRef.current === 'text') {
      // Save decoded text as .txt
      blob = new Blob([output], { type: 'text/plain;charset=utf-8' });
      filename += '.txt';
    } else if (outputTypeRef.current === 'binary') {
      // Save decoded binary as .bin
      blob = new Blob([binaryOutputRef.current], {
        type: 'application/octet-stream',
      });
      filename += '.bin';
    } // else decode output field as .b64
    else {
      // Save Base64-encoded output as .b64
      blob = new Blob([output], { type: 'text/plain;charset=utf-8' });
      filename += '.b64';
    }

    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    link.click();
  };

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const clearFields = () => {
    setInput('');
    setOutput('');
    binaryOutputRef.current = null;
    outputTypeRef.current = null;
  };

  return (
    <div className={`container ${darkMode ? 'dark' : 'light'}`}>
      <div>
        <div className='button-row'>
          <button onClick={encodeBase64}>→ Encode</button>
          <button onClick={decodeBase64}>← Decode</button>
          <button onClick={handleLoadFile}>📂 Load File</button>
          <button onClick={handleSaveFile}>💾 Save File</button>
          <button onClick={toggleDarkMode}>
            {darkMode ? '🌞 Light Mode' : '🌙 Dark Mode'}
          </button>
          <button onClick={clearFields}>🧹 Clear</button>
        </div>

        <textarea
          className={`textarea ${darkMode ? 'dark' : 'light'}`}
          placeholder='Input here...'
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />

        <textarea
          className={`textarea ${darkMode ? 'dark' : 'light'}`}
          placeholder='Output appears here...'
          value={output}
          readOnly
        />

        <input
          type='file'
          accept='*'
          ref={fileInputRef}
          onChange={onFileChange}
        />
      </div>

    
    </div>
  );
}
