<<<<<<< HEAD
import localFont from 'next/font/local'
import StyledComponentsRegistry from 'lib/registry'
import classNames from 'classnames'

// styles
import GlobalStyles from './GlobalStyles'
import 'assets/css/bootstrap-reboot.min.css'
import 'assets/css/bootstrap-grid.min.css'

// head
=======
>>>>>>> fa8c76e588642c68340ddb49415b5b68f30c5fa3
export const metadata = {
    title: 'GSpot',
    description: 'Games market',
}

<<<<<<< HEAD
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
=======
export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="ru">
            <body>{children}</body>
        </html>
>>>>>>> fa8c76e588642c68340ddb49415b5b68f30c5fa3
    )
}
