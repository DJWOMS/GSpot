import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

const access_token =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

export async function POST(req: Request) {
  const data = (await req.json()) as { refresh_token: string }
  if (data.refresh_token === access_token) {
    const cookiesStore = cookies()

    cookiesStore.set({
      name: 'access_token',
      value: access_token,
      httpOnly: true,
      path: '/',
    })

    cookiesStore.set({
      name: 'refresh_token',
      value: access_token,
      httpOnly: true,
      path: '/',
    })

    return NextResponse.json('')
  }
  return NextResponse.json({ status: 'Invalid token' }, { status: 400 })
}
