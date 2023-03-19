import { FC } from 'react'
import { BestGames } from './BestGames'
import { LatestNews } from './LatestNews'
import { OtherGames } from './OtherGames'

const Home: FC = (): JSX.Element => {
    return (
        <>
            <BestGames />
            <OtherGames />
            <LatestNews />
        </>
    )
}

export default Home
