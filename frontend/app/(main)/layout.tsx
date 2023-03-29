import Header from 'components/Header'
import Footer from 'components/Footer'

// head
export const metadata = {
  title: 'GSpot',
  description: 'Games market',
}

interface Props {
  children: React.ReactNode
}

const RootLayout = ({ children }: Props) => {
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

export default RootLayout
