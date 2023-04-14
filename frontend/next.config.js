const API_URL = process.env.API_URL || (process.env.VERCEL_URL ? `${process.env.VERCEL_URL}/mocks` : null)

/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
    scrollRestoration: true,
  },
  output: 'standalone',
  swcMinify: true,
  images: {
    domains: ['loremflickr.com'],
    unoptimized: true,
  },
  env: {
    API_URL,
    NEXT_PUBLIC_API_URL: API_URL,
  },
}

module.exports = nextConfig
