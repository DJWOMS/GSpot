import ContactsPage from 'app/(main)/contacts/page'
import CarouselSection from 'components/CarouselSection'
import { Container } from 'components/Container'
import Section from 'components/Section'
import { GameCard, GameCardBig, GameCardInterface, ListGames, GameListInterface } from 'features/games'
import { LatestNews } from 'features/news'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

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
        <ContactsPage />
      </Container>

      <LatestNews />
    </>
  )
}

export default Home
