import localFont from 'next/font/local'
import cn from 'classnames'
import './global.scss'

// head
export const metadata = {
    title: 'GSpot',
    description: 'Games market',
}

// fonts
const montserrat = localFont({
    src: '../fonts/Montserrat.ttf',
    variable: '--font-montserrat',
})
const openSans = localFont({
    src: '../fonts/OpenSans.ttf',
    variable: '--font-opensans',
})

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="ru" className={cn(montserrat.variable, openSans.variable)}>
            <body>{children}</body>
        </html>
    )
}
