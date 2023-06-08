import { NextResponse } from 'next/server'

const access_token =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

export async function POST(req: Request) {
  const data = (await req.json()) as { refresh_token: string }
  if (data.refresh_token === access_token) {
    return new Response('', {
      status: 200,
      headers: {
        'Set-Cookie': `token=${access_token}; HttpOnly; Path=/`,
        '\0Set-Cookie': `token=${access_token}; HttpOnly; Path=/`,
      },
    })
  }
  return NextResponse.json({ status: 'Invalid token' }, { status: 400 })
}
