import { refresh_token, access_token } from 'features/auth/mocks'
import { AuthPayload } from 'features/auth/types'
import { NextResponse } from 'next/server'

export async function POST(req: Request) {
  const data = (await req.json()) as AuthPayload
  if (data.username === 'test' && data.password === 'test') {
    return new Response('', {
      status: 200,
      headers: {
        'Set-Cookie': `access_token=${access_token}; HttpOnly; Path=/`,
        '\0Set-Cookie': `refresh_token=${refresh_token}; HttpOnly; Path=/`,
      },
    })
  }
  return NextResponse.json({ status: 'No user' }, { status: 400 })
}
