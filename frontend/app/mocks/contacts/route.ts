import { NextResponse } from 'next/server'

export async function POST() {
  return NextResponse.json({ message: 'Спасибо! Ваши данные успешно отправлены!' }, { status: 201 })
}
