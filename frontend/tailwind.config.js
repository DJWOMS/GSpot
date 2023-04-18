const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}', './features/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        background: '#1b222e',
        main: {
          30: 'rgba(167, 130, 233, 0.03)',
          40: 'rgba(167, 130, 233, 0.04)',
          50: 'rgba(167, 130, 233, 0.05)',
          60: 'rgba(167, 130, 233, 0.06)',
          70: 'rgba(167, 130, 233, 0.07)',
          150: 'rgba(167,130, 233, 0.15)',
          250: 'rgba(167,130, 233, 0.25)',
          300: 'rgba(167,130, 233, 0.3)',
          400: 'rgba(167,130, 233, 0.4)',
          500: 'rgba(167,130, 233, 0.5)',
          600: 'rgba(167,130, 233, 0.6)',
        },
        platform: {
          xb: '#0e7a0d',
          ps: '#665cbe',
          wn: '#00aef0',
          ap: '#555',
        },
        danger: '#fd6060',
        primary: '#a782e9',
        acid: '#29b474',
        light: '#dbdada',
      },
      fontFamily: {
        sans: ['var(--font-opensans)', ...defaultTheme.fontFamily.sans],
        mont: ['var(--font-montserrat)', ...defaultTheme.fontFamily.sans],
      },
      borderRadius: {
        default: '6px',
      },
      letterSpacing: {
        default: '.4px',
      },
    },
  },
  plugins: [],
}
