import { FC } from 'react'
import { BestGames } from './BestGames'
import { LatestNews } from 'features/news'
import { OtherGames } from './OtherGames'
import { LatestGames } from './LatestGames'

const Home: FC = (): JSX.Element => {
  return (
    <>
      <BestGames />
      <LatestGames />
      <OtherGames />
      <LatestNews />
    </>
  )
}

export default Home
