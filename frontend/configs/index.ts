export const DEBUG = process.env.DEBUG === '1' || process.env.DEBUG === undefined

// if server use 127.0.0.1 else localhost
const localhost = typeof window === 'undefined' ? '127.0.0.1' : 'localhost'
export const API_URL = process.env.API_URL ?? `http://${localhost}:3000/mocks`
export const LINK_TO_GOOGLE_MAPS =
  'https://maps.google.com/maps?q=221B+Baker+Street,+London,+United+Kingdom&amp;hl=en&amp;t=v&amp;hnear=221B+Baker+St,+London+NW1+6XE,+United+Kingdom'
