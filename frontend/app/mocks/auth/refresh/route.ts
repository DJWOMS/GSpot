import { access_token, refresh_token } from 'features/auth'
import { NextResponse } from 'next/server'

export async function POST(req: Request) {
  const data = (await req.json()) as { refresh_token: string }
  if (data.refresh_token === access_token) {
    return new Response('', {
      status: 200,
      headers: {
        'Set-Cookie': `access_token=${access_token}; HttpOnly; Path=/`,
        '\0Set-Cookie': `refresh_token=${refresh_token}; HttpOnly; Path=/`,
      },
    })
  }
  return NextResponse.json({ status: 'Invalid token' }, { status: 400 })
}
