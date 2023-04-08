import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard, FilterGames } from 'features/games'
import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const CatalogPage = async () => {
  const games = await fetchServerSide<GameCardInterface[]>({
    path: '/games/list',
  })

  return (
    <>
      <Section
        title={
          <>
            Каталог <span>(35430 игр)</span>
          </>
        }
      />

      <Section last>
        <section className="section section--last section--catalog">
          <div className={'flex'}>
            <FilterGames />

            <div className="w-full">
              <div className="grid grid-flow-row grid-cols-4 gap-x-4">
                {games?.map((game, index) => (
                  <div className="w-full" key={index}>
                    <GameCard {...game} />
                  </div>
                ))}
              </div>

              <Pagination />
            </div>
          </div>
        </section>
      </Section>
    </>
  )
}

export default CatalogPage
