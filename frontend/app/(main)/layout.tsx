import Header from 'components/Header'
import Footer from 'components/Footer'

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
          { href: '/profile/purchases', title: 'Профиль' },
        ]}
      />

      {children}
      <Footer />
    </>
  )
}
