import { refresh_token, access_token } from 'features/auth/mocks'
import { AuthPayload } from 'features/auth/types'
import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

export async function POST(req: Request) {
  const cookieStorage = cookies()
  const data: AuthPayload = await req.json()
  if (data.username === 'test' && data.password === 'test') {
    cookieStorage.set('refresh_token', refresh_token, {
      httpOnly: true,
      path: '/',
      expires: new Date().setHours(new Date().getHours() + 1),
    })
    cookieStorage.set('access_token', access_token, {
      expires: new Date().setHours(new Date().getHours() + 2),
      httpOnly: true,
      path: '/',
    })
    return NextResponse.json({ status: 'authenticated' }, { status: 200 })
  }
  return NextResponse.json({ status: 'Invalid credentials' }, { status: 400 })
}
