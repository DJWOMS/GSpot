import BestGames from './BestGames'
import { LatestNews } from 'features/news'
import OtherGames from './OtherGames'
import LatestGames from './LatestGames'
import { fetchServerSide } from 'lib/fetchServerSide'
import { GameCardInterface } from 'features/games'

const Home = async () => {
  const [bestGames, latestGames] = await Promise.all([
    fetchServerSide<GameCardInterface[]>({
      path: '/best-games',
    }),
    fetchServerSide<GameCardInterface[]>({
      path: '/latest-games',
    }),
  ])

  return (
    <>
      <BestGames games={bestGames ?? []} />
      <LatestGames games={latestGames ?? []} />
      <OtherGames />
      <LatestNews />
    </>
  )
}

export default Home
