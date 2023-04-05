import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([
    {
      slug: 'adventure',
      name: 'Adventure',
    },
    {
      slug: 'fight',
      name: 'Fight',
    },
    {
      slug: 'sport',
      name: 'Sport',
    },
    {
      slug: 'action',
      name: 'Action',
    },
    {
      slug: 'rpg',
      name: 'RPG',
    },
    {
      slug: 'platform',
      name: 'Platform',
    },
  ])
}
