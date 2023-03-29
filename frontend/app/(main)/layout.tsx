import Footer from 'components/Footer'
import Header from 'components/Header'

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
        ]}
      />

      {children}
      <Footer />
    </>
  )
}
