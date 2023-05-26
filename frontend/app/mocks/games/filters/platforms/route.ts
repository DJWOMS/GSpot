import { generateMockFilterPlatform } from 'features/games/mocks'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(4)].map((_, id) => generateMockFilterPlatform({ id })))
}
