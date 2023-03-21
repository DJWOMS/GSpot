import localFont from 'next/font/local'
import StyledComponentsRegistry from 'lib/registry'
import classNames from 'classnames'

// styles
import GlobalStyles from './GlobalStyles'
import 'assets/css/bootstrap-reboot.min.css'
import 'assets/css/bootstrap-grid.min.css'

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
