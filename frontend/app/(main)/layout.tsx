import Header from './(components)/header'
import Footer from './(components)/footer'

// head
export const metadata = {
    title: 'GSpot',
    description: 'Games market',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <Header
                links={[
                    { href: '/', title: 'Главная' },
                    { href: '/catalog', title: 'Каталог' },
                    { href: '/news', title: 'Новости' },
                    { href: '/details', title: 'Детали' },
                ]}
            />

            {children}
            <Footer />
        </>
    )
}
