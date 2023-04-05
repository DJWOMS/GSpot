import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([100, 500])
}
