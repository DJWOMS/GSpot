import { generateMockFilterGenre } from 'features/games/mocks'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(5)].map((_, id) => generateMockFilterGenre({ id })))
}
