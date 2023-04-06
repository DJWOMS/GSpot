import { generateMockGameCard } from 'features/games'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(Math.floor(Math.random() * 10) + 10)].map(() => generateMockGameCard()))
}
