import { generateMockGamingCards } from 'features/games'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json(generateMockGamingCards())
}
