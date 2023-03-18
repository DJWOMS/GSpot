/** @type {import('next').NextConfig} */
const nextConfig = {
    experimental: {
        appDir: true,
    },
    output: 'standalone',
    compiler: {
        // Enables the styled-components SWC transform
        styledComponents: true,
    },
    swcMinify: true,
}

module.exports = nextConfig
