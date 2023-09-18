// eslint-disable-next-line @typescript-eslint/no-var-requires
const nextJest = require('next/jest')

const createJestConfig = nextJest({
  // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
  dir: './',
})

// Add any custom config to be passed to Jest
/** @type {import('jest').Config} */
const customJestConfig = {
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  roots: ['<rootDir>'],
  modulePaths: ['<rootDir>'],
  moduleDirectories: ['node_modules'],
  testEnvironment: 'jest-environment-jsdom',
  testPathIgnorePatterns: [
    '<rootDir>/.next/',
    '<rootDir>/.vercel/',
    '<rootDir>[/\\\\](node_modules|.next)[/\\\\]',
  ],
  transformIgnorePatterns: ['/node_modules/', '^.+\\.module\\.(css|sass|scss)$'],
  transform: {
    // Use babel-jest to transpile tests with the next/babel preset
    // https://jestjs.io/docs/configuration#transform-objectstring-pathtotransformer--pathtotransformer-object
    '^.+\\.(js|jsx|ts|tsx)$': ['babel-jest', { presets: ['next/babel'] }],
  },
  setupFilesAfterEnv: ['@testing-library/jest-dom', '@testing-library/jest-dom/extend-expect'],
}

// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
module.exports = createJestConfig(customJestConfig)
