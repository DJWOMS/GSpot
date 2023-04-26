import { NextRequest, NextResponse } from 'next/server'

const couponData = ['QWERTY', 'ASDFGH', 'ZXCVBN', 'YUIOPK']

export async function POST(req: NextRequest) {
  const data = await req.json()
  const res = couponData.includes(data.coupon)
  return NextResponse.json(res)
}
