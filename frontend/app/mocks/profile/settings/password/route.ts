import { NextResponse } from 'next/server'

export async function POST() {
  return NextResponse.json({ message: 'changed' }, { status: 201 })
}
