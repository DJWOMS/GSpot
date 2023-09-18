import { generateMockFilterPrice } from 'features/games/mocks'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json(generateMockFilterPrice())
}
