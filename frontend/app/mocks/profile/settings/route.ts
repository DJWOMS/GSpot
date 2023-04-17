import { generateMockPurchaseCard } from 'features/profile'
import { NextResponse } from 'next/server'

const mockData = {
  nickname: 'Jon(0)_(^)',
  email: 'Jon@gmail.com',
  firstName: 'John',
  lastName: 'Smith',
}

export function GET() {
  return NextResponse.json(mockData)
}
