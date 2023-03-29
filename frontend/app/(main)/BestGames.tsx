import Carousel from 'components/Carousel'
import Section from 'components/Section'
import CardBig from 'components/CardBig'
import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const BestGames = async () => {
  const bestGames =
    (await fetchServerSide<GameCardInterface[]>({
      path: '/best-games',
    })) ?? []

  return (
    <Section
      bg
      first
      items={[
        {
          title: {
            children: (
              <>
                <b>Лучшие игры</b> этого месяца
              </>
            ),
            uppercase: true,
          },
          children: (
            <Carousel
              breakpoints={{
                0: {
                  slidesPerView: 1,
                },
                576: {
                  slidesPerView: 2,
                },
                768: {
                  slidesPerView: 1,
                },
                1200: {
                  slidesPerView: 2,
                },
              }}
            >
              {bestGames.map((game, index) => (
                <CardBig key={index} {...game} />
              ))}
            </Carousel>
          ),
        },
      ]}
    />
  )
}

export default BestGames
