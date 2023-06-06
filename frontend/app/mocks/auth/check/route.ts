import { NextResponse } from 'next/server'

const access_token =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

export async function GET(req: Request) {
  if (req.headers.get('access_token') === access_token) {
    return NextResponse.json({ status: 'Authenticated' }, { status: 200 })
  }
  return NextResponse.json({ status: 'Invalid token' }, { status: 400 })
}
