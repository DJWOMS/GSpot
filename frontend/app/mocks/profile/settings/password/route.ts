import { NextResponse } from 'next/server'

const mockData = {
  change: 'password changed',
}

export async function POST() {
  return NextResponse.json(mockData)
}
