import { access_token } from 'features/auth/mocks'
import { NextResponse } from 'next/server'

export async function GET(req: Request) {
  if (req.headers.get('access_token') === access_token) {
    return NextResponse.json({ status: 'Authenticated' }, { status: 200 })
  }
  return NextResponse.json({ status: 'Invalid token' }, { status: 400 })
}
