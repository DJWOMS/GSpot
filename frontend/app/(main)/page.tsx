import BestGames from './BestGames'
import { LatestNews } from 'features/news'
import OtherGames from './OtherGames'
import LatestGames from './LatestGames'
import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const Home = async () => {
  const bestGamesData = fetchServerSide<GameCardInterface[]>({
    path: '/best-games',
  })
  const latestGamesData = fetchServerSide<GameCardInterface[]>({
    path: '/latest-games',
  })

  const [bestGames, latestGames] = await Promise.all([bestGamesData, latestGamesData])

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
