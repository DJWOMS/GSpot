import { ReactNode } from 'react'
import Footer from 'components/Footer'
import Header from 'components/Header'
import { checkAuthServer } from 'features/auth'

// head
export const metadata = {
  title: 'GSpot',
  description: 'Games market',
}

const RootLayout: ({ children }: { children: ReactNode }) => Promise<JSX.Element> = async ({ children }) => {
  const isAuthenticated = await checkAuthServer()
  return (
    <>
      <Header
        isAuthenticated={isAuthenticated}
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
