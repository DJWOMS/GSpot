import { generateMockPurchaseCard, UserDataInterface } from 'features/profile'
import { NextRequest, NextResponse } from 'next/server'

let mockData = {
  nickName: 'Jon(0)_(^)',
  email: 'Jon@gmail.com',
  firstName: 'John',
  lastName: 'Smith',
}

export function GET() {
  return NextResponse.json(mockData)
}

export async function POST(req: Request) {
  const data = await req.json()
  mockData = data
  return NextResponse.json(mockData)
}
