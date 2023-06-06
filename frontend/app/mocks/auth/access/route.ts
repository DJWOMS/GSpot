import { RequestCookies } from 'next/dist/compiled/@edge-runtime/cookies'
import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

const access_token =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
const refresh_token =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

interface AuthPayload {
  username: string
  password: string
}

export async function POST(req: Request) {
  const data = (await req.json()) as AuthPayload
  if (data.username === 'test' && data.password === 'test') {
    const expirationDate = new Date(Date.now() + 86400 * 1000).toUTCString()
    const cookiesStore = cookies() as RequestCookies

    cookiesStore.set({
      name: 'access_token',
      value: access_token,
      path: '/',
    })

    cookiesStore.set({
      name: 'refresh_token',
      value: refresh_token,
      httpOnly: true,
      path: '/',
    })

    return NextResponse.json('')
  }
}
