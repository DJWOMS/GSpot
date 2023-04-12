import { generateMockFilterPrice } from 'features/games'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json(generateMockFilterPrice())
}
