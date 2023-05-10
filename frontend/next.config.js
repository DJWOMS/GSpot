/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['loremflickr.com'],
    unoptimized: true,
  },
}

module.exports = nextConfig
