import { Montserrat, Open_Sans } from 'next/font/google'
import StyledComponentsRegistry from '@/lib/registry'
import classNames from 'classnames'

// styles
import GlobalStyles from './GlobalStyles'
import '@/public/css/bootstrap-reboot.min.css'
import '@/public/css/bootstrap-grid.min.css'

// head
export const metadata = {
    title: 'GSpot',
    description: 'Games market',
}

// fonts
const montserrat = Montserrat({
    weight: ['300', '400', '500'],
    subsets: ['cyrillic', 'latin'],
    display: 'swap',
    variable: '--font-montserrat',
})
const openSans = Open_Sans({
    weight: ['400', '600'],
    subsets: ['cyrillic', 'latin'],
    display: 'swap',
    variable: '--font-opensans',
})

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <StyledComponentsRegistry>
            <html lang="ru" className={classNames(montserrat.variable, openSans.variable)}>
                <body>
                    <GlobalStyles />
                    {children}
                </body>
            </html>
        </StyledComponentsRegistry>
    )
}
