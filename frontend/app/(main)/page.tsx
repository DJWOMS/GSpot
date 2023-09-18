import CarouselSection from 'components/CarouselSection'
import Container from 'components/Container'
import Section from 'components/Section'
import { GameCard, GameCardBig, ListGames } from 'features/games/components'
import type { GameCardInterface, GameListInterface } from 'features/games/types'
import { LatestNews } from 'features/news/components'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.css'

const Home = async () => {
  const [bestGames, latestGames, otherGames, giftGames, subscriptionsGames] = await Promise.all([
    fetchServerSide<GameCardInterface[]>({ path: '/games/best' }),
    fetchServerSide<GameCardInterface[]>({ path: '/games/latest' }),
    fetchServerSide<GameListInterface[]>({ path: '/games/other?key=a', cache: 'no-cache' }),
    fetchServerSide<GameListInterface[]>({ path: '/games/other?key=b', cache: 'no-cache' }),
    fetchServerSide<GameListInterface[]>({ path: '/games/other?key=c', cache: 'no-cache' }),
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
            <GameCardBig key={index} {...game} />
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

      <Container>
        <div className={s.sections}>
          {otherGames && (
            <Section title="Игры">
              <ListGames>{otherGames}</ListGames>
            </Section>
          )}

          {giftGames && (
            <Section title="Наборы в подарок">
              <ListGames>{giftGames}</ListGames>
            </Section>
          )}

          {subscriptionsGames && (
            <Section title="Подписки">
              <ListGames>{subscriptionsGames}</ListGames>
            </Section>
          )}
        </div>
      </Container>

      <LatestNews />
    </>
  )
}

export default Home
