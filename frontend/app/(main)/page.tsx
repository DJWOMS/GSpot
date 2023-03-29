import { GameCardInterface } from 'features/games'
import { LatestNews } from 'features/news'
import { fetchServerSide } from 'lib/fetchServerSide'
import BestGames from './BestGames'
import LatestGames from './LatestGames'
import OtherGames from './OtherGames'

export const revalidate = 10 // revalidate this page every 60 seconds

const Home = async () => {
  const bestGamesData = fetchServerSide<GameCardInterface[]>({
    path: '/games/best',
  })
  const latestGamesData = fetchServerSide<GameCardInterface[]>({
    path: '/games/latest',
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
