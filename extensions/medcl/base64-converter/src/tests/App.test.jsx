import { render, screen } from '@testing-library/react';
import App from '../src/App';

test('renders Base64 Converter', () => {
  render(<App />);
  const linkElement = screen.getByText(/Base64 Converter/i);
  expect(linkElement).to.exist;
});
