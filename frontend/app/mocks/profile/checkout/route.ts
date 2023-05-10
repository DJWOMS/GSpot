import { generateMockCheckoutGameCard } from 'features/profile/mocks'
import { NextRequest, NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([...new Array(5)].map(() => generateMockCheckoutGameCard()))
}

export async function POST(req: NextRequest) {
  const data = await req.json()
  return NextResponse.json(data)
}
