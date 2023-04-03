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
        <div className="grid gap-x-8 lg:grid-cols-12">
          <div className="lg:col-span-3">
            <FilterGames />
          </div>

          <div className="lg:col-span-9">
            <div className="grid grid-cols-1 gap-x-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
              {data?.map(({ title, coverImg, price, link }, id) => (
                <div className="w-full" key={id}>
                  <GameCard title={title} coverImg={coverImg} link={link} badge="New" price={price} sale={15} />
                </div>
              ))}
            </div>

            <Pagination />
          </div>
        </div>
      </Section>
    </>
  )
}

export default CatalogPage
