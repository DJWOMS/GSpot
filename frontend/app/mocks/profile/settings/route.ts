import { NextResponse } from 'next/server'

let mockData = {
  username: 'Jon(0)_(^)',
  email: 'Jon@gmail.com',
  firstName: 'John',
  lastName: 'Smith',
}

export function GET() {
  return NextResponse.json(mockData)
}

export async function POST(req: Request) {
  const data = await req.json()
  if (data.username !== 'busyname') {
    mockData = data
    return NextResponse.json({ status: 201 })
  }
  return NextResponse.json({ status: 400 })
}
