import { Header } from './Header'
import { Footer } from './Footer'

// head
export const metadata = {
    title: 'GSpot',
    description: 'Games market',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <Header />
            {children}
            <Footer />
        </>
    )
}
