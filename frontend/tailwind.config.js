const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}', './features/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        background: '#1b222e',
        primary: '#a782e9',
        'trans-gray': 'rgba(167, 130, 233, 0.06)',
        acid: '#29b474',
        dark: 'rgba(167, 130, 233, 0.03)',
        light: '#dbdada',
      },
      fontFamily: {
        sans: ['var(--font-opensans)', ...defaultTheme.fontFamily.sans],
        mont: ['var(--font-montserrat)', ...defaultTheme.fontFamily.sans],
      },
      borderRadius: {
        default: '6px',
      },
    },
  },
  plugins: [],
}
