import { generateMockGameCard } from 'features/games/mocks'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(10)].map(() => generateMockGameCard()))
}
export function DELETE() {
  return NextResponse.json({}, { status: 200 })
}
