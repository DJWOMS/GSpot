export const DEBUG = process.env.DEBUG === '1' || process.env.DEBUG === undefined

// if server use 127.0.0.1 else localhost
const localhost = typeof window === 'undefined' ? '127.0.0.1' : 'localhost'
export const API_URL = process.env.API_URL ?? `http://${localhost}:3000/mocks`
