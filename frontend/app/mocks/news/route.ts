import { generateMockNewsCard } from 'features/news/mocks'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(10)].map(() => generateMockNewsCard()))
}
