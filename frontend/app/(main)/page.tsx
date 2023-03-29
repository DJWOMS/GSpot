import BestGames from './BestGames'
import { LatestNews } from 'features/news'
import OtherGames from './OtherGames'
import LatestGames from './LatestGames'

const Home = async () => {
  return (
    <>
      {/* @ts-expect-error Async Server Component */}
      <BestGames />
      {/* @ts-expect-error Async Server Component */}
      <LatestGames />
      <OtherGames />
      <LatestNews />
    </>
  )
}

export default Home
