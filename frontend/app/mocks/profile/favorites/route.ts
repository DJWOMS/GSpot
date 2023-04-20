import { generateMockFavoriteGameCard } from 'features/profile'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(10)].map(() => generateMockFavoriteGameCard()))
}
export function DELETE() {
  return NextResponse.json({}, { status: 200 })
}
