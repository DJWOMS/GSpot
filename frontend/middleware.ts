import { DEBUG } from 'configs'
import { NextRequest, NextResponse } from 'next/server'

// Limit the middleware to paths starting with `/mocks/`
export const config = {
  matcher: '/mocks/:function*',
}

export function middleware(request: NextRequest) {
  if (!DEBUG) {
    const url = request.nextUrl.clone()

    url.pathname = `/404`
    return NextResponse.rewrite(url)
  }
}
