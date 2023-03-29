import Header from 'components/Header'
import Footer from 'components/Footer'
import { FC, ReactNode } from 'react'

// head
export const metadata = {
  title: 'GSpot',
  description: 'Games market',
}

const RootLayout: FC<{ children: ReactNode }> = ({ children }) => {
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
