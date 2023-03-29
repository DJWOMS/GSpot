import Header from 'components/Header'
import Footer from 'components/Footer'
import { fetchServerSide } from 'lib/fetchServerSide'

// head
export const metadata = {
  title: 'GSpot',
  description: 'Games market',
}

interface Props {
  children: React.ReactNode
}

const RootLayout = async ({ children }: Props) => {
  const categories = await fetchServerSide<{ id: number; name: string }[]>({
    path: '/categories',
  })

  return (
    <>
      <Header
        categories={categories ?? []}
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
