import { couponData } from 'features/profile'
import { NextRequest, NextResponse } from 'next/server'

export async function POST(req: NextRequest) {
  const data = await req.json()
  const res = couponData.includes(data.coupon)
  return NextResponse.json(res)
}
