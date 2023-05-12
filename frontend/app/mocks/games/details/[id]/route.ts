import { generateMockGameDetails } from 'features/games/mocks'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json(generateMockGameDetails())
}
