import Breadcrumbs from 'components/Breadcrumbs'
import Section from 'components/Section'
import Pagination from 'components/Pagination'
import { GameCard, FilterGames } from 'features/games'
import { GameCardInterface } from 'features/games'

async function getData(): Promise<GameCardInterface[]> {
  const res = await fetch('http://localhost:3100/api/catalog-page')
  if (!res.ok) {
    return []
  }
  return res.json()
}

const CatalogPage = async () => {
  const data = await getData()
  return (
    <>
      <Section
        first
        last
        items={[
          {
            title: {
              children: (
                <>
                  Каталог <span>(35430 игр)</span>
                </>
              ),
            },
          },
        ]}
      />
      <Section
        last
        items={[
          {
            navigation: [
              {
                children: <Breadcrumbs items={[{ name: 'Каталог' }]} />,
              },
            ],
            children: (
              <section className="section section--last section--catalog">
                <div className={'flex'}>
                  <FilterGames />

                  <div className="w-full">
                    <div className="grid gap-x-4 grid-cols-4 grid-flow-row">
                      {data.map(({ title, coverImg, price, link }, id) => (
                        <div className="w-full" key={id}>
                          <GameCard title={title} coverImg={coverImg} link={link} badge="New" price={price} sale={15} />
                        </div>
                      ))}
                    </div>

                    <Pagination />
                  </div>
                </div>
              </section>
            ),
          },
        ]}
      />
    </>
  )
}

export default CatalogPage
