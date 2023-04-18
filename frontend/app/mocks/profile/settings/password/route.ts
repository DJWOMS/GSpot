import { NextResponse } from 'next/server'

const mockData = {
  change: 'password change',
}

export function POST() {
  return NextResponse.json(mockData)
}
