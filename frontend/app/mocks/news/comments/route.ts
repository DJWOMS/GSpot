import { NextResponse } from 'next/server'

const mockComments = [
  { avatar: '', name: 'John Doe', time: '20.08.2020, 14:53', text: 'NotImpressed', likes: 7, dislikes: 12 },
  { avatar: '', name: 'Mike Mayers', time: '30.05.2020, 17:30', text: 'So so', likes: 5, dislikes: 1 },
  {
    avatar: '',
    name: 'Sunny Rooster',
    time: '05.08.2022, 12:40',
    text: 'There are many variations of passages of Lorem Ipsum avmajority have suffered alteration in some form, by injected humour, or randomised wlook',
    likes: 2,
    dislikes: 4,
  },
]

export function GET() {
  return NextResponse.json(mockComments)
}
