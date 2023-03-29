import Section from 'components/Section'
import Carousel from 'components/Carousel'
import { GameCard } from 'features/games'
import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const LatestGames = async () => {
  const latestGames =
    (await fetchServerSide<GameCardInterface[]>({
      path: '/latest-games',
    })) ?? []

  return (
    <Section
      items={[
        {
          children: (
            <Carousel
              breakpoints={{
                0: {
                  slidesPerView: 2,
                },
                576: {
                  slidesPerView: 2,
                },
                768: {
                  slidesPerView: 3,
                },
                1200: {
                  slidesPerView: 5,
                },
              }}
            >
              {latestGames.map((game, index) => (
                <GameCard key={index} {...game} />
              ))}
            </Carousel>
          ),
          title: 'Latest releases',
        },
      ]}
    />
  )
}

export default LatestGames
