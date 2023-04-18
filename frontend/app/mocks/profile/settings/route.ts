import { generateMockPurchaseCard, UserDataInterface } from 'features/profile'
import { NextResponse } from 'next/server'

const mockData = {
  nickName: 'Jon(0)_(^)',
  email: 'Jon@gmail.com',
  firstName: 'John',
  lastName: 'Smith',
}

export function GET() {
  return NextResponse.json(mockData)
}

export function POST(req: Promise<UserDataInterface>) {
  return NextResponse.json(mockData)
}
