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
    return new Response('', {
      status: 200,
      headers: {
        'Set-Cookie': `token=${access_token}; HttpOnly; Path=/`,
        '\0Set-Cookie': `token=${refresh_token}; HttpOnly; Path=/`,
      },
    })
  }
  return NextResponse.json({ status: 'No user' }, { status: 400 })
}
