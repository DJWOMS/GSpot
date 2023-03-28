import BestGames from './BestGames'
import { LatestNews } from 'features/news'
import OtherGames from './OtherGames'
import LatestGames from './LatestGames'
import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const Home = async () => {
  const bestGamesData = await fetchServerSide<GameCardInterface[]>({
    path: '/best-games',
  })
  const latestGamesData = await fetchServerSide<GameCardInterface[]>({
    path: '/latest-games',
  })

  return (
    <>
      <BestGames games={bestGamesData} />
      <LatestGames games={latestGamesData} />
      <OtherGames />
      <LatestNews />
    </>
  )
}

export default Home
