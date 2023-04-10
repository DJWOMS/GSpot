import { generateMockCheckoutGameCard } from 'features/profile'
import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(5)].map(() => generateMockCheckoutGameCard()))
}
