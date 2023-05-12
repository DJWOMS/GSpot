import { generateMockFilterSortBy } from 'features/games/mocks'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(3)].map(() => generateMockFilterSortBy()))
}
