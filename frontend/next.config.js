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
}

module.exports = nextConfig
