import BestGames from './BestGames'
import { LatestNews } from 'features/news'
import OtherGames from './OtherGames'
import LatestGames from './LatestGames'
import { GameCardInterface } from 'features/games'

async function getBestGamesData(): Promise<GameCardInterface[]> {
  try {
    const res = await fetch('http://127.0.0.1:3100/api/best-games')

    if (!res.ok) {
      throw new Error('Failed to fetch data!')
    }

    return await res.json()
  } catch (error) {
    console.log(error)
    return []
  }
}

const Home = async () => {
  const bestGamesData: Array<GameCardInterface> = await getBestGamesData()

  return (
    <>
      {/* @ts-expect-error Async Server Component */}
      <BestGames bestGamesData={bestGamesData} />
      {/* @ts-expect-error Async Server Component */}
      <LatestGames />
      <OtherGames />
      <LatestNews />
    </>
  )
}

export default Home
