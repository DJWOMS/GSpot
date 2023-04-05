import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([
    {
      slug: 'ps',
      name: 'Playstation',
    },
    {
      slug: 'xb',
      name: 'XBOX',
    },
    {
      slug: 'wn',
      name: 'Windows',
    },
    {
      slug: 'mo',
      name: 'Mac OS',
    },
  ])
}
