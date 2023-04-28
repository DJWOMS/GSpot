'use client'

import { Analytics } from '@vercel/analytics/react'
import cn from 'classnames'
import localFont from 'next/font/local'
import { AuthProvider } from 'providers/AuthProvider'
import './global.scss'

// Commented because use client used for Provider
// head
// export const metadata = {
//   title: 'GSpot',
//   description: 'Games market',
// }

// fonts
const montserrat = localFont({
  src: '../assets/fonts/Montserrat.ttf',
  variable: '--font-montserrat',
  preload: true,
})
const openSans = localFont({
  src: '../assets/fonts/OpenSans.ttf',
  variable: '--font-opensans',
  preload: true,
})

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru" className={cn(montserrat.variable, openSans.variable)}>
      <body>
        <AuthProvider>
          {children}
          <Analytics />
        </AuthProvider>
      </body>
    </html>
  )
}
