import { generateMockGameCardSimple } from 'features/games/mocks'
import { NextResponse, type NextRequest } from 'next/server'

export function GET(request: NextRequest) {
  const url = new URL(request.url)
  const params = Object.fromEntries(url.searchParams.entries())
  const query = params.query?.toLowerCase() ?? ''

  const mockData = [
    generateMockGameCardSimple({ title: 'Game 1' }),
    generateMockGameCardSimple({ title: 'Game 2' }),
    generateMockGameCardSimple({ title: 'Game 3' }),
    generateMockGameCardSimple({ title: 'Other 1' }),
    generateMockGameCardSimple({ title: 'Other 1' }),
    generateMockGameCardSimple({ title: 'Simple' }),
  ]

  // filter by query
  const filteredMock = mockData.filter((game) => game.title.toLowerCase().includes(query)).slice(0, 3)

  // prepare response
  const responseMock = filteredMock.map(({ title }, index) => ({
    id: index,
    title,
  }))

  return NextResponse.json(responseMock)
}
