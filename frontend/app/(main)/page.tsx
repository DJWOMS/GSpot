import CardBig from 'components/CardBig'
import CarouselSection from 'components/CarouselSection'
import { GameCard, OtherGames, GameCardInterface } from 'features/games'
import { LatestNews } from 'features/news'
import { fetchServerSide } from 'lib/fetchServerSide'

const Home = async () => {
  const [bestGames, latestGames] = await Promise.all([
    fetchServerSide<GameCardInterface[]>({ path: '/games/best' }),
    fetchServerSide<GameCardInterface[]>({ path: '/games/latest' }),
  ])

  return (
    <>
      {/* best games with carousel */}
      {bestGames && (
        <CarouselSection
          title={
            <>
              <b>Лучшие игры</b> этого месяца
            </>
          }
          showBig
        >
          {bestGames.map((game, index) => (
            <CardBig key={index} {...game} />
          ))}
        </CarouselSection>
      )}

      {/* latest games with carousel */}
      {latestGames && (
        <CarouselSection title="Новинки и обновления">
          {latestGames.map((game, index) => (
            <GameCard key={index} {...game} />
          ))}
        </CarouselSection>
      )}

      <OtherGames />
      <LatestNews />
    </>
  )
}

export default Home
