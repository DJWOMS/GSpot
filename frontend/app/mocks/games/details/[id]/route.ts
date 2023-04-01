import { generateMockGameDetails } from 'features/games'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json(generateMockGameDetails())
}
