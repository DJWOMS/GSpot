import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard, FilterGames } from 'features/games'
import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const CatalogPage = async () => {
  const data = await fetchServerSide<GameCardInterface[]>({
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
              <div className="grid gap-x-4 grid-cols-4 grid-flow-row">
                {data?.map(({ title, coverImg, price, link }, id) => (
                  <div className="w-full" key={id}>
                    <GameCard title={title} coverImg={coverImg} link={link} badge="New" price={price} sale={15} />
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
