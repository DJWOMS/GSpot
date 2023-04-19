import { NextResponse } from 'next/server'

//export function GET() {
//  return NextResponse.json([...new Array(1)].map(() => generateMockContactsForm()))
//}() => generateMockContactsForm()
//export function POST(request: NextRequest) {
//  console.log(request.body, 'request')
//  return NextResponse.json(() => generateMockContactsForm())
//}
export async function POST() {
  return NextResponse.json({ message: 'Спасибо! Ваши данные успешно отправлены!' }, { status: 201 })
}
