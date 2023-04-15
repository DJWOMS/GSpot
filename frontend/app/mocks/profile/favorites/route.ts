import { generateMockFavoriteGameCard } from 'features/profile'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(10)].map(() => generateMockFavoriteGameCard()))
}
