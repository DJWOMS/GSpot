import { NextResponse } from 'next/server'

export function GET() {
  return NextResponse.json([
    {
      value: '0',
      option: 'По интересам',
    },
    {
      value: '1',
      option: 'От новых к старым',
    },
    {
      value: '2',
      option: 'От старых к новым',
    },
  ])
}
